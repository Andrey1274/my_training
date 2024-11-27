# Импортирование библиотек:
import hashlib #=> импортирование модуля для создания хэша
import time #=> импортирование модуля времени

# Создание классов:
class User: #=> создаем класс пользователя User
    def __init__(self, nickname, password, age): #=> определяем атрибуты объектов класса User
        self.nickname = nickname #=> имя пользователя
        self.password = hashlib.sha256(password.encode()).hexdigest()  #=> пароль в хэшированном виде
        self.age = age #=> возраст пользователя

class Video: #=> создаем класс Video
    def __init__(self, title, duration, adult_mode=False): #=> определяем атрибуты объектов класса Video
        self.title = title #=> название объекта Video
        self.duration = duration  #=> продолжительность объекта Video, в секундах
        self.time_now = 0  #=> текущая секунда воспроизведения
        self.adult_mode = adult_mode  #=> ограничение по возрасту

class UrTube: #=> создаем класс списков пользователей UrTube
    def __init__(self): #=> определяем атрибуты объектов класса UrTube
        self.users = []  #=> объявляем список пользователей
        self.videos = []  #=> объявляем список видео
        self.current_user = None  #=> объявляем переменную с текущим пользователем

    def log_in(self, nickname, password): #=> создаем метод log_in для проверки введенного логина и пароля
        hashed_password = hashlib.sha256(password.encode()).hexdigest() #=> здесь переменной hashed_password присваивается введенный пароль
        for user in self.users: #=> открывается цикл для проверки списка пользователей
            if user.nickname == nickname and user.password == hashed_password: #=> проверяется условие совпадения имени и пароля пользователя
                self.current_user = user #=> при выполнении условия переменной current_user присваивается введенное имя пользователя и пароль
                return
        print("Пользователь не найден или пароль неверный.") #=>

    def register(self, nickname, password, age): #=> создаем метод register для добавления пользователя в список
        for user in self.users: #=> открывается цикл для проверки списка пользователей
            if user.nickname == nickname: #=> проверяется условие совпадения существующих имен в списке пользователей с введенным логином
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age) #=> вводится новая переменная new_user и к ней добавляется пользователь с логином, паролем и возрастом
        self.users.append(new_user) #=> добавляется новый пользователь в список пользователей
        self.current_user = new_user  #=> вход после регистрации

    def log_out(self): #=> создаем метод log_out для сброса текущего пользователя на None
        self.current_user = None

    def add(self, *videos): #=> создаем метод добавления неограниченного количества Video объектов
        for video in videos: #=> объявляем цикл для проверки наличия объектов video в списке видео
            if not any(v.title == video.title for v in self.videos): #=> проверка условия совпадения только заголовка видео
                self.videos.append(video) #=> в список видео добавляется Video объект

    def get_videos(self, keyword): #=>
        return [video.title for video in self.videos if keyword.lower() in video.title.lower()] #=> возвращает название видео, если введенное слово совпадает с названием видео (без учета регистра букв)

    def watch_video(self, title): #=> создаем метод для просмотра видео
        if not self.current_user: #=> проверка наличия зарегистрированного пользователя
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos: #=> открываем цикл для проверки видео в списке на следующие условия:
            if video.title == title: #=> проверяется условие совпадения названия видео
                if video.adult_mode and self.current_user.age < 18: #=> проверяется условие наличия ограничения по возрасту
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                while video.time_now < video.duration: #=> открывается имитация показа видео
                    print(f"Смотрим {video.title}: {video.time_now} сек.") #=>
                    time.sleep(1)  #=> Пауза в 1 секунду для имитации просмотра
                    video.time_now += 1 #=>
                print("Конец видео")
                video.time_now = 0  #=> сбросить текущее время просмотра
                return

        print("Видео не найдено.")


# Код для проверки работы классов
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))  #=> ['Лучший язык программирования 2024 года']
print(ur.get_videos('ПРОГ'))  #=> ['Лучший язык программирования 2024 года']

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')  #=> "Войдите в аккаунт..."
ur.register('vasya_pupkin', 'lolkekcheburek', 13)  #=> Регистрация пользователя
ur.watch_video('Для чего девушкам парень программист?')  #=> "Вам нет 18 лет..."
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)  #=> Регистрация пользователя с доступом к видео
ur.watch_video('Для чего девушкам парень программист?')  #=> Просмотр видео

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)  #=> Попытка зарегистрироваться с существующим никнеймом
print(ur.current_user.nickname)  #=> 'urban_pythonist'

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')  #=> "Видео с таким названием не найдено."