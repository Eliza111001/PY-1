list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_ = max(list_numbers)
for i in range(len(list_numbers)):
    if list_numbers[i] == max_:
        i_max = i
        break
list_numbers[i_max], list_numbers[-1] = list_numbers[-1], list_numbers[i_max]
print(list_numbers)
