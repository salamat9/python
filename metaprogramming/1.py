# создание обертки для Функции

# Задача. Вы хотите обернуть функцию слоем, добавляющим дополнительную логику
# (например, логирование, профилирование и т. п.).

# Решение. Если вам потребуется обернуть функцию дополнительным кодом, определите
# функцию декоратор.

# Например:

import time
from functools import wraps


def time_this(func):
    """
    Декоратор, который выводит время выполнения.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@time_this
def count_down(n):
    """
    Counts down.
    """
    while n > 0:
        n -= 1

count_down(100_000_000)


# Обсуждение
# Декоратор – это функция, которая принимает функцию на вход и возвращает
# новую функцию на выходе. Когда вы пишете такой код:

@time_this
def count_down(n):
    ...

# это равноценно такой последовательности шагов:

def count_down(n):
    ...

countdown = time_this(count_down)

# Встроенные декораторы @staticmethod, @classmethod и @property работают так же.
# Например, два этих фрагмента эквивалентны:

class A:
    @classmethod
    def method(cls):
        pass


class B:
    # Эквивалентное определение метода класса def method(cls):
    pass

    def method(cls):
        pass

    method = classmethod(method)

# Код внутри декоратора обычно создает новую функцию, которая принимает любые аргументы
# через *args и **kwargs, как в функции wrapper() в этом рецепте. Внутри этой функции вы
# помещаете вызов изначальной входящей функции и возвращаете ее результат. Однако вы также
# добавляете дополнительный код по желанию (например, профилирующий). Созданная функция
# wrapper возвращается в результате и занимает место изначальной функции. Чрезвычайно важно
# подчеркнуть, что декораторы в общем случае не изменяют сигнатуру вызова или возвращаемое
# значение декорируемой функции.

# Использование *args и **kwargs здесь позволяет убедиться, что могут быть приняты любые входные
# аргументы. Возвращаемое значение декоратора практически всегда будет результатом вызова
# func(*args, **kwargs), где func – это изначальная недекорированная функция. При первой встрече
# с декораторами обычно начинают с простых примеров вроде показанного выше. Однако если вы будете
# писать декораторы в реальной работе, то придется помнить о нескольких тонкостях. Например,
# об использовании декоратора @wraps(func) в показанном решении легко забыть, но именно оно
# обеспечивает сохранение метаданных функции (описано в следующем рецепте).