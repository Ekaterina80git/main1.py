# дано : 3 целых числа переменные (first,second,third) написать условие которое выводит
# которая выводит колличество одинаковых чисел среди введенных

first = int(input("Введите число :   "))
second = int(input("Ввведите число:   "))
third = int(input("Введите число:    "))

if first != second and first != third and second != third:
    print(0)
elif first == second and first == third and second == third:
    print(3)
else:
    print(2)



























