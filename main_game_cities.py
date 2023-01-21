from list_cities import create_result_dict_city
from list_letters import letters
from check_letter import check_letter_computer, check_letter_user
from buffer_word import buffer_word_user, buffer_word_computer
from admin_help import admin_command_help
from check_count_answer import check_count_answer
from random import choice
# from aiogram import types
# from bot import create_bot

# cr_bot = create_bot()
# bot = cr_bot[0]
# dp = cr_bot[1]
#
# @dp.message_handler()
# async def message_bot(msg : types.Message, text_bot):
#     await bot.send_message(msg.from_user.id, text_bot)
#     return msg.text.lower()

def return_computer_word(user_letter, dict_city, buffer):
    user_letter = check_letter_user(user_letter)
    #print(users_letter, '- буква пользователя')
    word_computer = choice(dict_city[user_letter])
    buffer_word_computer(word_computer, buffer, dict_city, user_letter)
    buffer.append(word_computer)
    return word_computer

def get_word_user(word_user, dict_city, word_computer, example_input_user_word, buffer, word, count_wrong_ans):
    for values in dict_city.values():
        if word_user in values:
            buffer.append(word_user)
            return check_letter_computer(word_user)

    else:
        count_wrong_ans += 1
        if check_count_answer(count_wrong_ans):
            print('Попытки закончилсь. Ты проиграл!\nНе переживай, компьютер сложно выйграть :)')
            # send_message_bot('Попытки закончилсь. Ты проиграл!\nНе переживай, компьютер сложно выйграть :)')
            return True
        else:
            word_user = input(f'Такого {word} нет\n{example_input_user_word}\nНапиши {word} get word:\t').lower()
            # word_user = send_message_bot(f'Такого {word} нет\n{example_input_user_word}\nНапиши {word}:')
            word_user = admin_command_help(word_user, dict_city, word_computer, buffer, word)
            # word_user = buffer_word_user(word_user, word_computer, buffer, example_input_user_word, word)
            word_user = buffer_word_user(word_user, buffer, word)
            return get_word_user(word_user, dict_city, word_computer, example_input_user_word, buffer, word, count_wrong_ans)

def check_letter_users(word_user, word_computer, dict_city, example_input_user_word, buffer, word, count_wrong_ans):
    if word_user[0] == check_letter_computer(word_computer)[-1]:
        user_letter = get_word_user(word_user, dict_city, word_computer, example_input_user_word, buffer, word, count_wrong_ans)
        if user_letter == True:
            return True
        else:
            return return_computer_word(user_letter, dict_city, buffer)
    else:
        count_wrong_ans += 1
        if check_count_answer(count_wrong_ans):
            print('Попытки закончилсь. Ты проиграл!\nНе переживай, компьютер сложно выйграть :)')
            # send_message_bot('Попытки закончилсь. Ты проиграл!\nНе переживай, компьютер сложно выйграть :)')
            return True
        else:
            print(f'{word.title()} должен начинаться с "{word_computer[-1].upper()}"\n{word_computer} - {check_letter_computer(word_computer)}')
            # send_message_bot(f'{word.title()} должен начинаться с "{word_computer[-1].upper()}"\n{word_computer} - {check_letter_computer(word_computer)}')
            word_user = input('Напиши город check letter:\t').lower()
            # word_user = send_message_bot('Напиши {word}:')
            word_user = admin_command_help(word_user, dict_city, word_computer, buffer, word)
            word_user = buffer_word_user(word_user, buffer, word)
            return check_letter_users(word_user, word_computer, dict_city, example_input_user_word, buffer, word, count_wrong_ans)

def choice_game(): #msg : types.Message
    qustion = input('Во что хочешь сыграть сегодня? (1-слова (русские), 2-слова (английские), 3-города):\t')
    # await message_bot(msg, 'Во что хочешь сыграть сегодня? (1-слова (русские), 2-слова (английские), 3-города):')
    # qustion = msg.text.lower()
    # qustion = text_for_bot(text_bot.text)
    if qustion == '1':
        word = 'слово'
        path = 'words'
        return create_result_dict_city(path), word
    elif qustion == '3':
        word = 'город'
        path = 'cities'
        return create_result_dict_city(path), word
    else:
        print('Я тебя не понимаю. Напиши еще раз')
        return choice_game()
        # text_bot = SendTextBot('Я тебя не понимаю. Напиши еще раз')
        # await message_bot(msg, 'Я тебя не понимаю. Напиши еще раз')
        # await choice_game(msg)

def preparation_game():
    count_wrong_ans = 0
    dict_city_word = choice_game()
    dict_city = dict_city_word[0]
    word = dict_city_word[1]
    lst_letters = letters() # список букв
    buffer = []
    word_computer = return_computer_word(choice(lst_letters), dict_city, buffer)
    return word_computer.title(), dict_city, word, buffer, count_wrong_ans

def game():
    info = preparation_game()
    word_computer = info[0]
    dict_city = info[1]
    word = info[2]
    buffer = info[3]
    count_wrong_ans = info[4]
    print(word_computer.title())
    while True:
        word_user = input(f'Напиши {word} while:\t').lower()
        # word_user = send_message_bot(f'Напиши {word}:')
        if word_user == 'off':
            break
        example_input_user_word = f'{word_computer} - {word_computer[-1].upper()}'
        word_user = admin_command_help(word_user, dict_city, word_computer, buffer, word)
        word_user = buffer_word_user(word_user, buffer, word)
        word_computer = check_letter_users(word_user, word_computer, dict_city, example_input_user_word, buffer, word, count_wrong_ans)
        if word_computer == True:
            break
        print(word_computer.title())
        # send_message_bot(word_computer)

game()

