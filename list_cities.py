def read_city_from_file(path):
    list_city = []
    with open(path, 'r', encoding='utf-8') as file_city:
        for city in file_city:
            list_city.append(city.lower())
    return list_city

def create_dict_city_word(path):
    list_city = read_city_from_file(path)
    text_dict_letters_words = {}
    for value in list_city:
        if value[0] not in text_dict_letters_words:
            text_dict_letters_words[value[0]] = value
        else:
            text_dict_letters_words[value[0]] += f' {value}'
    return text_dict_letters_words

def create_result_dict_city(path):
    text_dict_letters_words= create_dict_city_word(path)
    dict_letters_words = {}
    for key in text_dict_letters_words:
        dict_letters_words[key] = text_dict_letters_words[key].split()
    # await dict_letters_words
    return dict_letters_words



