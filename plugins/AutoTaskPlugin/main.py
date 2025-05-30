from pkg.plugin.context import register, handler, BasePlugin, APIHost, EventContext
from pkg.plugin.events import GroupMessageReceived
import subprocess
import os
import re
import asyncio
import json
from datetime import datetime, timedelta, timezone
from croniter import croniter
from pkg.platform.types import *

APPLIANCE_ID = "VERSA"

# 创建UTC+8时区对象
china_tz = timezone(timedelta(hours=8))

@register(name="AutoTaskPlugin", 
          description="增加定时功能的小插件（支持±1分钟触发范围）\n/定时 添加 <任务名> <时间>\n/定时 删除 <任务名>\n/定时 列出", 
          version="1.0", 
          author="lock")
class AutoTaskPlugin(BasePlugin):

    def __init__(self, host: APIHost):
        self.host = host
        # 初始化任务列表
        self.tasks = []
        self.load_tasks()
        self.lock = asyncio.Lock()
        self.last_check_time = -1.0

        # 启动定时检查器
        self.check_timer_task = asyncio.create_task(self.check_timer())

    lock = asyncio.Lock()  # 创建一个锁以确保线程安全
    command_queue = asyncio.Queue()  # 创建一个队列以存储待处理的命令

    async def register(self) -> None:
        super().register()

    async def on_unregister(self) -> None:
        # 停止定时检查器
        self.check_timer_task.cancel()
        self.check_timer_task = None

    async def check_timer(self):
        while True:
            try:
                await asyncio.sleep(60)
                await self.check_timer_handler()
            except Exception as e:
                print(f"定时检查出错: {e}")

    async def check_timer_handler(self):
        now = datetime.now(china_tz)
        
        for task in self.tasks:
            cron_expr = task["cron"]
            try:
                # 使用当前时间的整点作为基准
                base_time = datetime(now.year, now.month, now.day, now.hour, now.minute)
                iter = croniter(cron_expr, base_time)
                next_run = iter.get_next(datetime)
                
                # 检查当前时间是否正好是触发时间
                if now.minute == next_run.minute and now.hour == next_run.hour:
                    last_triggered = task.get("last_triggered_at")
                    is_running = task.get("is_running", False)
                    
                    # 确保任务未在执行中且距上次触发至少5分钟
                    if not is_running and (last_triggered is None or (now - last_triggered).total_seconds() >= 300):
                        task["last_triggered_at"] = now
                        task["is_running"] = True
                        self.save_tasks()
                        
                        try:
                            await self.execute_task(task)
                        finally:
                            task["is_running"] = False
                            self.save_tasks()
            except Exception as e:
                print(f"解析定时任务cron表达式失败: {cron_expr}, 错误: {str(e)}")
                continue
                    
    async def execute_task(self, task):
        script_name = task["script"]
        target_id = task["target"]
        target_type = task["type"]
        task_name = task["name"]

        script_path = os.path.join(os.path.dirname(__file__), 'data', f"{script_name}.py")
        if os.path.exists(script_path):
            try:
                result = subprocess.check_output(['python', script_path], text=True, timeout=60)  # 设置超时为60秒
                messages = self.convert_message(result, target_id)
                await self.send_reply(target_id, target_type, messages)
            except subprocess.CalledProcessError as e:
                error_msg = f"定时任务 {task_name} 执行失败: {e.output}"
                await self.send_reply(target_id, target_type, [Plain(error_msg)])
            except Exception as e:
                error_msg = f"定时任务 {task_name} 发生错误: {str(e)}"
                await self.send_reply(target_id, target_type, [Plain(error_msg)])
        else:
            await self.send_reply(target_id, target_type, [Plain(f"定时任务 {task_name} 对应的脚本 {script_name}.py 不存在")])

    def convert_message(self, message, sender_id):
        parts = []
        last_end = 0
        image_pattern = re.compile(r'!\[.*?\]\((https?://\S+)\)')  # 定义图像链接的正则表达式

        # 检查消息中是否包含at指令
        if "atper_on" in message:
            parts.append(At(target=sender_id))  # 在消息开头加上At(sender_id)
            message = message.replace("atper_on", "")  # 从消息中移除"send_on"

        for match in image_pattern.finditer(message):  # 查找所有匹配的图像链接
            start, end = match.span()  # 获取匹配的起止位置
            if start > last_end:  # 如果有文本在图像之前
                parts.append(Plain(message[last_end:start]))  # 添加纯文本部分
            image_url = match.group(1)  # 提取图像 URL
            parts.append(Image(url=image_url))  # 添加图像消息
            last_end = end  # 更新最后结束位置
        if last_end +1 < len(message):  # 如果还有剩余文本
            parts.append(Plain(message[last_end:]))  # 添加剩余的纯文本

        return parts if parts else [Plain(message)]  # 返回构建好的消息列表，如果没有部分则返回纯文本消息

    async def send_reply(self, target_id, target_type, messages):
        await self.host.send_active_message(adapter=self.host.get_platform_adapters()[0],
                                            target_type=target_type,
                                            target_id=str(target_id),
                                            message=MessageChain(messages),
                                        )

    def load_tasks(self):
        """
        加载任务列表，从 tasks.json 文件中读取
        """
        try:
            with open(os.path.join(os.path.dirname(__file__), 'tasks.json'), 'r', encoding='utf-8') as file:
                tasks_data = json.load(file)
                if not isinstance(tasks_data, list):
                    self.tasks = []
                    return
                self.tasks = []
                for task_data in tasks_data:
                    task = {
                        "cron": task_data.get("cron", ""),
                        "script": task_data.get("script", ""),
                        "target": task_data.get("target", 0),
                        "type": task_data.get("type", ""),
                        "name": task_data.get("name", ""),
                        "created_at": task_data.get("created_at", ""),
                        "last_triggered_at": datetime.fromisoformat(task_data.get("last_triggered_at", "")) if task_data.get("last_triggered_at") else None
                    }
                    self.tasks.append(task)
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            self.tasks = []
        except Exception as e:
            print(f"加载定时任务失败: {str(e)}")
            self.tasks = []

    def save_tasks(self):
        """
        保存任务列表，写入到 tasks.json 文件中
        """
        try:
            tasks_data = []
            for task in self.tasks:
                task_data = {
                    "cron": task.get("cron", ""),
                    "script": task.get("script", ""),
                    "target": task.get("target", 0),
                    "type": task.get("type", ""),
                    "name": task.get("name", ""),
                    "created_at": task.get("created_at", ""),
                    "last_triggered_at": task.get("last_triggered_at").isoformat() if task.get("last_triggered_at") else None,
                    "is_running": task.get("is_running", False)
                }
                tasks_data.append(task_data)
            with open(os.path.join(os.path.dirname(__file__), 'tasks.json'), 'w', encoding='utf-8') as file:
                json.dump(tasks_data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"保存定时任务失败: {str(e)}")

    @handler(GroupMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        await self.command_queue.put(ctx)  # 将命令上下文放入队列
        await self.process_commands()  # 处理命令

    async def process_commands(self):
        while not self.command_queue.empty():  # 当队列不为空时
            ctx = await self.command_queue.get()  # 从队列中获取命令上下文
            await self.handle_command(ctx, 'group')  # 执行命令
            await asyncio.sleep(2)  # 等待 2 秒再处理下一个命令

    async def handle_command(self, ctx: EventContext, target_type):
        msg = str(ctx.event.message_chain).strip()

        launcher_id = str(ctx.event.launcher_id)
        launcher_type = str(ctx.event.launcher_type)
        
        # 获取黑/白名单
        pipeline_cfg = await self.ap.pipeline_service.get_pipeline('0525bcd5-3c3c-48a9-aae3-17bfc94dcbaf')
        mode = pipeline_cfg['config']['trigger']['access-control']['mode']
        sess_list = pipeline_cfg['config']['trigger']['access-control'][mode]

        found = False
        if (launcher_type== 'group' and 'group_*' in sess_list) \
            or (launcher_type == 'person' and 'person_*' in sess_list):
            found = True
        else:
            for sess in sess_list:
                if sess == f"{launcher_type}_{launcher_id}":
                    found = True
                    break 
        ctn = False
        if mode == 'whitelist':
            ctn = found
        else:
            ctn = not found
        if not ctn:
            # print(f'您被杀了哦')
            return

        # 处理 cmd，如果包含 / 则删除 /
        if '/' in msg:
            msg = msg.replace('/', '')  # 删除所有 /，只保留文字部分

        # 检查消息是否以“定时”开头
        if msg.startswith("定时"):
            command = msg.split(' ', 3)  # 拆分命令为最多四个部分

            # 命令结构：定时 [子命令] [任务名] [时间]
            # 例如：定时 添加 早报 6:00
            #       定时 删除 早报
            #       定时 列出

            subcmd = command[1].strip() if len(command) > 1 else ""
            task_name = command[2].strip() if len(command) > 2 else ""
            task_time = command[3].strip() if len(command) > 3 else ""
            sender_id = ctx.event.sender_id
            group_id = ctx.event.launcher_id

            if subcmd == "添加":
                await self.add_task(ctx, target_type, group_id, task_name, task_time)
            elif subcmd == "删除":
                await self.delete_task(ctx, target_type, group_id, task_name)
            elif subcmd == "列出":
                await self.list_tasks(ctx, target_type, group_id)
            else:
                await ctx.reply(MessageChain([Plain("请使用以下格式：\n/定时 添加 <任务名> <时间>\n/定时 删除 <任务名>\n/定时 列出\n例如：定时 添加 早报 8:10\n任务名仅能触发/data目录下脚本\n目前有任务：\n早报")]))

    async def add_task(self, ctx: EventContext, target_type, group_id, task_name, task_time):
        # 检查任务名称是否已存在
        for task in self.tasks:
            if task["name"] == task_name and task["time"] == task_time:
                await ctx.reply(MessageChain([Plain(f"定时任务 {task_name} 已存在，请使用其他名称!")]))
                return

        # 验证cron表达式是否正确
        try:
            # 验证cron表达式是否正确
            croniter(task_time)
        except ValueError as e:
            await ctx.reply(MessageChain([Plain(f"cron表达式格式不正确: {str(e)}")]))
            return

        # 保存任务信息
        new_task = {
            "cron": task_time,
            "script": f"{task_name}",  # 脚本名称与任务名一致，需要存放在 data/目录下
            "target": group_id,
            "type": target_type,
            "name": task_name,
            "created_at": datetime.now(china_tz).strftime("%Y-%m-%d %H:%M:%S"),
            "last_triggered_at": None  # 添加一个新字段，用于记录任务的最后触发时间
        }

        self.tasks.append(new_task)
        self.save_tasks()

        await ctx.reply(MessageChain([Plain(f"定时任务 {task_name} 已添加，时间：{task_time}")]))

    async def delete_task(self, ctx: EventContext, target_type, sender_id, task_name):
        # 查找并删除任务
        for task in self.tasks:
            if task["name"] == task_name :
                self.tasks.remove(task)
                self.save_tasks()
                await ctx.reply(MessageChain([Plain(f"定时任务 {task_name} 已删除!")]))
                return

        await ctx.reply(MessageChain([Plain(f"定时任务 {task_name} 不存在!")]))

    async def list_tasks(self, ctx: EventContext, target_type, sender_id):
        tasks_info = []
        for task in self.tasks:
            if task["target"] == sender_id and task["type"] == target_type:
                tasks_info.append(f"{task['name']} - cron: {task['cron']} - {task['created_at']} (最后触发时间: {task.get('last_triggered_at', '从未触发')})")

        if tasks_info:
            message = "\n".join(tasks_info)
        else:
            message = "没有找到任何定时任务!"

        await ctx.reply(MessageChain([Plain(message)]))

    def __del__(self):
        # 清理定时检查器
        if self.check_timer_task:
            self.check_timer_task.cancel()