# Задача. Вы хотите определить функцию или метод, где один или
# более аргументов являются необязательными и имеют значение по умолчанию.

# Решение. Определить функцию с необязательными аргументами несложно:
# просто пропишите значения в определении и убедитесь, что аргументы
# по умолчанию идут последними.

# Например:

def spam(a, b=42):
    print(a, b)

spam(1)  # a=1, b=42
spam(1, 5)  # a=1, b=5

# Если значение по умолчанию – это изменяемый (мутабельный) контейнер,
# такой как список, множество или словарь, используйте None в
# качестве значения по умолчанию:

def spam(a, b=None):
    if b is None:
        b = []

# Если вместо предоставления значения по умолчанию вы хотите написать код,
# который просто проверяет, передано ли в необязательном аргументе целевое
# значение, используйте такую идиому:

_no_value = object()

def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')

# Вот как эта функция себя ведет:

spam(1)  # No b value supplied
spam(1, 2)  # b = 2
spam(1, None)  # b = None

# Понаблюдайте за разницей между отсутствием переданного значения
# и передачей значения None.

# Обсуждение
# Определение функций с аргументами по умолчанию – несложное дело, но не без тонкостей.
# Во первых, значения, назначенные значениями по умолчанию, связываются
# только один раз, во время определения функции. Попробуйте поэкспериментировать:

x = 42

def spam(a, b=x):
    print(a, b)

spam(1)
x = 23
spam(1)

# Заметьте, как изменение переменной x (которая была использована в качестве
# значения по умолчанию) не оказывает влияния на последующие события.

# Во вторых, значения, назначенные значениями по умолчанию, всегда должны
# быть неизменяемыми объектами, и такими как None, True, False, числа или строки.

# Никогда не пишите такой код:

def spam(a, b=[]):  # НЕТ!
    pass

# Если вы это сделаете, то столкнетесь со всеми возможными неприятностями,
# если значение по умолчанию когда либо покинет пределы функции и будет изменено.
# Такие изменения навсегда поменяют значение по умолчанию и подействуют на все
# будущие вызовы функции.

# Например:

def spam(a, b=[]):
    print(b)
    return b

x = spam(1)  # []
x.append(99)  # [99]
x.append('Yow!')  # [99, 'Yow!']
spam(1)  # Возвращается измененный список!

# Вероятно, вы хотели не этого. Чтобы избежать таких проблем, лучше назначить
# в качестве значения по умолчанию None и проверить его затем в функции,
# как показано в решении.

# Использование оператора is при проверке None – важнейшая часть этого рецепта.
# Некоторые делают такую ошибку:

def spam(a, b=None):
    if not b:  # НЕТ! Вместо этого используйте 'b is None'
        b = []
        print(b)

# Хотя None выдает значение False, многие другие объекты (например, строки
# нулевой длины, пустые списки, кортежи и словари) ведут себя так же.
# Так что показанная выше проверка будет ошибочно считать некоторые входные
# значения отсутствующими.

# Например:

spam(1)  # ОК
x = []
spam(1, x)  # Невидимая ошибка. Значение x перезаписывается по умолчанию
spam(1, 0)  # Невидимая ошибка. 0 игнорируется
spam(1, '')  # Невидимая ошибка. '' игнорируется

# Последняя часть этого рецепта – это особенно тонкий момент: функция, которая
# выполняет проверку, передано ли значение (любое) в необязательном аргументе.
# Хитрость в том, что вы не можете использовать None, 0 или False в качестве
# значения по умолчанию при проверке присутствия предоставленного пользователем
# аргумента (поскольку все они являются вполне допустимыми аргументами и пользователь
# может передать их в функцию). Так что вам нужно делать провер- ку как то по другому.

# Чтобы решить эту проблему, вы можете создать уникальный частный экземпляр object,
# как показано в решении (переменная _no_value). Затем вы проверяете предоставленный
# аргумент в функции, сравнивая его с этим специальным значением, чтобы узнать,
# передан аргумент или нет. Идея в том, что крайне маловероятно, что пользователь
# передаст в качестве входного значения экземпляр _no_value. Поэтому это безопасное
# значение для проверки того, предоставлен ли экземпляр.

# Использование object() может показаться необычным. object – это класс, который является
# обычным базовым классом (суперклассом) практически всех объектов Python. Вы можете
# создавать экземпляры object, но они не особенно интересны, поскольку не имеют каких то
# полезных методов или атрибутов (в них нет словаря экземпляра, так что вы не можете присвоить
# им атрибуты). В общемто, проверка идентичности – единственная вещь, для которой они полезны.
# Их можно использовать в качестве специальных значений, как и показано в вышеописанном решении.