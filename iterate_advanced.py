import fire
from functools import reduce  # python 3 need import

def filter_tutor():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    f = list(filter(lambda n: n > 5, a))
    print("filter(lambda n: n if n > 5, a) : {}".format(f))


def map_tutor():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    m = list(map(lambda n: n * 2, a))
    print("map(lambda n: n * 2, a) : {}".format(list(m)))


def reduce_tutor():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    d = reduce(lambda x, y: x+y, a)
    print("reduce(lambda x, y: x + y, a) : {}".format(d))


if __name__ == '__main__':
    fire.Fire()