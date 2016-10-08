# -*- coding: utf8 -*-
from random import randint

import math
from math import sqrt

def DecToHex():
    x = input()
    if x == 0:
        print 0
        return 0
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
                return  n
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


def and_or_not():
    hello_msg = 'And Or Not\nДля помощи введите help\n'
    task_msg = 'Введите выражение:'
    answer_msg = '='
    format_error_msg = 'Неверный формат задания'
    arg_andornot_error_msg = 'Используемые операторы: and, or, not'
    arg_truefalse_error_msg = 'Используемые операнды: true, false'
    help_message = ''
    err_code = 0
    answer = None
    # 0 - no errors
    # 1 - format error
    # 2 - arg andornot error
    # 3 - arg truefalse error
    # 4 - exit
    # 5 - help
    print hello_msg
    while err_code != 4:
        print task_msg
        args = raw_input().split()
        if err_code == 1:
            print format_error_msg
            err_code = 0
        if err_code == 2:
            print arg_andornot_error_msg
            err_code = 0
        if err_code == 3:
            print arg_truefalse_error_msg
            err_code = 0
        if err_code == 5:
            print help_message
            err_code = 0
        if len(args) == 2:
            if args[0].lower() == 'not':
                args[1], err_code = convert_to_bool(args[1])
                answer = not args[1]
            else:
                err_code = 2
        elif len(args) == 3:
            args[0], er1 = convert_to_bool(args[0])
            args[2], er2 = convert_to_bool(args[2])
            if er1 != 0 or er2 != 0:
                err_code = 3
            if args[1].lower() == 'and':
                answer = args[0] and args[2]
            elif args[1].lower() == 'or':
                answer = args[0] or args[2]
            else:
                err_code = 2
        elif len(args) == 1:
            if args[0].lower() == 'exit':
                err_code = 4
            if args[0].lower() == 'help':
                err_code = 5
        else:
            err_code = 1

        if err_code == 0:
            print answer_msg,
            if answer:
                print 'True'
            else:
                print 'False'
        print ''


def convert_to_bool(input_str):
    if (input_str.lower() == 'true') or (input_str == '1') :
        return True, 0
    elif (input_str.lower() == 'false') or (input_str == '0'):
        return False, 0
    else:
        return False, 3


def convert_to_answer(input_bool):
    if input_bool:
        return 'True'
    else:
        return 'False'
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
        print DecToOct()
    if a == "8":
        DecToHex()


def main():
    menu_chisel()

    
if __name__ == '__main__':
    main()
