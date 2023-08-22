#!/usr/bin/env python3
from typing import Final
from telegrambot import TeleBot, filters
import asyncio

BOT_USERNAME: Final = 'your_bot_name'
token = 'your_token_key'

with open("security_token.txt", "r") as f:
    token = f.read()

app = TeleBot(token)

@app.handle_message(filters.TEXT & ~filters.COMMAND)
async def handle_message(update, context):
    lastmessage = update.message.text
    await update.message.reply_text(f"echo : {lastmessage}")

@app.handle_command("chatid")
async def getchatid(update, context):
    chatid = update.effective_message.chat_id

    print(f"[request] /chatid : {chatid}")

    await update.message.reply_text(f"your chatid is")
    await update.message.reply_text(f"{chatid}")

#app.send_to_user("hello?", "your_chat_id")
#app.send_to_users("hello?", ["your_chat_id", "your_chat_id"])

app.start()