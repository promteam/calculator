def long_multiply(a, b):
    a.reverse()
    b.reverse()
    c = [0] * (len(a) + len(b) + 1)
    for i in range(len(a)):
        for j in range(len(b)):
            multiply = a[i] * b[j]
            c[i + j] += multiply % 10
            c[i + j + 1] += multiply // 10
    for i in range(len(c) - 1):
        c[i + 1] += c[i] // 10
        c[i] %= 10
    while len(c) > 1 and c[len(c) - 1] == 0:
        c.pop()
    c.reverse()
    print ''.join([str(i) for i in c])


def long_num_add_sub(a, b, f):
    Ans = []
    _less = True
    if not(f):
        if (len(a) > len(b)):
            _less = False
        elif len(a) == len(b):
            for i in range(len(a)):
                if a[i] > b[i]:
                    _less = False
                    break
            _less = False
    a.reverse()
    b.reverse()
    a += [0] * max(len(b) - len(a), 0)
    b += [0] * max(len(a) - len(b), 0)
    sign = True
    if _less:
        sign = False
        a, b = b, a
    if f:
        Ans = [0] * max(len(a), len(b))
        for i in range(len(a)):
            Ans[i] += a[i]
        for i in range(len(b)):
            Ans[i] += b[i]
        for i in range(len(Ans) - 1):
            Ans[i + 1] += Ans[i] // 10
            Ans[i] %= 10
        while Ans[len(Ans) - 1] > 10:
            Ans.append(Ans[len(Ans) - 1] // 10)
            Ans[len(Ans) - 1] %= 10
        Ans.reverse()
    else:
        for i in range(len(b)):
            Ans.append(a[i] - b[i])
        for i in range(len(b) + 1, len(a)):
            Ans.append(a[i])
        for i in range(len(Ans) - 1):
            while Ans[i] < 0:
                Ans[i] += 10
                Ans[i + 1] -= 1
        while len(Ans) > 1 and Ans[len(Ans) - 1] == 0:
            Ans.pop()
        if not(sign):
            Ans.append('-')
        Ans.reverse()
    print ''.join(map(str, Ans))


def long_arithmetics():
    while True:
        print "Доступные пункты меню:"
        print "Введите 1 для сложения или вычитания длинных чисел."
        print "Введите 2 для умножения длинных чисел."
        f = raw_input()
        if not(f.isdigit()):
            print "Неверный формат ввода!\n"
            continue
        f = int(f)
        if f != 1 and f != 2:
            print "Неверный формат ввода!\n"
            continue

        if f == 1:
            while True:
                print "Введите два неотрицательных числа в формате: [число] (+/-) [число]"
                A = map(str, raw_input().split())
                if len(A) != 3 or not (A[0].isdigit()) or A[1] != '+' and A[1] != '-' or not(A[2].isdigit()) or not(A[2][0].isdigit()) or not(A[0][0].isdigit()):
                    print "Неверный формат ввода!\n"
                    continue
                a = []
                b = []
                for i in range(len(A[0])):
                    a.append(int(A[0][i]))
                for i in range(len(A[2])):
                    b.append(int(A[2][i]))
                long_num_add_sub(a, b, A[1] == '+')
                return
        elif f == 2:
            while True:
                print "Введите два неотрицательных числа в формате: [число] * [число]"
                A = map(str, raw_input().split())
                if len(A) != 3 or not(A[0].isdigit()) or A[1] != '*' or not(A[2].isdigit()) or not(A[2][0].isdigit()) or not(A[0][0].isdigit()):
                    print "Неверный формат ввода!\n"
                    continue
                a = []
                b = []
                for i in range(len(A[0])):
                    a.append(int(A[0][i]))
                for i in range(len(A[2])):
                    b.append(int(A[2][i]))
                long_multiply(a, b)
                return
        return
