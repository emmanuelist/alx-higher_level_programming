#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniqList = set(my_list)
    num = 0

    for i in uniqList:
        num += i

    return (num)
