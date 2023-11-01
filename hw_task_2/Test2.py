# задание 1 - ok

# a = ["Python", "php", "go", "C"] #нужно убрать, список
# b = "Python age php color white go C" #строка
# c = []
# # # print(type(a))
# # # print(type(b))
# split = b.split()
# # # print(type(split))
# # # print(type(a))
# # # print(a)
# # # print(split)
# # print("a:", a)
# # print('split:', split)
#
# def fun(words):
#     for i in split:
#         if not (i in words):
#             c.append(i)
#     print("c = split - a:", c)
#     print("result:", ' '.join(c))
#
# fun(a)




# задание 2 - ok
# spisok = [2, 3, 6, 8, 10, 15, 21, 24, 65]
#
# new = []
#
# def kratnoe(a):
#     for item in spisok:
#         if item % a == 0:
#             new.append(item)
#     print(new)
#
# kratnoe(5)



# задание 3 - ok

# def add(*args):
#     value = []
#     for item in args:
#         if isinstance(item, str):
#             value.append(item)
#
#     return value
#
# result = add("apple", 1, 2, "new", "spisok")
# print(result)


#задание 4 - ok

# spisok_1 = [1, 2, 5, "python", "new"]
# spisok_2 = [3, 5, "new", 4]
# c = []
# def intersection(spisok_1, spisok_2):
#     for item in spisok_1:
#         if item in spisok_2:
#             c.append(item)
#     print(c)
#
# intersection([1, 2, 5, "python", "new"],[3, 5, "new", 4])


#задание 5 - ne ok


# задание 6 - ne ok
#
#
# aa = "5"
#
# try:
#     if isinstance(aa, int):
#         print("true")
# except Exception:
#     print("false")


# задание 8 - ne ok

# elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
#
#
# args = []
# # def name(args):
# for i in 0, 1, 2, 3:
#     args = (elements[i][0:len(elements)-1])
#     # args.append([i][2:3])
#     print(args)
# # print(len(args))



#     # args += i
#     # print(args)
#     args.append(i)
#     # c[i] = args[i]
# print(args)

# c = sorted(elements)
# print(c)
# def second(data):
#     return data[0][1:3]


# print(second(c))


# print(elements[0][0:3])
# print(elements[1][0:3])
# print(elements[2][0:3])
# print(elements[3][0:3])
