import numpy as np

X = np.array([[66, 5, 15, 2, 500],
              [21, 3, 50, 1, 100],
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])
c = np.array([3000, 200, -50, 5000, 100])


def squared_error(X, y, c):
    sse = 0.0
    prediction = 0.0
    subtract = 0.0
    square = 0.0
    for xi, yi in zip(X, y):
        prediction = (X @ c)
        subtract = y - prediction
        square = subtract ** 2
        sse = sum(square)

    print("%.1f" % sse)


squared_error(X, y, c)
