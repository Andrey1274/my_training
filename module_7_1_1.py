class Product: #=> создаем класс (Product - продукты)

    def __init__(self, name:str, weight:float, category:str): #=> создаем метод создания объектов внутри класса Product
                                                              # с атрибутами: name, weight, category
        self.name = str(name) #=> определяем атрибут объекта внутри класса Product (name - название продукта)
        self.weight = float(weight) #=> определяем атрибут объекта внутри класса Product (weight - вес продукта)
        self.category = str(category) #=> определяем атрибут объекта внутри класса Product (category - категория продукта)

    def __str__(self): #=> создаем магический метод __str__ для вывода объектов
        return f'{self.name}, {self.weight}, {self.category}' #=> возврвщает строку в формате: <название>, <вес>, <категория>

class Shop: #=> создаем класс (Shop - магазин)
    __file_name = 'products.txt'  # => создаем инкапсулированный атрибут класса Shop
                                  # и присваиваем ему имя создаваемого текстового файла

    def __init__(self): #=> создаем метод создания объектов внутри класса Shop
        file = open(self.__file_name, 'a')  # => открываем файл для добавления объекта (магазина)
        file.close()  # => закрываем файл с помощью встроенной функции close


    def get_products(self): #=> создаем метод для работы с файлом __file_name
        work_file = open(self.__file_name, 'r') #=> открываем файл __file_name для считывания информации из него
        exist_product = work_file.read() #=> считываем информацию в переменную exist_product с помощью встроенной функции read
        work_file.close() #=> закрываем файл __file_name с помощью встроенной функции close
        return exist_product #=> возвращаем значение переменной exist_product

    def add(self, *products:object): #=> создаем метод для добавления неограниченного количества оъектов класса Product
        ex_product = self.get_products() #=> создаем атрибут метода add и присваиваем ему значение метода get_products

        for product in products: #=> открываем цикл для проверки (списка продуктов - *products), которые хотим добавить
            if product.name in ex_product: #=> условие, если продукт с таким названием уже есть в атрибуте ex_product
                print(f'Продукт {product.name} уже есть в магазине') #=> вывод на консоль сообщения
            else:
                work_file = open(self.__file_name, 'a') #=> иначе, открываем файл __file_name
                                                        # для добавления в него объектов (списка продуктов)
                work_file.write(f'{product}\n') #=> перезаписываем переменную work_file с помощью встроенной функции write
                                                # с добавлением продукта с новой строки
                work_file.close() #=> закрываем файл __file_name с помощью встроенной функции close

# Проверка кода:
s1 = Shop() #=> создаем объект класса (Shop - магазин)
p1 = Product('Potato', 50.5, 'Vegetables') #=> создаем объект класса Product и присваиваем ему значения атрибутов
p2 = Product('Spaghetti', 3.4, 'Groceries') #=> создаем объект класса Product и присваиваем ему значения атрибутов
p3 = Product('Potato', 5.5, 'Vegetables') #=> создаем объект класса Product и присваиваем ему значения атрибутов

print(p2) #=> выводим на консоль сообщение в формате: <название>, <вес>, <категория>

s1.add(p1, p2, p3) #=> вызываем метод добавления неограниченного количества объектов (продуктов в наш магазин)

print(s1.get_products()) #=> выводим на консоль считанную информацию (с помощью метода get_products) о наличии продуктов в магазине