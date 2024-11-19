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

    def __len__(self): #=> определяем специальный метод __len__ внутри класса House
        return self.number_of_floors #=> возвращаем значение атрибута number_of_floors (количества этажей)

    def __str__(self): #=> определяем специальный метод __str__ внутри класса House
        return f'Название {self.name}, кол-во этажей: {self.number_of_floors}' #=> возвращаем значение атрибутов (name) и (number_of_floors)

h1 = House('ЖК Эльбрус', 10) #=> задаем объект h1
h2 = House('ЖК Акация', 20) #=> задаем объект h2

#h1.go_to(5) #=> вызываем метод go_to для объекта h1
#h2.go_to(10) #=> вызываем метод go_to для объекта h2

#__str__
print(h1) #=> вывод на консоль значения объекта h1
print(h2) #=> вывод на консоль значения объекта h2

#__len__
print(len(h1)) #=> вывод на консоль результата метода __len__ по объекту h1
print(len(h2)) #=> вывод на консоль результата метода __len__ по объекту h2

# Разные способы вывода на консоль:
print(h1.name,' - ',h1.number_of_floors,'этажей')
print(h2.name,' - ',len(h2),'этажей')
