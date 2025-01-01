
# Импортируем необходимые модули
import threading
import time
from random import randint
# Cоздаём класс Bank со следующими свойствами:
# Атрибуты объекта: balance - баланс банка (int); lock - объект класса Lock для блокировки потоков
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    # Методы объекта в классе Bank:
    # Метод deposit будет совершать 100 транзакций пополнения средств
    def deposit(self):
        for i in range(100): #=> открываем цикл на 100 транзакций пополнения средств
            replenishment_balance = randint(50, 500) # инициализация случайного целого число от 50 до 500.
            with self.lock:
                if self.balance <= 500 and self.lock.locked(): #=> если баланс меньше или равен 500
                                                              # и замок lock заблокирован - lock.locked(), то разблокировать его
                    self.balance += replenishment_balance #=> операция по пополнению баланса
                    print(f'Пополнение: {replenishment_balance}. Баланс: {self.balance}\n') #=> вывод сообщения о пополнении баланса
            time.sleep(0.001) #=> ставим задержку по времени на 0,001 секунды

    # Метод take будет совершать 100 транзакций снятия средств
    def take(self):
        for i in range(100): #=> открываем цикл на 100 транзакций снятия средств
            reducing_balance = randint(50, 500) #=> инициализация случайного целого числа от 50 до 500
            print(f'Запрос на {reducing_balance}\n') #=> вывод сообщения о запросе средств с баланса

            with self.lock:
                if reducing_balance <= self.balance: #=> производится проверка:если случайное число меньше или равно текущему балансу
                    self.balance -= reducing_balance #=> производится снятие, уменьшив balance на соответствующее число
                    print(f'Снятие: {reducing_balance}. Баланс: {self.balance}') #=> выводится сообщение о снятии и о текущем балансе
                else:
                    print(f'Запрос отклонен, недостаточно средств')
            time.sleep(0.001) #=> ставим задержку по времени на 0,001 секунды

def main(): #=> объявляем функцию main для запуска потоков
# Создаём объект класса Bank
    bk = Bank()

#Создаём 2 потока для методов класса Bank: deposit и take:
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

#  Запускаем эти потоки.
    th1.start()
    th2.start()
    th1.join()
    th2.join()

# После окончания работы потоков выводится сообщение:
    print(f'Итоговый баланс: {bk.balance}')

if __name__ == '__main__': #=> запускаем конструкцию для проверки условия импортирования данного файла как модуля
    main()