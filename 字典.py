empty_dict = {}
dict1 = {'a': 1, 'b': 4, 'c': 5, 'd': ['a', 'b', 'c']}

heros = {'及时雨': '宋江', '玉麒麟': '卢俊义', '花和尚': '鲁达'}
# heros['豹子头'] = '林冲'
# print(heros)
# heros['及时雨'] = '宋公明'
# print(heros)
# new_dict = {'花和尚': '鲁智深', '入云龙': '公孙胜'}
# heros.update(new_dict)
# print(heros)

# heros = {'及时雨': '宋江', '玉麒麟': '卢俊义', '花和尚': '鲁达'}
# print(heros)
# del heros['及时雨']
# print(heros)
# del heros
# heros.pop('及时雨')
# print(heros)
# heros.popitem()
# print(heros)
# heros.clear()
# print(heros)

# list_1 = [1, 2, 3, 4, '5', 6, 7, 8, '5', 6, 7, 8, 9, 10]
# print(list_1)
# del list_1[5]
# print(list_1)
# list_1.pop()
# print(list_1)
# list_1.remove('5')
# print(list_1)

# heros = {'及时雨': '宋江', '玉麒麟': '卢俊义', '花和尚': '鲁达'}
# print(heros)
# if '及雨' in heros:
#     print('Yes')
# else:
#     print('No')

# heros = {'及时雨': '宋江', '玉麒麟': '卢俊义', '花和尚': '鲁达'}
# list1 = list(heros.keys())
# print(list1)
# list2 = list(heros.values())
# print(list2)
# list3 = list(heros.items())
# print(list3)
# key, value = list3[1]



# print(key, value, sep='+')

# heros = {'及时雨': '宋江', '玉麒麟': '卢俊义', '花和尚': '鲁达'}





# print(heros)
# new_heros = heros.copy()
# print(new_heros)

heros = {'及时雨': '宋江', '玉麒麟': '卢俊义', '花和尚': '鲁达'}
print(heros)
for key in heros.keys():
    print(key)
for value in heros.values():
    print(value)
for item in heros.items():
    print(item)
for key, value in heros.items():
    print(f'{key}->{value}')
