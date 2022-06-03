from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
import spy
from random import randint
candies = 0


def hi_command(update: Update, context: CallbackContext):
    spy.log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')


def help_command(update: Update, context: CallbackContext):
    spy.log(update, context)
    update.message.reply_text('/hi\n/time\n/help\n/calc\n/candy')


def time_command(update: Update, context: CallbackContext):
    spy.log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def calc_command(update: Update, context: CallbackContext):
    spy.log(update, context)
    msg = update.message.text.split()
    update.message.reply_text(f'{msg[1]} = {eval(msg[1])}')


def cand_command(update: Update, context: CallbackContext):
    spy.log(update, context)
    global candies
    candies = randint(30, 50)
    update.message.reply_text(f'On the table {candies} candies.\nEnter number of candies (no more 5)')


def bot_candy(n):
    if n % 6 == 0:
        return 1
    else:
        return n % 6


def c_command(update: Update, context: CallbackContext):
    spy.log(update, context)
    global candies
    msg = update.message.text
    candies -= int(msg)
    if candies <= 0:
        update.message.reply_text(f'On the table 0 candies\nYou are WINNER!!!)))')
        update.message.reply_text('To continue enter: /candy')
        return
    else:
        update.message.reply_text(f'On the table {candies} candies')
    bot = bot_candy(candies)
    candies -= bot
    update.message.reply_text(f'Bot took {bot} candies')
    if candies <= 0:
        update.message.reply_text(f'On the table 0 candies\nBOT is WINNER!!!)))')
        update.message.reply_text('To continue enter: /candy')
    else:
        update.message.reply_text(f'On the table {candies} candies')


