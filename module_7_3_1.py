import string #=> импортируем модуль string для проведения операций со строками в нашем файле

class WordsFinder: #=> создаем класс (WordsFinder - поисковик слов)
    def __init__(self, *file_names): #=> создаем метод (с созданием объекта) __init__ внутри класса WordsFinder
        self.file_names = file_names #=> определяем атрибут объекта - список имен файлов

    def get_all_words(self): #=> создаем метод get_all_words для который будет возвращать словарь
                             # с ключом в виде имени файла и значением в виде списка слов этого файла
        all_words = {} #=> создаем изначально пустой словарь
        for file_name in self.file_names: #=> открываем цикл для перебора файлов в списке имен файлов
            with open(file_name, 'r', encoding='utf-8') as file: #=> #=> воспользуемся оператором with
                                                                     # для корректного открытия и закрытия файлов.
                                                                     # Здесь открывается файл file_name для чтения
                                                                     # и сохранения информации из него в переменную file
                text = file.read().lower() #=> здесь транслируется информация из переменной file в переменную text
                                           # с применением всроенных методов: (read - чтение) и (lower - в нижнем регистре)

                # Убираем пунктуацию
                text = text.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                #=> с применением встроенных методов: translate, maketrans, replace

                # Разбиваем на слова
                words = text.split() #=> воспользуемся встроенным методом split для представления строки в виде списка слов
                all_words[file_name] = words #=> здесь идёт добавление к ключу словаря (file_name) списка слов (значения)
        return all_words #=> возвращение словаря

    def find(self, word): #=> создаем метод find для который будет возвращать словарь,
                          # где ключ - название файла, значение - первая позиция искомого слова в списке слов этого файла
        results = {} #=> создаем изначально пустой словарь
        all_words = self.get_all_words() #=> запускаем метод get_all_words
        for file_name, words in all_words.items(): #=> открываем цикл для перебора всех ключей и значений словаря
                                                   # с помощью встроенного метода items
            if word.lower() in words: #=> условие, если искомое слово есть в списке слов words
                results[file_name] = words.index(word.lower()) + 1 #=> здесь идёт добавление к ключу словаря (file_name)
                                                                   # номера искомого слова из списка (значения).
                                                                   # Позиция с 1
        return results #=> возвращение словаря

    def count(self, word): #=> создаем метод find для который будет возвращать словарь,
                           # где ключ - название файла, значение - количество раз искомое слово есть в списке слов этого файла
        results = {} #=> создаем изначально пустой словарь
        all_words = self.get_all_words() #=> запускаем метод get_all_words
        for file_name, words in all_words.items(): #=> открываем цикл для перебора всех ключей и значений словаря
                                                   # с помощью встроенного метода items
            count = words.count(word.lower()) #=> запускаем процедуру подсчета, сколько раз искомое слово встречается в файле
            if count > 0: #=> условие
                results[file_name] = count #=> здесь идёт добавление к ключу словаря (file_name) значения count
        return results #=> возвращение словаря

# Запускаем код для проверки
finder2 = WordsFinder('test_file.txt') #=> создаем объект с именем файла test_file.txt
print(finder2.get_all_words()) #=> вывод на консоль результата работы метода get_all_words
print(finder2.find('TEXT')) #=> вывод на консоль результата работы метода find
print(finder2.count('teXT')) #=> вывод на консоль результата работы метода count