immutable_var = (1,'string',True,[2,3])
print(immutable_var)
immutable_var[3][1] = (immutable_var[3][1])**2 #=> возведение в степень
print(immutable_var)
mutable_list = ['apple','coconut','banana']
print(mutable_list)
mutable_list[1] = 'strawberry'
print(mutable_list)
mutable_list.append(True)
print(mutable_list)
mutable_list.extend('45')
print(mutable_list)
mutable_list.extend([45])
print(mutable_list)
mutable_list.remove('apple')
print(mutable_list)
print('strawberry'in mutable_list) #=> проверяем наличие элемента в списке
print(mutable_list[::2]) #+> выводим только нечетные элементы из списка