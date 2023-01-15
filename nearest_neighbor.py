import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

X, y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

X = MinMaxScaler().fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=2)

y_predict = np.empty(len(y_test), dtype=np.int64)

lines = []


def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi) ** 2
    return np.sqrt(sum)


def main(X_train, X_test, y_train, y_test):
    global y_predict
    global lines

    for i, test_item in enumerate(X_test):
        distances = [dist(train_item, test_item) for train_item in X_train]

        nearest = np.argmin(distances)

        lines.append(np.stack((test_item, X_train[nearest])))

        y_predict[i] = y_train[nearest]

    print(y_predict)


main(X_train, X_test, y_train, y_test)
