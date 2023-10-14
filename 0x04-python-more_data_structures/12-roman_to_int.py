#!/usr/bin/python3
def to_subtract(listNum):
    to_sub = 0
    maxList = max(listNum)

    for n in listNum:
        if maxList > n:
            to_sub += n

    return (maxList - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    romNm = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    listKeys = list(romNm.keys())

    num = 0
    lastRom = 0
    listNum = [0]

    for ch in roman_string:
        for r_num in listKeys:
            if r_num == ch:
                if romNm.get(ch) <= lastRom:
                    num += to_subtract(listNum)
                    listNum = [romNm.get(ch)]
                else:
                    listNum.append(romNm.get(ch))

                lastRom = romNm.get(ch)

    num += to_subtract(listNum)

    return (num)
