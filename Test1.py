# Задание 1

# s1 = "Hi"
# s2 = ""
# s3 = "Python"
#
# def string_length(example):
#     print(len(example))
#
# string_length("Hi")
# string_length("")
# string_length("Python")


# Задание 2

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8, 9]
# c = [a, b]
# def find(ex):
#     # for i in ex:
#         if len(a) > len(b):
#             print(len(a))
#         else:
#             print(len(b))
# find(c)


# Задание 3

# a = [1, 2, 3, 4, 8, 1]
# rnd = 5
# def adding(list):
#     list.append(rnd)
#     print(list)
#
# adding(a)


# Задание 4

# def function(count):
#     if count > 100 or count < -100:
#         print("-")
#     else:
#         print("+")
#
#
# function(-120)

# Задание 5

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

# Задание 6

# a = [-1, 2, 5, -6, 3]
# c = []
#
# def howmany(ex):
#     for i in ex:
#         if i > 0:
#             c.append(i)
#     # print(c)
#     print(len(c))
#
# howmany(a)

# Задание 7

# a = 5 # кол-во лет
# b = 3 # кол-во месяцев

# def days(a,b):
#     count = b * 29 + a * 12 * 29 #перевод в дни
#     print(count)
# days(10,11)

# Задание 8

stroka = "Я не могу это использовать"

# str =55
def main():
    try:
        split = stroka.split()
        operate(split)

    except:
        print('ето не строка')



# print(split)
c = []
# new_stroka = ''

def operate(data):
    new_stroka = ''
    for i in data:
        # print(i[0])
        c.append(i[0])
        new_stroka += i[0]
    print(new_stroka)

main()

# else:
# print("fail")

# def name(str):
#     for i in (split):
#         print(i[0])
#         c.append(i[0])
# # print(c)
#     else:
#         print("fail")
# print(c)



# Задание 9

# def fact(n):
#     f = 1
#     for i in range(1, n+1):
#         f *= i
#     print(f)
#
# fact(3)
# fact(6)
# fact(8)

# Задание 10

# lst = [2, 4, 5, 8, 9, 13]
# i = 0
# while i < len(lst):
#     lst[i] *= i
#     i += 1
# print(lst)
