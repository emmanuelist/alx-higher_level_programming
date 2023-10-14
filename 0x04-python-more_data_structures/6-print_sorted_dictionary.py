#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    listOrder = list(a_dictionary.keys())
    listOrder.sort()
    for i in listOrder:
        print("{}: {}".format(i, a_dictionary.get(i)))
