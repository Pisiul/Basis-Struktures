
#                                              БАЗОВЫЕ СТРУКТУРЫ ДАННЫХ

# ****************************************** ДОМАШНЕЕ ЗАДАНИЕ 05.10.2024.*********************************************

#                             ------------- Задача №1 (просто) "Арифметика" --------------
"1st program"
# Задача:
# 1. Напишите в начале программы однострочный комментарий: "1st program".
# 2. Выведите на экран(в консоль) результат: возведение числа 9 в степень 0.5, после умножение на 5.
# 3. Предполагаемый результат: 15.0

# Ответ:
print(9 ** 0.5 * 5) # - возводим число в степень и  умножеам его.
#-----------------------------------------------------------------------------------------------------------------------
# D:\Программы\ProjectPyton\BasiesStructures\Scripts\python.exe D:\Программы\ProjectPyton\BasiesStructures\homework.py
15.0
# Process finished with exit code 0
# ----------------------------------------------------------------------------------------------------------------------

#                               ------------- Задача №2 (просто) "Логика" -------------
"2nd program"
# Задача:
# 1. Напишите в начале программы однострочный комментарий: "2nd program".
# 2. Убедитесь в том что 9.99 больше 9.98 и 1000 не равно 1000.1 одновременно, выведете результат на экран(в консоль)
# 3. Предполагаемый результат: True

# Ответ №1:
print(9.99 > 9.98, 1000 != 1000.1) # - с помощью знаков ( < > ) и ( ! = ) какое число больше и  что числа не равны.
#-----------------------------------------------------------------------------------------------------------------------
# D:\Программы\ProjectPyton\BasiesStructures\Scripts\python.exe D:\Программы\ProjectPyton\BasiesStructures\homework.py
# True True
# Process finished with exit code 0
# ----------------------------------------------------------------------------------------------------------------------

# Ответ №2:
print(9.99 > 9.98 and 1000 != 1000.1) # - с помощью строгого оператора ( and ) проверяем верность выражения.
#-----------------------------------------------------------------------------------------------------------------------
# D:\Программы\ProjectPyton\BasiesStructures\Scripts\python.exe D:\Программы\ProjectPyton\BasiesStructures\homework.py
# True True
# True
# Process finished with exit code 0
#-----------------------------------------------------------------------------------------------------------------------

# Ответ №3:
print(9.99 > 9.98 or 1000 != 1000.1) # - не строгогий оператор ( or ) позволяет быть верным даже если верно только одно.
#-----------------------------------------------------------------------------------------------------------------------
# D:\Программы\ProjectPyton\BasiesStructures\Scripts\python.exe D:\Программы\ProjectPyton\BasiesStructures\homework.py
# True True
# True
# True
# Process finished with exit code 0
# ----------------------------------------------------------------------------------------------------------------------

#                          ------------ Задача №3 (средне) "Школьная загадка" -------------
"3rd program"
# Задача:
# 1. Напишите в начале программы однострочный комментарий: "3rd program".
# 2. Выведите на экран(в консоль)
# 3. Выведите на экран(в консоль) 2 умноженное на 2 плюс 2 с приоритетом для сложения.
# 4. Выведите на экран(в консоль) результат сравнения этих двух выражений.
# Предполагаемый результат (с использованием ==): False

# Ответ:
print(2 * 2 + 2) # - производим умножение на 2 плюс 2 без приоритета.
print((2 + 2) * 2) # - производим умножение на 2 с приоритетом на плюс.
print(2 * 2 + 2 == (2 + 2) * 2) # - сравниваем выражения и узнаем верны ли они.
#-----------------------------------------------------------------------------------------------------------------------
# D:\Программы\ProjectPyton\BasiesStructures\Scripts\python.exe D:\Программы\ProjectPyton\BasiesStructures\homework.py
# 6
# 8
# False
# Process finished with exit code 0
#------------------------------------------------------------------------------------------------------------------------

#                          ------------ Задача №4 (сложно) "Первый после точки" -------------
'4th program'
# Задача:
# 1. Напишите в начале программы однострочный комментарий: "4th program".
# 2. Дана строка '123.456'.
# 3. Вывести на экран первую цифру после запятой - 4.

# Ответ:
print(float('123.456')) # - переводим строчный тип данных в числовой - дробный.
print(type(float('123.456'))) # - проверяем командой и получаем подтверждение типа данных.
print(float('123.456') * 10) # - умножаем на 10
print(type(int( 1234.56))) # - проверяем командой и получаем подтверждение типа данных.
print(int(1234.56) / 10) # - делим на 10
print(float('123.456') * 10), print(int(1234.56) / 10) # - записываем одной строкой.
#-----------------------------------------------------------------------------------------------------------------------
#D:\Программы\ProjectPyton\BasiesStructures\Scripts\python.exe D:\Программы\ProjectPyton\BasiesStructures\homework.py
# 123.456
# <class 'float'>
# 1234.56
# <class 'int'>
# 123.4
#1234.56
#123.4
# Process finished with exit code 0
#-----------------------------------------------------------------------------------------------------------------------






