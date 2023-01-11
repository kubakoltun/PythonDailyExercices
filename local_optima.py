import math
import random

w = [random.random() / 3, random.random() / 3, random.random() / 3]
h = [1. + math.sin(1 + x / 6.) * w[0] + math.sin(-.3 + x / 9.) * w[1] + math.sin(-.2 + x / 30.) * w[2] for x in
     range(100)]
h[0] = 0.0
h[99] = 0.0


def climb(x, h):
    summit = False

    if h[x + 1] > h[x]:
        while not summit:
            summit = True
            if h[x + 1] > h[x]:
                x = x + 1
                summit = False
        return x
    else:
        while not summit:
            summit = True
            if h[x - 1] > h[x]:
                x = x - 1
                summit = False
        return x


def main(h):
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    print("Started at %d and got to %d" % (x0, x))
    return x0, x


main(h)
