calls = 0

def count_calls():
    global calls
    calls += 1



def string_info(string):
    string = input('Введите строку: ', )
    print(len(string))
    print(string.lower())
    print(string.upper())
    count_calls()



def  is_contains(string, list_to_search):
    string = input('Введите искомую строку: ', )
    string.lower()
    list_ = input('Введите список из которого нужно выделить искомую строку через запятую :', )
    list_.lower()
    list_to_search = list_.split(',')
    print(list_to_search)
    if string in list_to_search:
        print(True)
    else:
        print(False)
    count_calls()


string_info('')
string_info('')
is_contains('',[])

print('Функции : ',calls)