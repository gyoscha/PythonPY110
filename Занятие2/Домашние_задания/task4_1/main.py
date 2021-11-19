def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield ','.join(iterable[i], iterable[i+1])


def task(*args):
    list_ = (list(value) for value in args)
    for i in pairwise(list_):
        print(i)




if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    list_ = [list(value) for value in pts]
    e = map(pairwise, list_)
    print(next(e))


