# -*- coding:utf8 -*-



def count_of_words(a):
    return len(a.split())



def do_strings(typ, str1, str2):
    if typ == '+':
        return str1 + str2
    else:
        return str1 * str2


def menu_string_calc():

    print """\nЧто надо сделать со строками?

    1 - сложить
    2 - умножить на число
    3 - посчитать кол-во слов"""

    choice = input()

    if choice == 1:
        first = raw_input('Введите первую строку\n')
        second = raw_input('Введите вторую строку\n')

        print do_strings('+', first, second)


    elif choice == 2:
        first = raw_input('Введите строку\n')
        second = input('Введите число\n')

        print do_strings('*', first, second)

    elif choice == 3:
        first = raw_input('Введите строку\n')
        print count_of_words(first)

    else:
        print 'Попробуйте снова'




def main():
    menu_string_calc()

if __name__ == '__main__':
    main()
