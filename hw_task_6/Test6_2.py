from keras.models import Sequential
from keras.layers import Dense
import numpy as np

class Neur:
    def __init__(self, path_dataset='data.txt', input_dim=9, output_dim=2, h_dim=25, alpha=0.00001, num_epochs=1000, batch_size=30):
        self.path_dataset = path_dataset
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.h_dim = h_dim
        self.alpha = alpha
        self.num_epochs = num_epochs
        self.batch_size = batch_size

        self.dataset = []
        self.nn_weights = {}

    def data_preparation(self):

        dataset = np.genfromtxt(self.path_dataset, delimiter=',', dtype=float)
        dataset = dataset[1:]

        for i in range(len(dataset[0]) - 1):
            dataset = dataset[~np.isnan(dataset[:, i])]

        dataset[:, 2] = dataset[:, 2] * 0.001
        dataset[:, 4] = dataset[:, 4] * 0.01
        dataset[:, 5] = dataset[:, 5] * 0.01
        dataset = np.around(dataset, 2)

        target = dataset[:, -1]
        dataset = dataset[:, :9]
        if dataset.shape[0] != target.shape[0]:
            raise Exception("количество обучаемйо выборки не равно количеству ответов")

        self.dataset = [(dataset[i][None, ...], int(target[i])) for i in range(len(target))]

    def inference(self, x):  #первый проход нейронки
        if not self.nn_weights:
            raise Exception('Сеть не обучена')
        t1 = x @ self.nn_weights['W1'] + self.nn_weights['b1']
        h1 = self.relu(t1)
        t2 = h1 @ self.nn_weights['W2'] + self.nn_weights['b2']
        z = self.softmax_batch(t2)

        return np.argmax(z)
    def training(self):
        self.data_preparation()

        self.nn_weights['W1'] = np.random.rand(self.input_dim, self.h_dim)
        self.nn_weights['b1'] = np.random.rand(1, self.h_dim)
        self.nn_weights['W2'] = np.random.rand(self.h_dim, self.output_dim)
        self.nn_weights['b2'] = np.random.rand(1, self.output_dim)

        self.nn_weights['W1'] = (self.nn_weights['W1'] - 0.5) * 2 * np.sqrt(1 / self.input_dim)
        self.nn_weights['b1'] = (self.nn_weights['b1'] - 0.5) * 2 * np.sqrt(1 / self.input_dim)
        self.nn_weights['W2'] = (self.nn_weights['W2'] - 0.5) * 2 * np.sqrt(1 / self.h_dim)
        self.nn_weights['b2'] = (self.nn_weights['b2'] - 0.5) * 2 * np.sqrt(1 / self.h_dim)


        loss_arr = []

        for ep in range(self.num_epochs):
            random.shuffle(self.dataset)
            for i in range(len(self.dataset) // self.batch_size):
                batch_x, batch_y = zip(*self.dataset[i * self.batch_size: i * self.batch_size + self.batch_size])
                x = np.concatenate(batch_x, axis=0)
                y = np.array(batch_y)

            #forward
                t1 = x @ self.nn_weights['W1'] + self.nn_weights['b1']
                h1 = self.relu(t1)
                t2 = h1 @ self.nn_weights['W2'] + self.nn_weights['b2']
                z = self.softmax_batch(t2)
                E = np.sum(self.sparse_cross_entropy_batch(z, y))

            #backward
                y_full = self.to_full_batch(y, self.output_dim)
                dE_dt2 = z - y_full
                dE_dW2 = h1.T @ dE_dt2
                dE_db2 = np.sum(dE_dt2, axis=0, keepdims=True)
                dE_dh1 = dE_dt2 @ self.nn_weights['W2'].T
                dE_dt1 = dE_dh1 * self.relu_deriv(t1)
                dE_dW1 = x.T @ dE_dt1
                dE_db1 = np.sum(dE_dt1, axis=0, keepdims=True)

            #update
                self.nn_weights['W1'] = self.nn_weights['W1'] - self.alpha * dE_dW1
                self.nn_weights['b1'] = self.nn_weights['b1'] - self.alpha * dE_db1
                self.nn_weights['W2'] = self.nn_weights['W2'] - self.alpha * dE_dW2
                self.nn_weights['b2'] = self.nn_weights['b2'] - self.alpha * dE_db2

                loss_arr.append(E)


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

    # print('предсказание')
    # predictions_0 = model.predict(np.array(X[:3]))
    # print(predictions_0)


