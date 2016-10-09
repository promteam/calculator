# -*- coding:utf8 -*-

from math import sqrt


def pow_leftafterdivision_sqrt():

    print "Для возведения в степень нажмите 1."
    print "Чтобы узнать остаток от деления нажмите 2."
    print "Чтобы узнать корень квадратный от числа, нажмите 3."
    decide = input()
    if decide == 1:
        print "Введите 2 числа через Enter"
        a = input()
        b = input()
        print a ** b
    elif decide == 2:
        print "Введите 2 числа через Enter"
        a = input()
        b = input()
        if (b==0):
            print "Вы что? На ноль же нельзя делить! Введите другое число"
        else:
            print a % b
    elif decide == 3:
        print "Введите 1 число"
        a = input()
        if (a<0):
            print "Введите, пожалуйста, положительное число"
        else: print sqrt(a)
    elif decide > 3:
        print "Введено неверное значение."
        print "Пожалуйста, введите число от 1 до 3"
    elif decide < 1:
        print "Введено неверное значение."
        print "Пожалуйста, введите число от 1 до 3"

def main():
    pow_leftafterdivision_sqrt()

main()

#by DieRK or Dmitry Nikulin