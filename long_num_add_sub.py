# -*- coding:utf-8 -*-
def long_num_add_sub():
    a = []
    b = []
    sign = None
    sum = []

    correct = False
    digits = [str(j) for j in range(10)]

    while correct == False:
        correct = True
        raw = raw_input('Введxите выражение (a±b):')
        if raw.count('+') == 1:
            a, b = raw.split('+')
            sign = '+'
        elif raw.count('-') == 1:
            a, b = raw.split('-')
            sign = '-'
        else:
            correct = False
            a = b = raw
        a = a.strip(' ')
        b = b.strip(' ')
        for i in a:
            if i not in digits:
                correct = False
        for i in b:
            if i not in digits:
                correct = False
    a = a.rjust(max(map(len, [a, b])), '0')
    b = b.rjust(max(map(len, [a, b])), '0')
    a = list(map(int, a))[::-1]
    b = list(map(int, b))[::-1]
    # NOW REVERSED!!!
    flag = 0
    for i in range(len(a)):
        c = a[i]
        if sign == '+':
            c += b[i] + flag
            sum.append(c % 10)
            flag = c / 10

        elif sign == '-':
            c -= b[i]
            c += flag
            sum.append((c + 10) % 10)
            if c < 0:
                flag = -1
            else:
                flag = 0
    if flag > 0:
        sum.append(flag)
    sum.reverse()
    is_zero = True
    while is_zero == True and len(sum) > 1:
        if sum[0] == 0:
            sum = sum[1:]
        else:
            is_zero = False
    result = ''.join(map(str, sum))
    print(result)
    return result
