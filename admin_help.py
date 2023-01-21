from check_letter import check_letter_computer
# from send_message_bot import text_for_bot
from buffer_word import buffer_word_user
from aiogram import types

def check_command_admin(word, dict_city, buffer, word_computer):
    flag = True
    if word == 'admin':
        word = dict_city[check_letter_computer(word_computer)]
        flag = True
    elif word == 'buffer':
        word = buffer
        flag = True
    else:
        flag = False
    return word, flag

def admin_command_help(word_user, dict_city, word_computer, buffer, word):
    check = check_command_admin(word_user, dict_city, buffer, word_computer)
    #print('пройдено admin')
    if check[-1]:
        print(check[0])
        word_user = input(f'Напиши {word} admin:\t').lower()
        # word_user = text_for_bot(f'Напиши {word}:')
        word_user = buffer_word_user(word_user, buffer, word)
        return word_user
    return word_user