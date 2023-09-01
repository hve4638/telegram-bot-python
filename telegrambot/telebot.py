import requests
import asyncio
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

class TeleBot:
    def __init__(self, token:str):
        self.app = Application.builder().token(token).build()
        self.bot = self.app.bot
        self.send_url = f'https://api.telegram.org/bot{token}/sendMessage'

    def handle_command(self, text):
        def decorator(func):
            self.app.add_handler(CommandHandler(text, func))
            return func
        return decorator
    
    def handle_message(self, text):
        def decorator(func):
            self.app.add_handler(MessageHandler(text, func))
            return func
        return decorator
        
    async def __send_message(self, text, chat_id):
        requests.post(self.send_url, json={'chat_id': chat_id, 'text': text})

    def send_to_user(self, text, target):
        asyncio.run(self.__send_message(text=text, chat_id=target))
            
    def send_to_users(self, text, targets):
        for chat_id in targets:
            asyncio.run(self.__send_message(text=text, chat_id=chat_id))
    
    def start(self):
        print("run polling...")
        self.app.run_polling(allowed_updates=Update.ALL_TYPES)