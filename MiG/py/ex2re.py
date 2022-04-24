def func1(any_tuple, num1, num2):
    empty_tuple = {}
    try:
        serial_num1 = any_tuple.index(num1)
    except ValueError:
        return empty_tuple

    try:
        serial_num2 = any_tuple.index(num2, serial_num1)
    except ValueError:
        return any_tuple[serial_num1:]

    return any_tuple[serial_num1:serial_num2 + 1]


def func2(new_tuple):
    dictionary = {}
    for i in new_tuple:
        if str(i).isdigit():
            dictionary[i] = i ** 2
        else:
            dictionary[i] = 'квадрат'
    return dictionary


tuple0 = (8, 2, 'k', 1, 3, 4, 'jj', 5, ';', 2, 8, 4, 1, 5, 8)
tuple1 = func1(tuple0, 1, 1)
b = func2(tuple1)
print(tuple0)
print(tuple1)
print(b)
