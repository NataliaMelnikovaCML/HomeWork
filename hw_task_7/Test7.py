# задание 2

from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd


df = pd.read_csv('titanic.csv')
Survived = df['Survived']
df['Survived'] = df['SexCode']
df['SexCode'] = Survived

df = df.rename(columns={'Survived':'SexCode1'})
df = df.rename(columns={'SexCode':'Survived'})
df = df.rename(columns={'SexCode1':'SexCode'})

df.to_csv('new_titanic.csv', index=False)
df_new = pd.read_csv('new_titanic.csv')
df_new = df_new.dropna(axis='index', how='any')
df_new.to_csv('new_titanic_without_nan.csv', index=False)

df_x_train = df_new.drop(['Survived','Name','Sex','PClass'],axis='columns')
df_y_train = df_new.drop(['PassengerID','Name','PClass','Age','Sex','SexCode'],axis='columns')
model = svm.SVC()
model.fit(df_x_train, np.ravel(df_y_train))

y_test = model.predict(df_x_train[:11])
print(y_test)
print(df_y_train[:11])