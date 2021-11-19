def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield ((iterable[i][0] + iterable[i+1][0]) ** 2
               + (iterable[i][1] + iterable[i+1][1]) ** 2) ** 0.5


def task():
    length = sum(i for i in pairwise(pts))
    print(f'Длина ломаной линии = {length}')


if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    task()



