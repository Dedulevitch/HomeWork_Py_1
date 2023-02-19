# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
# РЕШЕНИЕ
# number = input("Введите трехзначное число")
# result = 0
# if len(number) == 3:
#     for i in number:
#         num = int(i)
#         result += num
#     print(result)
# else:print("Ошибка")
##########################################

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# РЕШЕНИЕ
# cranes = int(input("Введите общее количество сделанных журавлей"))
# if cranes % 2 == 0:
#     print(cranes // 6)
#     print(round(cranes // 1.5))
#     print(cranes // 6)
# else:print("Число с остатком")
#######################################

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
#РЕШЕНИЕ
# ticket = input("Введите шестизначный номер билета")
# if len(ticket) == 6:
#     result = 0
#     result2 = 0
#     slice = ticket[0:3]
#     slice2 = ticket[3:6]
#     for i in slice:
#         number = int(i)
#         result += number
#     for j in slice2:
#         number2 = int(j)
#         result2 += number2
#     if result == result2:
#         print("Ура !!! Счатливый билет")
#     else:print("У вас обычный билет")
#
# else: print("Задано неверное число")
################################################

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')