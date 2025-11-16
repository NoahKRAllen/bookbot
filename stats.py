from typing import Any


def num_words_in_string(string):
    return len(string.split())

def amount_of_each_char(string):
    lower_string = string.lower()
    char_dict = {}
    for char in lower_string:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def sorted_dict(dict_to_sort):
    return dict(sorted(dict_to_sort.items(), key=lambda item: item[1], reverse=True))