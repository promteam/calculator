# -*- coding: utf-8 -*-
def and_or_not():

    hello_msg = 'And Or Not\nДля помощи введите help\n'
    task_msg = 'Введите выражение:'
    answer_msg = '='
    error_msg = 'Неверный формат задания'
    help_message = 'В программе используются выражения вида: true and true\nДля выхода введите \'exit\''

    input_str = None
    answer = None
    splited = None

    print hello_msg
    input_str = raw_input()
    while input_str != 'exit':
        splited = map(lambda x: x.lower(), input_str.split())
        if len(splited) == 1:
            if splited[0].lower() == 'help':
                print help_message
            elif splited[0] == 'true' or splited[0] == 'false':
                print answer_msg, splited[0]
        elif len(splited) == 2:
            if splited[0] == 'not' and (splited[1] == 'true' or splited[1] == 'false'):
                print answer_msg, bool_to_raw(not raw_to_bool(splited[1]))
            else:
                print error_msg
        elif len(splited) == 3:
            if (splited[0] == 'true' or splited[0] == 'false') and (splited[2] == 'true' or splited[2] == 'false'):
                if splited[1] == 'and':
                    print answer_msg, bool_to_raw(raw_to_bool(splited[0]) and raw_to_bool(splited[2]))
                elif splited[1] == 'or':
                    print answer_msg, bool_to_raw(raw_to_bool(splited[0]) or raw_to_bool(splited[2]))
                else:
                    print error_msg
            else:
                print error_msg
        else:
            print error_msg
        input_str = raw_input()


def raw_to_bool(raw):
    if raw == 'true':
        return True
    else:
        return False


def bool_to_raw(boolean):
    if boolean:
        return 'true'
    else:
        return 'false'



