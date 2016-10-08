# -*- coding:utf8 -*-

from math import sqrt


def pow_left_after_division_sqrt():

    print "Для возведения в степень нажмите 1."
    print "Чтобы узнать остаток от деления нажмите 2."
    print "Чтобы узнать корень квадратный от числа, нажмите 3."
    decide = input()
    if decide == 1:
        print "Введите 2 числа"
        a = input()
        b = input()
        print a ** b
    elif decide == 2:
        print "Введите 2 числа"
        a = input()
        b = input()
        print a % b
    elif decide == 3:
        print "Введите 1 число"
        a = input()
        print sqrt(a)

