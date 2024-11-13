def test_function(): #=> объявляем функцию (test_function)
    def inner_function(): #=> объявляем вложенную функцию (inner_function) внутри функции (test_function)
        print("Я в области видимости функции test_function") #=> команда вывода на консоль значения
        return #=> прерывание функции (inner_function) без возврата какого либо значения
    inner_function() #=> вызов функции (inner_function) внутри функции (test_function)
    return #=> прерывание функции (test_function) без возврата какого либо значения
#inner_function() # <= данная команда по вызову вложенной функции (inner_function) даёт ошибку, что имя вложенной функции не определено
test_function() #=> вызов внешней функции (test_function)