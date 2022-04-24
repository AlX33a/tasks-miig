import calendar
import datetime
import time


def func1(date):
    def date_ok(date_try):
        try:
            time.strptime(date_try, '%d.%m.%Y')
            return True
        except ValueError:
            return False

    if date_ok(date):
        return date
    else:
        date = date.split('.')
        if int(date[1]) > 12:
            return func1(date[0] + '.12.' + date[2])
        return func1(str(int(date[0]) - 1) + '.' + str(int(date[1])) + '.' + date[2])


def func2(text):
    possible_data = {'послезавтра': 2, 'позавчера': -2, 'сегодня': 0, 'завтра': 1, 'вчера': -1}
    today_date = str(datetime.datetime.now())[:-16].split('-')

    for i in possible_data:
        if i in text:
            modified_date = f'{int(today_date[-1]) + possible_data[i]}.{int(today_date[-2])}.{int(today_date[-3])}'
            return text.replace(i, modified_date)


def func3(text):
    day_s = {'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3, 'пятница': 4, 'суббота': 5, 'воскресенье': 6}
    for i in day_s:
        if i in text:
            day = day_s[i]
    data = list(map(int, str(datetime.datetime.now())[:-16].split('-')))

    if 'прошлый' in text or 'прошлая' in text or 'прошлое' in text:
        if data[2] != calendar.monthrange(data[0], data[1])[0]:
            data[2] -= 1
        else:
            if data[1] != 1:
                data[1] -= 1
                data[2] = calendar.monthrange(data[0], data[1])[-1]
            else:
                data[0] -= 1
                data[1] = 12
                data[2] = calendar.monthrange(data[0], data[1])[-1]

        while calendar.weekday(data[0], data[1], data[2]) != day:
            if data[2] != calendar.monthrange(data[0], data[1])[-1]:
                data[2] -= 1
            else:
                data[1] -= 1
                data[2] = calendar.monthrange(data[0], data[1])[-1]
        return f'{data[-1]}.{data[-2]}.{data[-3]}'

    if 'следующий' in text or 'следующая' in text or 'следующее' in text:
        if data[2] != calendar.monthrange(data[0], data[1])[-1]:
            data[2] += 1
        else:
            if data[1] < 12:
                data[1] += 1
                data[2] = 1
            else:
                data[0] += 1
                data[1] = 1
                data[2] = 1

        while calendar.weekday(data[0], data[1], data[2]) != day:
            if data[2] != calendar.monthrange(data[0], data[1])[-1]:
                data[2] += 1
            else:
                data[1] += 1
                data[2] = 1
        return f'{data[-1]}.{data[-2]}.{data[-3]}'
    return f'{data[-1]}.{data[-2]}.{data[-3]}'


print(func1("32.15.2019"))
print(func2("позавчера наступит, а 2010 уже не вернется"))
print(func3("следующий воскресенье"))
