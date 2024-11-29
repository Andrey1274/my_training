class Vehicle(): #=> создаем родительский класс Vehicle (транспортное средство)

    __COLOR_VARIANTS= ['blue', 'red', 'green', 'black', 'white'] #=> открываем список вариантов цветов кузова как атрибут класса Vehicle с двумя нижними подчеркиваниями

    def __init__(self, owner, __model, __color, __engine_power): #=> создаем метод (с созданием объекта) __init__ внутри класса Vehicle
        self.owner = owner #=> создаем атрибут объекта в классе Vehicle (owner - владелец)
        self.__model = __model #=> создаем атрибут объекта в классе Vehicle (__model - модель авто) с двумя нижними подчеркиваниями
        self.__color = __color #=> создаем атрибут объекта в классе Vehicle (__color - цвет кузова авто) с двумя нижними подчеркиваниями
        self.__engine_power = __engine_power #=> создаем атрибут объекта в классе Vehicle (__engine_power - мощность двигателя) с двумя нижними подчеркиваниями

    def get_model(self): #=> создаем метод get_model (модели)
        print(f'Модель: {self.__model}')

    def get_horsepower(self): #=> создаем метод get_horsepower (мощность двигателя)
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self): #=> создаем метод get_color (цвет кузова)
        print(f'Цвет: {self.__color}')

    def print_info(self): #=> создаем метод print_info (выввод данных)
        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print(f'Владелец: {self.owner}') #=> вывод на косоль данных о владельце

    def set_color(self, new_color): #=> создаем метод set_color (выбор цвета)
        if new_color.lower() in self.__COLOR_VARIANTS: #=> если новый цвет есть в вариантах цвета авто
            self.__color = new_color #= присваиваем атрибуту цвета новое значение, переопределяем цвет
        else:
            print(f'Нельзя поменять цвет на {new_color}')


class Sedan(Vehicle): #=> создаем дочерний класс Sedan (седан)

    __PASSENGERS_LIMIT = 5 #=> определяем атрибут класса Sedan (число пассажирских мест равно 5) с двумя нижними подчеркиваниями

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500) #=> создаем объект класса Sedan

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink') #=> вызываем метод замены цвета кузова set_color
vehicle1.set_color('BLACK') #=> вызываем метод замены цвета кузова set_color
vehicle1.owner = 'Vasyok' #=> переопределяем значение атрибута owner

# Проверяем что поменялось
vehicle1.print_info() #=> вызываем метод вывода данных print_info