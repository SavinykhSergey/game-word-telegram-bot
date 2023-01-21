def check_letter_computer(word):
    if word[-1] == 'ь' or word[-1] == 'ы':
        return word[-2]
    else:
        return word[-1]

def check_letter_user(word):
    if word[-1] == 'ь' or word[-1] == 'ы':
        return word[:-1]
    else:
        return word