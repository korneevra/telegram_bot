from telegram import Update, update
from telegram.ext import Updater, CommandHandler, CallbackContext
from random import randint

dot_empty = '  '
dot_hum = 'x'
dot_bot = 'o'
field_size = 3
line_size = 3
t_map = []


def field_init():
    return [['  ' for j in range(field_size)] for i in range(field_size)]


def cell_empty(cell):
    return t_map[cell[1]][cell[0]] == '  '


def is_valid_cell(cell):
    return (cell[0] < field_size) and (cell[1] < field_size) and (cell[0] >= 0) and (cell[1] >= 0)


def bot_turn():
    while True:
        bot = [randint(0, field_size - 1), randint(0, field_size - 1)]
        if is_valid_cell(bot) and cell_empty(bot):
            return bot


def win_check(dot):
    if t_map[0][0] == t_map[1][0] == t_map[2][0] == dot: return True
    if t_map[0][1] == t_map[1][1] == t_map[2][1] == dot: return True
    if t_map[0][2] == t_map[1][2] == t_map[2][2] == dot: return True
    if t_map[0][0] == t_map[0][1] == t_map[0][2] == dot: return True
    if t_map[1][0] == t_map[1][1] == t_map[1][2] == dot: return True
    if t_map[2][0] == t_map[2][1] == t_map[2][2] == dot: return True
    if t_map[0][0] == t_map[1][1] == t_map[2][2] == dot: return True
    if t_map[0][2] == t_map[1][1] == t_map[2][0] == dot: return True


