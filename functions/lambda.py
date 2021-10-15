# Задача. Вам нужно предоставить короткую функцию обратного вызова для
# использования в операции типа sort(), но вы не хотите определять отдельную
# однострочную функцию с помощью инструкции def. Вместо этого вам бы
# пригодился способ определить функцию «в строке».

# Решение. Простые функции, которые просто вычисляют результат выражения,
# могут быть заменены инструкцией lambda.

# Например:

add = lambda x, y: x + y


print(add(2, 3))
print(add('hello', 'world'))


# Использование lambda абсолютно равноценно такому примеру:

def add(x, y):
    return x + y


print(add(2, 3))

# Обычно lambda используется в контексте какой то другой операции, такой
# как сортировка или свертка (reduction) данных:

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']

print(sorted(names, key=lambda name: name.split()[-1].lower()))

# Обсуждение
# Хотя lambda позволяет определить простую функцию, ее возможности сильно ограничены.
# В частности, может быть определено только одно выражение, результат которого станет
# возвращаемым значением. Это значит, что никакие другие возможности языка, в т. ч.
# множественные инструкции, условия, итерации и обработка исключений, использоваться не могут.
# Вы можете замечательно писать код на Python без использования lambda. Однако вы наверняка
# натолкнетесь на них в написанной кем то программе, в которой используется множество маленьких
# функций для вычисления результатов выражений, или же в программе, которая требует от пользователей
# предоставлять функции обратного вызова (callback functions).
