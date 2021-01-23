#Uses python3

import sys
from collections import namedtuple


class Number:

    def __init__(self, anumber):
        self.digits = anumber
        self.first = int(anumber[0])
        self.second = int(anumber[1]) if len(anumber) > 1 else -1
        self.third = int(anumber[2]) if len(anumber) > 2 else -1
        self.fourth = int(anumber[3]) if len(anumber) > 3 else -1

    def __str__(self):
        return self.digits



class Numbers:
    
    def __init__(self, numbers_list):
        self.list = [Number(x) for x in numbers_list]

    def remove(self, n):
        number = next((x for x in self.list if x.digits == n), None)
        self.list.pop(number)

    def first_digits(self):
        return sorted([x.first for x in self.list], reverse=True)

    def second_digits(self):
        return sorted([x.second for x in self.list], reverse=True)

    def third_digits(self):
        return sorted([x.third for x in self.list], reverse=True)

    def fourth_digits(self):
        return sorted([x.fourth for x in self.list], reverse=True)


def largest_number(a):
    biggest_number = []
    numbers = Numbers(a)
    
    while len(numbers.list) > 0:
        for nominee in numbers.list:
            for number in numbers.list:
                if biggerThan(nominee, number):
                    biggest_number.append(nominee.digits)
                    numbers.remove(nominee.digits)




    res = ""
    for x in a:
        res += x
    return res



def biggerThan(n1, n2):
    if n1.first > n2.first:
        return True
    
    if n1.first == n2.first and n1.second > n2.second:
        return True

    if n1.first == n2.first and n1.second == n2.second and n1.third > n2.third:
        return True

    if n1.first == n2.first and n1.second == n2.second and n1.third == n2.third and n1.fourth > n2.fourth:
        return True

    return False



if __name__ == '__main__':
    #input = sys.stdin.read()
    input = '3 2 31 3'
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
