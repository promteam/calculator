#-*- coding: utf-8 -*-

import AndOrNot
import SimpleOperationsMenu
import long_num_add_sub
import string_menu

def main():
    exit = False
    while not exit:
        print 'Главное меню Калькулятора:'
        print '1. Сделать что-то с числами.'
        print '2. Сделать что-то со строками.'
        print '3. Сделать что-то с длинными числами.'
        print '4. Сделать что-то логическое.'
        print '0. Выйти из программы.'
        choice = raw_input('Введите номер выбранного пункта: ')
        while choice not in '01234':
            choice = raw_input('Пожалуйста, введите корректный номер пункта: ')
        print ''
        if choice == '1':
            SimpleOperationsMenu.main()
        elif choice == '2':
            string_menu.main()
        elif choice == '3':
            long_num_add_sub.long_arithmetics()
        elif choice == '4':
            AndOrNot.add_or_not()
        elif choice == '0':
            exit = True


if __name__ == '__main__':
    main()
