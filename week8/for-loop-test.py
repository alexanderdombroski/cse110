
basic = True

if basic:
    for data in range(10), ('a', 'b'), "hello world", {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}:
        print()
        for index in data:
            print(index)
else:
    for data in (('a', 'b'), ('b', 'c'), ('d', 'e')), enumerate("hello world"), dict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}).items():
        print()
        print(data)
        for index, value in data:
            print(f'{index} ~ {value}')



'''
List of things you can iterate through

##Basics
Numbers -- range()
Strings
Lists
Dictionary Keys

##Advanced
Lists inside Lists
Tuples inside Lists -- enumerate() or dict().keys()
--For these you must set the same number of local variables in the loop as each list/tuple length
'''