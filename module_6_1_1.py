class Animal(): #=> создаем родительский класс Animal (животные)
    alive = True #=> создаем атрибут класса Animal (alive - живой)
    fed = False #=> создаем атрибут класса Animal (fed - накормленный)


    def __init__(self, name): #=> создаем метод __init__ для определения имени каждого животного (объекта)
        self.name = name #=> передаем атрибут (имя) объекта внутри метода __init__


    def eat(self, food): #=> создаем метод eat (кушать) с атрибутом этого метода food (еда)
        if food.edible: #=> условие, если еда съедобная (edible)
            print(f'{self.name}, съел {food.name}') #=> вывод на консоль
            self.fed = True #=> накормленный - да. Здесь переопределяется значение атрибута fed класса Animal
        else:
            print(f'{self.name}, не стал есть {food.name}') #=> вывод на консоль
            self.alive = False #=> живой - нет. Здесь переопределяется значение атрибута alive класса Animal


class Plant(): #=> создаем родительский класс Plant (растения)
    edible = False #=> создаем атрибут класса Plant (edible - съедобный)

    def __init__(self, name): #=> определяем метод (с созданием объекта) __init__ внутри класса Plant
        self.name = name #=> передаем атрибут (имя) объекта внутри метода __init__


class Mammal(Animal): #=> создаем дочерний класс Mammal (млекопитающее)
    pass

class Predator(Animal): #=> создаем дочерний класс Predator (хищник)
    pass

class Flower(Plant): #=> создаем дочерний класс Flower (цветок)
    pass


class Fruit(Plant): #=> создаем дочерний класс Fruit (фрукты)
    edible = True #=> переопределяем атрибут класса Fruit (edible - съедобный)

    def __init__(self, name): #=> определяем метод (с созданием объекта) __init__ внутри класса Fruit
        super().__init__(name) #=> вызываем встроенную функцию super, которая позволяет вызывать методы родительского класса (Plant) в дочернем классе

# Код для проверки работы классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось