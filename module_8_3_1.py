# Определяем пользовательское исключение для некорректного VIN номера
class IncorrectVinNumber(Exception): #=> создаем дочерний класс для формирования сообщений об ошибке при некорректом VIN номере
    def __init__(self, message): #=> создаем метод (с созданием объекта) __init__ внутри класса IncorrectVinNumber
        self.message = message  #=> создаем атрибут объекта в классе IncorrectVinNumber (message - сообщение)


# Определяем пользовательское исключение для некорректных номеров автомобиля
class IncorrectCarNumbers(Exception): #=> создаем дочерний класс для формирования сообщений об ощибке при некорректом Car номере
    def __init__(self, message): #=> создаем метод (с созданием объекта) __init__ внутри класса IncorrectCarNumbers
        self.message = message  #=> создаем атрибут объекта в классе IncorrectCarNumbers (message - сообщение)


# Определяем класс Car
class Car: #=> создаем класс Car для проверки сведений об автомобиле
    def __init__(self, model, vin, numbers): #=> создаем метод (с созданием объекта) __init__ внутри класса Car,
                                             # с атрибутами объектов: model, vin, numbers
        self.model = model  #=> создаем атрибут объекта - модель автомобиля (публичный атрибут)
        self.__vin = vin  #=> создаем атрибут объекта - VIN номер автомобиля (приватный атрибут)
        self.__numbers = numbers  #=> оздаем атрибут объекта - номер автомобиля (приватный атрибут)

        # Проверяем корректность VIN номера и номеров при создании объекта
        if not self.__is_valid_vin(self.__vin): #=> проверяем условие соответствия
            raise IncorrectVinNumber('Некорректный тип vin номер')  #=> формируем класс ошибки IncorrectVinNumber, если VIN некорректен

        if not self.__is_valid_numbers(self.__numbers): #=> проверяем условие соответствия
            raise IncorrectCarNumbers(
                'Некорректный тип данных для номеров')  #=> формируем класс ошибки IncorrectCarNumbers, если номера некорректны

    # Приватный метод для проверки корректности VIN номера
    def __is_valid_vin(self, vin_number): #=> создаем метод проверки введенных VIN номеров на соответствие (с атрибутом vin_number)
        if not isinstance(vin_number, int):  #=> проверка на целое число с применением встроенных функций isinstance и int
            raise IncorrectVinNumber('Некорректный тип vin номер')  #=> формируем класс ошибки IncorrectVinNumber, если VIN некорректен

        if vin_number < 1000000 or vin_number > 9999999:  #=> проверка на диапазон значений
            raise IncorrectVinNumber(
                'Неверный диапазон для vin номера')  #=> формируем класс ошибки IncorrectVinNumber, если VIN некорректен

        return True  #=> если проверки пройдены, возвращаем True

    # Приватный метод для проверки корректности номера автомобиля
    def __is_valid_numbers(self, numbers): #=> создаем метод проверки введенных номеров автомобиля на соответствие
                                           # (с атрибутом numbers)
        if not isinstance(numbers, str):  #=> проверка на строку с применением встроенных функций isinstance и str
            raise IncorrectCarNumbers(
                'Некорректный тип данных для номеров')  #=> формируем класс ошибки IncorrectCarNumbers, если номера некорректны

        if len(numbers) != 6:  #=> проверка на длину строки
            raise IncorrectCarNumbers('Неверная длина номера')  #=> формируем класс ошибки IncorrectCarNumbers, если номера некорректны

        return True  #=> Если проверки пройдены, возвращаем True


# Примеры использования классов и обработки исключений
try: #=> открываем блок try для проверки на возможные ошибки
    first = Car('Model1', 1000000, 'f123dj')  #=> создаем объект класса Car с корректными данными
except IncorrectVinNumber as exc: #=> открываем блок except, который будет исполняться
                                  # в случае возникновения ошибки IncorrectVinNumber в блоке try
    print(exc.message)  #=> если возникло исключение IncorrectVinNumber, выводим сообщение об ошибке
except IncorrectCarNumbers as exc: #=> открываем блок except, который будет исполняться
                                   # в случае возникновения ошибки IncorrectCarNumbers в блоке try
    print(exc.message)  #=> если возникло исключение IncorrectCarNumbers, выводим сообщение об ошибке
else:
    print(f'{first.model} успешно создан')  #=> если объект создан успешно, выводим сообщение на консоль

try: #=> открываем блок try для проверки на возможные ошибки
    second = Car('Model2', 300, 'т001тр')  #=> создаем объект класса Car с некорректным VIN номером
except IncorrectVinNumber as exc: #=> открываем блок except, который будет исполняться
                                  # в случае возникновения ошибки IncorrectVinNumber в блоке try
    print(exc.message)  #=> выводим сообщение об ошибке для некорректного VIN номера
except IncorrectCarNumbers as exc: #=> #=> открываем блок except, который будет исполняться
                                   # в случае возникновения ошибки IncorrectCarNumbers в блоке try
    print(exc.message) #=> если возникло исключение IncorrectCarNumbers, выводим сообщение об ошибке
else:
    print(f'{second.model} успешно создан') #=> если объект создан успешно, выводим сообщение на консоль

try: #=>
    third = Car('Model3', 2020202, 'нет номера')  #=> Создаем объект Car с некорректными номерами
except IncorrectVinNumber as exc: #=> открываем блок except, который будет исполняться
                                  # в случае возникновения ошибки IncorrectVinNumber в блоке try
    print(exc.message) #=> выводим сообщение об ошибке для некорректного VIN номера
except IncorrectCarNumbers as exc: #=> открываем блок except, который будет исполняться
                                   # в случае возникновения ошибки IncorrectCarNumbers в блоке try
    print(exc.message) #=> если возникло исключение IncorrectCarNumbers, выводим сообщение об ошибке
else:
    print(f'{third.model} успешно создан') #=> если объект создан успешно, выводим сообщение на консоль