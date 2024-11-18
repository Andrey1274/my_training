class House: #=> создаем класс House
    def __init__(self, name, number_of_floors): #=> определяем метод (с созданием объекта) __init__ внутри класса House
        self.name = name #=> передаем атрибут (имя) объекта внутри метода __init__
        self.number_of_floors = number_of_floors #=> передаем атрибут (количество этажей) объекта внутри метода __init__

    def go_to(self, new_floor): #=> определяем метод go_to внутри класса House
        if 1 <= new_floor <= self.number_of_floors: #=> проверяем условие, чтобы параметр new_floor был не меньше 1 и не более number_of_floors
            for i in range(1, new_floor + 1): #=> запуск цикла
                print(i) #=> вывод на консоль номера этажа i
        else: #=> иначе
            print('Такого этажа не существует') #=> вывод на консоль сообщения, если не выполняется условие

h1 = House('ЖК Горский', 18) #=> задаем объект h1
h2 = House('Домик в деревне', 2) #=> задаем объект h2
#h1.go_to(5) #=> вызываем метод go_to для объекта h1
h2.go_to(10) #=> вызываем метод go_to для объекта h2