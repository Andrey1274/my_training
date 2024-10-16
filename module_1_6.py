my_dict = {'Timofey':2011, 'Kirill':2008, 'Andrey':1974, 'Luda':1973}
print('Dict:', my_dict)
print('Existing value:', my_dict['Andrey'])
my_dict['Igor']=1991
print(my_dict)
my_dict.update({'Sahsa':1993, 'Dima':1997})
print(my_dict)
print(my_dict.get('Alex', 'Такого ключа нет'))
a = my_dict.pop('Andrey')
print('Deleted value:', a)
print('Modifiend dictionary:', my_dict)
my_set = {1, 47.278, 1, 2, 3, 'string', (4,8), 47.278, (4,8),'string'}
print('Set:', my_set)
print(my_set.discard(1))
print(my_set)
print(my_set.add(5))
print(my_set.add(7.3))
print('Modifiend set:', my_set)