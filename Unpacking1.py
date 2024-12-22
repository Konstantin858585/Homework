from typing import AnyStr


def print_params(a = 1, b = 'строка', c = True):


    print(a , b, c)
print_params()

print_params(b = 25)

print_params(c=[1, 2, 3])

def print_params(*args, **kwargs):
    print(values_list)
    print(values_dict)

values_list = [1 , 'строка', False]
values_dict = {'aaa':123, 'bbb':456, 'ccc':789}
print(values_list)
print(values_dict)
print_params(*values_list, **values_dict)


def print_params(*args, **kwargs):
    for key, values in kwargs.items():
        print(key,values)


values_list = [1 , 'строка', False]
values_dict = {'aaa':123, 'bbb':456, 'ccc':789}
values_list_2 = [75.86, 'Hello']
print(values_list)
print(values_dict)
print(values_list_2)
print_params(*values_list, **values_dict)
print_params(*values_list_2,42)