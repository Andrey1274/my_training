def single_root_words(root_word, *other_words): #=> объявляем функцию single_root_words с позиционным параметром (root_word) и параметром (*other_words) с неограниченной последовательностью
    same_words = [] #=> открываем пустой список (same_words)
    root_word_lower = root_word.lower() #=> определяем новый аргумент, в котором все символы параметра (root_word) будут в нижнем регистре

    for word in other_words: #=> объявляем цикл с переменной (word) для перебора всех элементов в последовательности (other_words)
        word_lower = word.lower() #=> определяем новый аргумент, в котором все символы переменной (word) будут в нижнем регистре
        if root_word_lower in word_lower or word_lower in root_word_lower: #=> проверяются условия наличия (совпадения) слов в введённых аргументах при запуске функции (single_root_words)
            same_words.append(word) #=> добавляется переменная (word) к списку (same_words), если выполняется условие выше
    return same_words #=> возвращается список (same_words) в качестве результата работы цикла

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies') #=> определяется новый список по результату работы функции (single_root_words)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel') #=> определяется новый список по результату работы функции (single_root_words)

print(result1) #=> вывод на консоль
print(result2) #=> вывод на консоль