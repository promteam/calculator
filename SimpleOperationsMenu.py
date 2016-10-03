# -*- coding: utf8 -*-
from random import randint

import math
from math import sqrt

def DecToHex():
    x = input()
    data = []
    i = 0
    while x > 0:
        data.append(x % 16)
        if data[i] ==  10:
            data[i] = 'A'
        elif data[i] == 11:
            data[i] = 'B'
        elif data[i] == 12:
            data[i] = 'C'
        elif data[i] == 13:
            data[i] = 'D'
        elif data[i] == 14:
            data[i] = 'E'
        elif data[i] == 15:
            data[i] = 'F'
        i += 1
        x /= 16
    data.append(x % 16)
    if data[i] == 10:
        data[i] = 'A'
    elif data[i] == 11:
        data[i] = 'B'
    elif data[i] == 12:
        data[i] = 'C'
    elif data[i] == 13:
        data[i] = 'D'
    elif data[i] == 14:
        data[i] = 'E'
    elif data[i] == 15:
        data[i] = 'F'
    data.reverse()
    for i in range(len(data)):
        print data[i],

def DecToBin(x = 1, c=''):
    print "Введите число для перевода"
    a = input()
    if a == 0:
        c = "0"
        return c

    if a % 2 == 0:
        return DecToBin(a // 2, c + "0")
    elif a // 2 < 1:
        c += "1"
        return c
    else:
        return DecToBin(a // 2, c + "1")

def ReverseBin(c):
    arr = list(c)
    arr.reverse()
    print ''.join(arr)

def DecToOct():
    while True:
            try:
                print 'Введите число'
                a = input()
                n = 0
                i = 0
                while a > 0:
                    n = n + (a % 8) * (10 ** i)
                    i += 1
                    a /= 8
                return n
            except StandardError, exc:
                print 'Некорректные данные \nВведите данные еще раз: '

def SimpleOperations():
    print "Введите + - * /, для соответсвующих операций "
    b = raw_input()
    print "Введите два числа "
    a = input()
    c = input()
    if b == "+":
        print a + c
    if b == "-":
        print a - c
    if b == "*":
        print a * c
    if b == "/":
        if c == 0:
            print "Деление на ноль запрещено"
        else:
            print a / c

def SinCosRadians():
    print "Введите угол в радианах "
    a = input()
    c = math.sin(a)
    d = math.cos(a)
    print "Синус = ", c, "Косинус = ", d

def SinCosDeegres():
    print "Введите угол в градусах "
    a = input()
    a = math.degrees(a)
    c = math.sin(a)
    d = math.cos(a)
    print "Синус = ", c, "Косинус = ", d

def PowDivisionSqrt():
    print "Для возведения в степень нажмите 1."
    print "Чтобы узнать остаток от деления нажмите 2."
    print "Чтобы узнать корень квадратный от числа, нажмите 3."
    decide = input()
    if decide == 1:
        print "Введите число и степень"
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


def AndOrNot():
    print 'Выберите операцию and, or или not, для этого введите название соответствующей операции '
    input = raw_input()
    if input == "and":
        print "Введите два числа "
        a, b = input(), input()
        print And(a, b)
    elif input == "or":
        print "Введите два числа "
        a, b = input(), input()
        print Or(a, b)
    elif input == "not":
        print "Введите число "
        a = input()
        print Not(a)
    else:
        print "Операция не найдена "
def ConvertToBool(toConv):
    return ((toConv == 'true') or (toConv == 'True'))

def And(arg1, arg2):
    return (ConvertToBool(arg1) and ConvertToBool(arg2))

def Or(arg1, arg2):
    return (ConvertToBool(arg1) or ConvertToBool(arg2))

def Not(argument):
    return (not ConvertToBool(argument))




def menu_chisel():
    print "Введите 1 для операций + - * /"
    print "Введите 2 для возведения в степень, деления с остатком или взятия корня"
    print "Введите 3 для нахождения sin или cos градусах"
    print "Введите 4 для нахождения sin или cos радианах"
    print "Введите 5 для логических операций and, or или not"
    print "Введите 6 для  перевода числа в двоичную СС"
    print "Введите 7 для  перевода числа в восьмиричную СС"
    print "Введите 8 для  перевода числа в шестнадцатиричную СС"
    a = raw_input()
    if a == "1":
        SimpleOperations()
    if a == "2":
        PowDivisionSqrt()
    if a == "3":
        SinCosDeegres()
    if a == "4":
        SinCosRadians()
    if a == "5":
        AndOrNot()
    if a == "6":
        ReverseBin(DecToBin(8))
    if a == "7":
        DecToOct()
    if a == "8":
        DecToHex()


def main():
    menu_chisel()

main()