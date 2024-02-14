from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions
import pyrogram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import os
api_id = 19576945
api_hash = "07fca730186bb632bcb8e4f78302a84c"
bot_token = "6633455116:AAFP4ASvIG6Qm-sRsMfP5z6TOygivjNbuRo"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)
#83zA&#aVqdtc$6$Tr430

from pyrogram import Client
from pyrogram.types import (InlineQueryResultArticle,InlineQueryResultCachedSticker, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
                            
@app.on_message(filters.private)
def start(client,message):
	message.reply("инструкция по использованию бота @anystiinfo ")
                            
@app.on_inline_query()
def anwer(_, inline_query):
	query = inline_query.query
	reslist=[]
	nw =[]
	
	try:
		for i in os.listdir(f"{query}"):
			f = open(f"{query}/{i}").read()
			reslist += [f]
			print(inline_query)
			print("...")
		for i in reslist:
			nw += [InlineQueryResultCachedSticker(sticker_file_id=i)]
		inline_query.answer(
		is_gallery=True,
    results=nw
    )
	except:
	       	
	       	inline_query.answer(
        	results=[
            InlineQueryResultArticle(
            title="инструкция",
            input_message_content="перейдите в лс бота, чтобы получить инструкцию"
                )
                ]
                )


app.run()
