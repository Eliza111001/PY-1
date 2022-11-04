import random

def get_unique_list_numbers() -> list[int]:
    from random import randint
    min_ = -10
    max_ = 10
    len_ = 15
    list_unique_numbers = [random.randint(min_, max_) for _ in range(len_)]

    while len(list_unique_numbers) != len(set(list_unique_numbers)):
            list_unique_numbers = [random.randint(min_, max_) for _ in range(len_)]
    return list_unique_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))