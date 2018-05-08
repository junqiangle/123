import random


def cookie():
    my_str = 'abcdefghijklmnopq1234567890'
    total = ''
    for v in range(12):
        total += random.choice(my_str)
    return total