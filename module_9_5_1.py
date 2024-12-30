# Создаём пользовательский класс исключения StepValueError, который наследуется от ValueError.
# Наследования достаточно, класс оставляем пустым при помощи оператора pass
class StepValueError(ValueError):
    pass

# Создаём класс Iterator.
class Iterator():

# Атрибуты объекта в данном классе:
# start - целое число с которого начинается итерация
# stop - целое число на котором заканчивается итерация
# step - шаг с которым совершается итерация
# pointer - указывает на текущее число в итерации (изначально start)

# Определяем метод (с созданием объекта) __init__ (self, start, stop, step=1) внутри класса Iterator с атрибутами: start, stop, step
# А также в этом методе проверяется значение атрибута step на возможное равенство нулю
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0') #=> перехватываем возможную ошибку при вводе данных
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

# Определяем магический метод __iter__ сбрасывающий значение pointer на start и возвращающий сам объект итератора
    def __iter__(self):
        self.pointer = self.start
        return self #=> возращает сам объект итератора

# _Определяем магический метод __next__ увеличивающий значение атрибута pointer на значение step
    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop): #=> проверка условия
                                                                                                         # прекращения итерации
            raise StopIteration #=> инициализируем прекращение итерации при выполнении условия выше
        current = self.pointer #=> вводим переменную current и присваиваем ей текущее значение pointer
        self.pointer += self.step #=> увеличиваем значение pointer на величину шага (step)
        return current #=> возвращаем значение переменной current


try:
    iter1 = Iterator(100, 200, 0) #=> задаём объект класса Iterator
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print("Шаг указан неверно")

# Вводимые значения
iter2 = Iterator(-5, 1) #=> задаём объект класса Iterator
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

# Вывод результатов итераций на консоль:
for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()