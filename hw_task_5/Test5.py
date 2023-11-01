# задание 1  - ok
# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame(np.random.randint(1, 10, size=(10, 10)))
# print(df)

#задание 2 - ne ok
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, size=(10, 10)), index=['A', 'B', 'C', 'D', 'E', 'G', 'H', 'I', 'J', 'K'])
# print(df)



# print(df)
# for i in df.loc['A':'K']:
#     if i <5:
#         df2 = df.drop('A')
# print(df2)

# for i in df.index:
#     # print(i)
#     for j in df.loc[i]:
#     # print(j)
#         if j < 2:
#     #         print(df)
#     #         df2 = df.drop(df.loc[i])
#     # print(df2)
# print(df['A':'C'])
#
# for i in df.loc['A']:
#     # print(i)
#     if i < 5:
#         df2 = df.drop('A')
# print(df2)

# print(df)
# for j in df.index:
# #     # print(j)
# #     for i in df.loc[j]:
# #         # print(i)
# #         # print(df.loc['A'])
# #         if i < 5:
# #             print('aga')

# for j in df.index:
# #     for i in df.loc[j]:
# #         if
# print(df)
# # print(df.loc['A'])
# print(df.iloc[1])

#  forj in range(1,9):
#     for i in df.iloc[j]:
#         if i <5:
#             df2 = df.drop(df.iloc[j,:],axis=0)
# print(df2)

# print(df['A':'C'])
# df2 = df.drop(df.index)
# print(df2)
# print(df.iloc[0:3])


# print(df['A':'C'])
# gg = df.iloc[1]
# print(gg)
#
# for i in gg:
#     if i >= 5:
#         print('alo')
#     else:
#         print('меньше 5')
#         df2 = df.drop(df.index[1])
# print(df2)

# print(df.index[1])
# print(df['B'])
# print(df['A':'C'])
print(df['A'])
# print(df.loc['B'])
# for j in range(0,1):
#     gg = df.iloc[j]
#     print(gg)
    # print(df.index[gg])

# print(df['A':'C'])
# for j in range(0,3):
#     gg = df.iloc[j]
#     # print(gg)
#     for i in gg:
#         if i >=5:
#             print('aga')
#         else:
#             print('меньше 5')
#         print(df.index[gg])
#             df2 = df.drop(df.index[gg])
#
# print(df2)

        # print(i)
    # print(j)


    # if i < 5:
    #     print('aga')
    # else:
    #     print(i)
    #
    # print(i)

# if i<5:
#     print('aga')
    # if i < 5:
        # print('ok')
#         ff = df.drop(gg)
# print(ff)



# print(df['A':'C'])
# for i in df.iloc[1]:
#     if i <5:
#         df2 = df.drop('B')
# print(df2)


# for j in range(0,10):
#     # print(j)
#     for i in df.iloc[j]:
#         if i <5:
#             df2 = df.drop(df.index[j])
# print(df2)




# print(df.iloc[9])





# for j in df.index:
#     for i in df.loc[j]:
#         if i.any() < 5:
#             df2 = df.drop(j)
# print(df2)

    # for j in df.index:
    #     for i in df.loc[j]:
    #         if i < 5:
    #             df2=df.drop(j)
    # print(df2)




# print(df.index)
# print(df)
# print(df.index)
# for i in df.index:
    # print(df.loc[i])
#     if df.loc[i] < 2:
#         df2 = df.drop(df.loc[i])
# print(df2)
# print(df.loc['A'] <2)



    # if i <2:
#         df2 = df.drop()
# print(df2)
# print(df.loc['A':'K'])


# df2 = df.drop('A',axis=0)
# print(df2)
# # new_df = df.loc[df['A':'C'] >= 5]
# print(new_df)



# out = df[df[0:9] >= 2]
# print(out)


# print(len(df.values))
# print(type(df.values))
# print(df.values[1, 1])
# print(df.values[df.values >= 2])
# print(df.values)
# print(df.values.tolist())
# for i in df.loc['A'] >=2:
#     print(df.loc['A'][i])
    # print(df.loc['A'])
    # print('ok')
# print(df.loc['A'])

# print(df[df >= 2])
# print(df['A':'C'])
# if df['A':'K'][df >= 2]:
#     print(df)

# for i in range(0, 9):
#     if df.all[0:9, i] >=2:
#         print(df.values[0:9, i])

# print(d)
#
# print(df.loc['A':'C'] >= 2)
# print(df.loc[0:2])


# if all(df.loc['A':'C'] >=2):
#     print('ok')
# else:
#     print('ne ok')
# print(df.loc['A':'C'])


# print(df.loc['A'] >= 2)
# # if bool(df.loc['A'] >=2) == True:
# for i in (df.loc['A']) >=2:
#     print(i)
#     if i == False:
#         print('ne ok')
#     if i == True:
#         print(df.loc['A'])
#     print(i)
#     # if any(i):
#     #     print('ok')
# else:
#     print('ne ok')


# print(df.iloc[0:3][0:10])
# print(df.iloc[0][0:10])
# # if i in df.iloc[0][0:10] >=
# for i in range(0, 3):
#     # for j in range(0, 10):
#     if df.iloc[i][0:10].all() >= 2:
#         print(df.iloc[i][0:10])

    # print(df.iloc[i][0:10])

# print(df.values['A', 0:10])

# for i in (df.values['A', 0:9]) >=2:
#     print('ok')
# else:
#     print('ne ok')

#задание 3 - ok

# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame(np.random.randint(1, 10, size=(10, 10)), index=['A', 'B', 'C', 'D', 'E', 'G', 'H', 'I', 'J', 'K'], columns=['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'k'])
# print(df)
#
# print(df.shape)
# print(df.columns)
# print(df.mean())
# print(df.mean().mean())
#
# df.to_csv('data.csv')

#задание 4 - ok

# import pandas as pd
# df = pd.read_csv('emojis.csv')
# print(df)
# print(df.columns)
#
# group = df.groupby('Subcategory').count()
# print(group)
# print(group.Rank.min()) #самая популярная подкатегория
# print(group[group.Rank == group.Rank.min()])

#задание 5 - ok
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('emojis.csv')
# print(df)
# print(df.columns)
#
# print(df['Year'])
#
# df['number'] = 1
# print(df)
# print(df.groupby('Year')['number'].count())
# # counter = df.groupby('Year')['number'].count()
#
# plt.plot(df.groupby('Year')['number'].count())
# plt.show()


#Задание 6 - ok
# import pandas as pd
# df = pd.read_csv('emojis.csv')
# # print(df)
# # print(len(df))
# # print(df.columns)
# # print(df['Category'])
#
# #
# def name(name_str):
#     isPresent = name_str in df
#     if isPresent == True:
#         counter = df.groupby(name_str)[name_str].count() * 100 / len(df)
#         print('% сделанных эмоджи в категории')
#         print(counter)
#
#     else:
#         print('нет категории')
# #
# name('Category')
# name('gfdg')



#Задание 7 - ok
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('BCT-USD.csv')
#
# def plot(date_1, date_2):
#     mm = df.groupby('Date')['Open'].mean()
#     plt.plot(mm.loc[date_1:date_2])
#     plt.show()
#
# plot('2021-10-24', '2021-10-31')
#

#задание 8 - ok
# import pandas as pd
# df = pd.read_csv('BCT-USD.csv')
#
#
# str = df[df['Volume']==df['Volume'].min()]
# print(str['Date']) #вытаскивается дата
# print(str['Date'].str[5:7]) #вытаскивается месяц

#задание 9 - ??
# import pandas as pd
# df = pd.read_csv('BCT-USD.csv')
#
# # for i in df['Date']
# str = df[df['Close'] > df['Open']]
# print(str['Date'].str[5:7])

