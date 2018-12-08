# _*_ coding: utf-8 _*_
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, InlineQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, InputTextMessageContent, InlineQueryResultArticle, MessageEntity, error, ParseMode
from telegram.chataction import ChatAction
from uuid import uuid4
from time import sleep
import random
import time

updater = Updater("Paste Your Token Here")

def start(bot, update):
    bot.send_chat_action(update.message.chat_id, ChatAction.TYPING)                              # this is a chat action for bot
    bot.send_message(chat_id = update.message.chat_id, text = "Hello {}".format(update.message.from_user.first_name))
    print(update.message.from_user)                              # how many people start bot
    # print("time is: ", time.localtime().tm_hour)

def random_func(bot, update):
    answer = random.randint(1,5)                              # random modul in python telegram bot
    bot.send_message(chat_id = update.message.chat_id, text = answer)

def picture(bot, update):                              # send picture to user
    bot.send_chat_action(update.message.chat_id, ChatAction. UPLOAD_PHOTO)                              # chat action for picture
    bot.send_photo(chat_id = update.message.chat_id, photo = open("location of file/name.jpg", "rb"), caption = "this is a caption")

def document(bot, update):                              # send doc to user
    bot.send_chat_action(update.message.chat_id, ChatAction.UPLOAD_DOCUMENT)                              # chat action for doc
    bot.send_document(chat_id = update.message.chat_id, document = open("location of bot/name.pdf", "rb"), caption = "this is a caption")

def audio(bot, update):                              # send audio to user
    bot.send_chat_action(update.message.chat_id, ChatAction.UPLOAD_AUDIO)                              # send chat action for audio
    bot.send_audio(chat_id = update.message.chat_id, audio = open("your file location/name.mp3", "rb"), caption = "this is a caption")

def location(bot, update):                              # send location to user
    chat_id = update.message.chat_id
    bot.send_location(chat_id, "", "")                              # write your location in ""

def sticker(bot, update):                              # send sticker to user
    chat_id = update.message.chat_id
    bot.sendSticker(chat_id, open("location of file/.stiker.webp", "rb"))

def text_filter(bot, update):                              # if user send text to bot you can control text
    # if update.message.from_user.id == 577559733:                              # in group who is admin # write your id(number)
    #     bot.send_message(chat_id = update.message.chat_id, text = "Hello Admin")

    # elif time.localtime().tm_hour == 12:                              # at 12:00 nobody cant send text in group
    #     bot.send_message(chat_id = update.message.chat_id, text = "time: 12:00")

    # elif (update.message.parse_entities(types = anti_link)):                              # anti link
    #     bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)

    # elif (update.message.parse_entities(type = anti_spam) or update.message_parse_caption_entities(type = anti_spam)):                              # anti apam
    #     bot.delete_message(chat_id = update.message.chat_id , message_id = update.message.message_id)

    if update.message.text == u"show keyboard" :                              # if user send show keyboard bot show 2 keyboard to user
        keyboard = [
            ["My ID"],
            ["info"]
            ]
        bot.sendMessage(update.message.chat_id, "choose a Button:", reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))

    elif update.message.text == "My ID":
        bot.sendMessage(update.message.chat_id, text = update.message.from_user.id)

    elif update.message.text == "info":
        keyboard = [
            [InlineKeyboardButton("text", "https://t.me/white_roze")]                              # write your username here
            ]
        bot.sendMessage(update.message.chat_id, "text", reply_markup =  InlineKeyboardMarkup(keyboard))

    elif update.message.text == "delete":                              # bot delete the message     (for word filtering)
        bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)
    elif update.message.text == "sleep":                              # use sleep library in bot
        bot.send_message(chat_id = update.message.chat_id, text = "one")
        sleep(3)                              # stop 3 secend
        bot.send_message(chat_id = update.message.chat_id, text = "two")

def photo_filter(bot, update):                              # if user send photo to bot, bot what should do
    bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)

def video_filter(bot, update):
    bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)

def doc_filter(bot, update):
    bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)

def audio_filter(bot, update):
    bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)

def animation_filter(bot, update):
    bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)

def command_filter(bot, update):
    bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)

def contact_filter(bot, update):
    bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)

def location_filter(bot, update):
    bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)

def reply_filter(bot, update):
    bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)

def sticker_filter(bot, update):
    bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)

def video_note_filter(bot, update):
    bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)

def voice_filter(bot, update):
    bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)

def forwarded_filter(bot, update):                              # bot delete forwarded message in group
    if update.message.parse_entities(types = [MessageEntity.forwarded]):
        bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)

def inlinequery(bot, update):
    list().append(InlineQueryResultArticle(id = uuid4(), title = "Uppercase", input_message_content = InputTextMessageContent(update.inline_query.query.upper())))
    list().append(InlineQueryResultArticle(id = uuid4(), title = "Lowercase", input_message_content = InputTextMessageContent(update.inline_query.query.lower())))
    bot.answerInlineQuery(update.inline_query.id, results = list())

def button_last(bot, update):                              # this is a model of button (past version)
    keyboard = [
        [InlineKeyboardButton("button 1", callback_data = "a1")],
        [InlineKeyboardButton("button 2", callback_data = "a2")]
        ]
    update.message.reply_text("pleas choose a button :", reply_markup = InlineKeyboardMarkup(keyboard))
def button_last_handler(bot, update):
    query = update.callback_query
    # print(query.data)
    if (query.data == "a1"):
        bot.send_message(chat_id = query.message.chat_id, text = "you choose button 1")
    elif (query.data == "a2"):
        bot.send_message(chat_id = query.message.chat_id, text = "you choose button 2")

def button(bot, update):                              # this bot is last version of button
    keyboard = [
        [InlineKeyboardButton("button 1", callback_data = "1")]
        ]
    bot.sendMessage(update.message.chat_id, "choose a button", reply_markup =  InlineKeyboardMarkup(keyboard))
def button_handler(bot, update):
    query = update.callback_query

    if query.data == "1":
        keyboard = [
            [InlineKeyboardButton("button 2", callback_data = "2")],
            [InlineKeyboardButton("button 3", callback_data = "3")]
            ]
        bot.editMessageText(text = "choose another button", chat_id = query.message.chat_id, message_id = query.message.message_id, reply_markup =  InlineKeyboardMarkup(keyboard))
    elif query.data == "2":
        keyboard = [
            [InlineKeyboardButton("button 2.1", callback_data = "4")],
            [InlineKeyboardButton("button 2.2", callback_data = "5")]
            ]
        bot.editMessageText(text ="choose another button", chat_id = query.message.chat_id, message_id = query.message.message_id, reply_markup =  InlineKeyboardMarkup(keyboard))
    elif query.data == "3":
        keyboard = [
            [InlineKeyboardButton("button 3.1", callback_data = "6")],
            [InlineKeyboardButton("button 3.2", callback_data = "7")]
            ]
        bot.editMessageText(text = "dont choose button", chat_id = query.message.chat_id, message_id = query.message.message_id, reply_markup =  InlineKeyboardMarkup(keyboard))

updater.dispatcher.add_handler(CommandHandler("button", button))
updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("random", random_func))
updater.dispatcher.add_handler(CommandHandler("picture", picture))
updater.dispatcher.add_handler(CommandHandler("document", document))
updater.dispatcher.add_handler(CommandHandler("audio", audio))
updater.dispatcher.add_handler(CommandHandler('location', location))
updater.dispatcher.add_handler(CommandHandler('sticker', sticker ))
updater.dispatcher.add_handler(CommandHandler("normal", button_last))
updater.dispatcher.add_handler(CallbackQueryHandler(button_last_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text_filter))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, photo_filter))
updater.dispatcher.add_handler(MessageHandler(Filters.video, video_filter))
updater.dispatcher.add_handler(MessageHandler(Filters.document, doc_filter))
updater.dispatcher.add_handler(MessageHandler(Filters.audio, audio_filter))
updater.dispatcher.add_handler(MessageHandler(Filters.animation, animation_filter))
updater.dispatcher.add_handler(MessageHandler(Filters.command, command_filter))
updater.dispatcher.add_handler(MessageHandler(Filters.contact, contact_filter))
updater.dispatcher.add_handler(MessageHandler(Filters.location, location_filter))
updater.dispatcher.add_handler(MessageHandler(Filters.reply, reply_filter))
updater.dispatcher.add_handler(MessageHandler(Filters.sticker, sticker_filter))
updater.dispatcher.add_handler(MessageHandler(Filters.video_note, video_note_filter))
updater.dispatcher.add_handler(MessageHandler(Filters.voice, voice_filter))
updater.dispatcher.add_handler(MessageHandler(Filters.forwarded, forwarded_filter))
updater.dispatcher.add_handler(InlineQueryHandler(inlinequery))
updater.start_polling()
updater.idle()                              # now you can cancel in terminal width ctr+c
