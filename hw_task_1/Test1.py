# Задание 1 - ok

# def string_length(example):
#     print(len(example))
#
# string_length("Hi")
# string_length("")
# string_length("Python")


# Задание 2 - ok

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8, 9, 10]
# c = [a, b]
# def find(ex):
#     if len(a) > len(b):
#         print(len(a))
#     else:
#         print(len(b))
# find(c)


# Задание 3- ok

# a = [1, 2, 3, 4, 8, 1]
# rnd = 5
# def adding(list):
#     list.append(rnd)
#     print(list)
#
# adding(a)


# Задание 4 - ok

# def function(count):
#     if count > 100 or count < -100:
#         print("-")
#     else:
#         print("+")
#
#
# function(-120)

# Задание 5 - ok

# str_1 = 'test'
# str_2 = 'test1'
#
# def quest(string):
#
#     if string == str_2[0:len(string)]:
#         print("Да")
#     else:
#         print("Нет")
#
# quest(str_1)

# Задание 6 - ok

# a = [-1, 2, 5, -6, 3]
# c = []

# def howmany(ex):
#     for i in ex:
#         if i > 0:
#             c.append(i)
#     # print(c)
#     print(len(c))
#
# howmany(a)

# Задание 7 - ok

# a = 5 # кол-во лет
# b = 3 # кол-во месяцев
#
# def days(a,b):
#     count = b * 29 + a * 12 * 29 #перевод в дни
#     print(count)
# days(10,11)

# Задание 8 - ok

# c = []
#
# def main(stroka):
#     new_stroka = ""
#     try:
#         split = stroka.split()
#
#         for i in split:
#
#             c.append(i[0])
#             new_stroka += i[0]
#         print(new_stroka)
#
#
#     except:
#         print('это не строка')
#
#
# main('я не могу это использовать')
# main(1232)

# Задание 9 - ok

# def fact(n):
#     f = 1
#     for i in range(1, n+1):
#         f *= i
#     print(f)
#
# fact(3)
# fact(6)
# fact(8)

# Задание 10 - ok

# lst = [2, 4, 5, 8, 9, 13]
# i = 0
# while i < len(lst):
#     lst[i] *= i
#     i += 1
# print(lst)
