# Задача. Вы хотите, чтобы функция возвращала несколько значений.

# Решение. Чтобы вернуть несколько значений из функции, просто
# сделайте возвращаемым значением кортеж.
# Например:

def my_func():
    return 1, 2, 3

a, b, c = my_func()
t = my_func()

print(a)
print(b)
print(c)
print(t)

# Обсуждение
# Хотя это выглядит так, будто my_func() возвращает несколько значений,
# на самом деле создается кортеж. Это кажется немного замысловатым,
# но дело в том, что кортеж задается не скобками, а запятыми.
# Например:

a = (1, 2)
print(a)  # (1, 2)

b = 1, 2
print(b)  # (1, 2)

c = 1,
print(c)  # (1,)

# При вызове функций, которые возвращают кортеж, часто результат
# присваивают нескольким переменным. Возвращаемое значение также
# может быть присвоено одной переменной: