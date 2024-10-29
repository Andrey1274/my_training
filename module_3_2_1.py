def send_email(message, recipient, *, sender = "university.help@gmail.com"): #=> объявляем функцию send_email с двумя позиционными параметрами (message и recipient) и одним именованным параметром (sender)
    if "@" not in recipient or "@" not in sender or not recipient.endswith((".com", ".ru", ".net")) or not sender.endswith((".com", ".ru", ".net")): #=> проверка условия наличия обязательных символов в строковых параметрах
        print(f'Ваше сообщение: {message}')
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}") #=> вывод на консоль
        print('')
    elif recipient == sender: #=> проверка условия на совпадение строковых параметров
        print(f'Ваше сообщение: {message}')
        print("Нельзя отправить письмо самому себе!") #=> вывод на консоль
        print('')
    elif sender == "university.help@gmail.com": #=> проверка условия наличия строкового параметра, который был задан по умолчанию
        print(f'Ваше сообщение: {message}')
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}") #=> вывод на консоль
        print('')
    else: #=> иначе
        print(f'Ваше сообщение: {message}')
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}") #=> вывод на консоль
        print('')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com') #=> запуск функции send_email с двумя позиционными (обычными) параметрами
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com') #=> запуск функции send_email с двумя позиционными (обычными) параметрами и измененным именованным параметром (sender)
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk') #=> запуск функции send_email с двумя позиционными (обычными) параметрами и измененным именованным параметром (sender)
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru') #=> запуск функции send_email с двумя позиционными (обычными) параметрами и измененным именованным параметром (sender)