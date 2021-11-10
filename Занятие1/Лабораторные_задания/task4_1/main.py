from itertools import count


def task():
    counter = count(100, 10)

    for _ in range(10):   # TODO распечатать с столбик первые 10 чисел бесконечного итератора
        print(next(counter))


if __name__ == "__main__":
    task()
