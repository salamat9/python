# Напишите функцию go_for_a_walk(), которая зовет погулять. Она будет
# распечатывать на экран “Давай, пойдем погуляем на улице!” Напишите
# декоратор, который будет принимать параметр temperature (декоратор тройной
# вложенности). Температуру должен вводить пользователь. Добавьте проверку
# на тип получаемых данных от пользователя используя конструкцию try - except.
# Переведите данные в int и прокиньте в декоратор.
# Если температура больше 10 С, то декоратор должен вызвать функцию
# go_for_a_walk и затем распечатать “На улице тепло, давай погуляем, я не
# против!“. Если от 0 до 10 С, то он вызовет функцию и распечатает “Прохладно.
# Надо одеться!“, если от -10 до 0 (не включая 0), то - “Холодно. Потеплее
# оденься и пойдем!“, если меньше -10, то “Мороз. Лучше давай дома посидим,
# фильм посмотрим!”

def first(func):
    def second(temp):
        def third():
            if temp > 10:
                func(temp)
                print('На улице тепло, давай погуляем, я не против!')
            elif 0 <= temp <= 10:
                func(temp)
                print('Прохладно. Надо одеться!')
            elif -10 <= temp < 0:
                func(temp)
                print('Холодно. Потеплее оденься и пойдем!')
            else:
                print('Мороз. Лучше давай дома посидим, фильм посмотрим!')
        return third
    return second


@first
def go_for_a_walk(temp):
    print('Давай, пойдем погуляем на улице!')
    return temp

while True:
    temperature = None

    while type(temperature) != int:
        try:
            temperature = int(input('Type a temperature: '))
        except ValueError:
            print('Type a valid number!')

    go_for_a_walk(temperature)()

# def first(t):
#     def second(func):
#         def third():
#             if t > 10:
#                 func()
#                 print('На улице тепло, давай погуляем, я не против!')
#             elif 0 <= t <= 10:
#                 func()
#                 print('Прохладно. Надо одеться!')
#             elif -10 <= t < 0:
#                 func()
#                 print('Холодно. Потеплее оденься и пойдем!')
#             else:
#                 print('Мороз. Лучше давай дома посидим, фильм посмотрим!')
#         return third
#     return second
#
#
# while True:
#     temperature = None
#
#     while type(temperature) != int:
#         try:
#             temperature = int(input('Type a temperature: '))
#         except ValueError:
#             print('Type a valid number!')
#
#
#     @first(temperature)
#     def go_for_a_walk():
#         print('Давай, пойдем погуляем на улице!')
#
#     go_for_a_walk()

