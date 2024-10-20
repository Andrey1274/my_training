from time import sleep
print('Введите последовательно три числа')
sleep(2) #=> Добавление временной паузы 2 секунды
first = float(input('Введите первое чило: ')) #=> вводится вещественное (float) число
second = float(input('Введите второе чило: '))
third = float(input('Введите третье чило: '))
if first == second and first == third:
    print('Количество совпадений: 3')
elif first == second or first == third or second == third: #=> проверка условий с оператором ИЛИ (or)
    print('Количество совпадений: 2')
else:
    print('Количество совпадений: 0')
