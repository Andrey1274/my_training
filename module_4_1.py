from fake_math import divide as f_d #=> импортируется функция (divide) из модуля (fake_math)
from true_math import divide as t_d #=> импортируется функция (divide) из модуля (true_math)
result1 = f_d(69, 3) #=> в переменную (result1) записывается возвращаемый результат работы модуля (fake_math)
result2 = f_d(3, 0) #=> в переменную (result2) записывается возвращаемый результат работы модуля (fake_math)
result3 = t_d(49, 7) #=> в переменную (result3) записывается возвращаемый результат работы модуля (true_math)
result4 = t_d(15, 0) #=> в переменную (result4) записывается возвращаемый результат работы модуля (true_math)
print(result1) #=> выводим результат 1 на консоль
print(result2)
print(result3)
print(result4)