
def is_prime(func): #=> объявляем функцию-декоратор, которая на вход принимает функцию sum_three

    def wrapper(*args, **kwargs): #=> объявляем вложенную функцию
        sum_ = func(*args, **kwargs) #=> вводим переменную sum_

# Делаем проверку на тип числа (Простое или Составное):
        is_prime = True
        for i in range(2, sum_):
            if sum_ % i == 0:
                is_prime = False
        if is_prime == True:
            return (f'Простое число\n{sum_}') #=> возвращаем результат проверки типа числа
        else:
            return (f'Составное число\n{sum_}')
    return wrapper #=> возвращаем функцию


@ is_prime #=> объявляем декоратор is_prime для функции sum_three
def sum_three(*value): #=> объявляем функцию, которая будет складывать числа
    sum_ = sum(value) #=> вводим переменную sum_, которая принимает значение суммы переданных чисел с помощью встроенной функции sum
    return sum_ #=> возвращаем переменную sum_

result = sum_three(2, 3, 6)
print(result)