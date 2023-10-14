#!/usr/bin/python3

def number_keys(a_dictionary):
    num = 0
    listKeys = list(a_dictionary.keys())

    for i in listKeys:
        num += 1

    return (num)
