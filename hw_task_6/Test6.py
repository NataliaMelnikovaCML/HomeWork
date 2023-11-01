from keras.models import Sequential
from keras.layers import Dense
import numpy as np

np.set_printoptions(precision=2, floatmode='fixed', suppress=True)
dataset = np.genfromtxt('../data.txt', delimiter=',', dtype=float)
dataset = dataset[1:]

for i in range(len(dataset[0]) - 1):
    dataset = dataset[~np.isnan(dataset[:, i])]

dataset = np.around(dataset, 2)

Y = dataset[:, -1]
X = dataset[:, :9]

model = Sequential() # создаем модель
model.add(Dense(12, input_dim=9, activation='relu'))  #добавляет слой через класс, класс dense мы можем подстроить для себя
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#обучение
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=15, batch_size=10, verbose=2)

print('предсказание')
predictions_0 = model.predict(np.array(X[:3]))
print(predictions_0)


