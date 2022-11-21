import json

INPUT_FILE = "input1.csv"

import csv
def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
     with open(filename, encoding="utf-8") as f:
        data_ = []
        for line_ in f:
            data_.append([char.rstrip(new_line) for char in line_.split(delimiter)])

     result = []

     for number_of_strip in range(1, len(data_)):
         current_dict = {}
         for number_of_value in range(len(data_[0])):
            current_dict.update({data_[0][number_of_value]: data_[number_of_strip][number_of_value]})

         result.append(current_dict)

     return result

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
