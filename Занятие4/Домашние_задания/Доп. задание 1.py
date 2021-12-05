# С помощью регулярных выражений сделать парсер строк и
# проверить корректность следующих выражений:
# 1 + 10 = 11
# 20 - 12 = 8
# 7.5 / 2.5 = 3
# 3 * 0.5 = 1.5
# 0.05 + 6 = 6.05
# Гарантируется что дано два числа (целых или дробных, разделитель дробной части
# «.»  Точка). Доступны четыре арифметических действия +, -, *, /
# Примечание функцией eval пользоваться нельзя :)
import re


if __name__ == '__main__':
    string_ = '1 + 10 = 11,' \
              '20 - 12 = 8,' \
              '7.5 / 2.5 = 3,' \
              '3 * 0.5 = 1.5,' \
              '0.05 + 6 = 6.05'

    number_regex = r'\b(?P<first_number>\d+\.?\d?\d?)\s+(?P<sign>\+|\-|\*|\/)\s+(?P<second_number>\d+\.?\d?\d?)\s+\=\s+(?P<last_number>\d+\.?\d?\d?)'

    pattern = re.compile(number_regex)

    for item in pattern.finditer(string_):
        print(item.groups())
        print(bool(item))
        if (item['sign'] == '+') and (float(item['first_number']) + float(item['second_number']) == float(item['last_number'])):
            print(f'Выражение: {item.group()} - верное')
            print('-' * 10)
        if (item['sign'] == '-') and (float(item['first_number']) - float(item['second_number']) == float(item['last_number'])):
            print(f'Выражение: {item.group()} - верное')
            print('-' * 10)
        if (item['sign'] == '/') and (float(item['first_number']) / float(item['second_number']) == float(item['last_number'])):
            print(f'Выражение: {item.group()} - верное')
            print('-' * 10)
        if (item['sign'] == '*') and (float(item['first_number']) * float(item['second_number']) == float(item['last_number'])):
            print(f'Выражение: {item.group()} - верное')
            print('-' * 10)
