import math


def is_armstrong_number(number):
    if number > 0:
        power = math.ceil(math.log10(number))
    clone = number
    res = 0
    while clone > 0:
        res += (clone % 10)**power
        clone = math.floor(clone/10)
    return res == number
