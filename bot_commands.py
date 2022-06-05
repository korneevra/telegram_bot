from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
import spy
from random import randint
import tic_tac_toe
candies = 0


def hi_command(update: Update, context: CallbackContext):
    spy.log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')


def help_command(update: Update, context: CallbackContext):
    spy.log(update, context)
    update.message.reply_text('/hi\n/time\n/help\n/calc\n/candy\n/ttt - "TicTacToe"')


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
        update.message.reply_text('To new game enter: /candy')
    else:
        update.message.reply_text(f'On the table {candies} candies')


def ttt_command(update: Update, context: CallbackContext):

    def field_print(t):
        for i in range(3):
            s = '| '
            for j in range(3):
                s += t[i][j] + ' | '
            update.message.reply_text(s)

    tic_tac_toe.t_map = tic_tac_toe.field_init()
    field_print(tic_tac_toe.t_map)
    update.message.reply_text('Enter /t X Y (0,1,2 through space): ')


def t_command(update: Update, context: CallbackContext):

    def field_print(t):
        for i in range(3):
            s = '| '
            for j in range(3):
                s += t[i][j] + ' | '
            update.message.reply_text(s)

    # update.message.reply_text('Enter /t X Y (0,1,2 through space): ')
    msg = update.message.text.split()
    human = [int(msg[1]), int(msg[2])]
    if not (tic_tac_toe.is_valid_cell(human) and tic_tac_toe.cell_empty(human)):
        update.message.reply_text('Wrong coordinates')
        return
    tic_tac_toe.t_map[human[1]][human[0]] = tic_tac_toe.dot_hum
    field_print(tic_tac_toe.t_map)
    if tic_tac_toe.win_check(tic_tac_toe.dot_hum):
        update.message.reply_text("Your WIN!\nTo new game enter /ttt")
        return
    elif tic_tac_toe.map_full(tic_tac_toe.t_map):
        update.message.reply_text("Drawn game!\nTo new game enter /ttt")
        return
    bot = tic_tac_toe.bot_turn()
    tic_tac_toe.t_map[bot[1]][bot[0]] = tic_tac_toe.dot_bot
    update.message.reply_text('BOT turn:')
    field_print(tic_tac_toe.t_map)
    if tic_tac_toe.win_check(tic_tac_toe.dot_bot):
        update.message.reply_text("Bot WIN!\nTo new game enter /ttt")
        return
    elif tic_tac_toe.map_full(tic_tac_toe.t_map):
        update.message.reply_text("Drawn game!\nTo new game enter /ttt")
        return
    else:
        update.message.reply_text('Your turn,\nEnter /t X Y (0,1,2 through space): ')
