from random import choice

def buffer_word_user(word_user, list_buffer, word):
    if word_user in list_buffer:
        #print(list_buffer)
        print(f'{word.title()} уже был назван')
        # text_for_bot(f'{word.title()} уже был назван')
        word_user = input(f'Напиши {word}:')
        # word_user = text_for_bot(f'Напиши {word}:')
        return word_user
    # list_buffer.append(word_user)
    return word_user

def buffer_word_computer(word, list_buffer, dict_city, user_letter):
    if word in list_buffer:
        word = buffer_word_computer(choice(dict_city[user_letter]), list_buffer, dict_city, user_letter)
        return word
    else:
        return word
    # list_buffer.append(word)


