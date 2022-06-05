from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, filters
from bot_commands import *
import settings

updater = Updater(settings.bot_token)

updater.dispatcher.add_handler(CommandHandler("hi", hi_command))
updater.dispatcher.add_handler(CommandHandler("time", time_command))
updater.dispatcher.add_handler(CommandHandler("t", t_command))
updater.dispatcher.add_handler(CommandHandler("ttt", ttt_command))
updater.dispatcher.add_handler(CommandHandler("help", help_command))
updater.dispatcher.add_handler(CommandHandler("calc", calc_command))
updater.dispatcher.add_handler(CommandHandler("candy", cand_command))
updater.dispatcher.add_handler(CommandHandler("duck", duck_command))
updater.dispatcher.add_handler(MessageHandler(filters.Filters.text, c_command))

print('server start')

updater.start_polling()
updater.idle()

