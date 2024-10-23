numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] #=> создается пустой список для простых чисел
not_primes = [] #=> создается пустой список для составных чисел
for i in range(len(numbers)): #=> создается цикл для последовательного перебора всех элементов в заданном списке
    if numbers[i] == 1: #=> производится проверка каждлго элемента из заданного списка на значение равным единице
        continue
    for j in range (i): #> создается вложенный цикл для последовательной проверки делимости элементов
        if numbers[j] == 1: #=> производится проверка каждлго элемента из заданного списка на значение равным единице
            continue
        elif numbers[i] % numbers[j] == 0: #=> проверка делимости элементов на цело
            not_primes.append(numbers[i]) #=> при выполнении условия делимости на цело, данный элемент списка считается составным и добавляется в список составных чисел
            break #=> при выполнении условия делимости на цело, прерывается дальнейшая проверка i-го элемента на делимость
    else:
        primes.append(numbers[i]) #=> если не найдено делителей для i-го элемента, следовательно такой элемент будет считаться простым числом и добавляется в список простых чисел
print(primes) #=> выводится на консоль список простых чисел
print(not_primes) #=> выводится на консоль список составных чисел
print('Выполнено')