#-*- coding: utf-8 -*-
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


if __name__ == '__main__':
    and_or_not()
