def get_count_char(str_):
    dict_ = {}
    str_ = ''.join(str_.lower().split())
    for char_ in str_:
        if char_.isalpha() == True:
            if char_ in dict_:
                dict_[char_] += 1
            else:
                dict_[char_] = 1
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))


check_dict = {
    'a': 2,
    'b': 3,
    'c': 5
}

def percent(dict_symbols):
    new_dict = {}
    total_count = sum(dict_symbols.values())
    list_symbols = []
    for symbol, count in dict_symbols.items():
        list_symbols.append(symbol)
        count = round(count / total_count * 100, 2)
        dict_symbols[symbol] = count

    return dict_symbols

print(percent(check_dict))
