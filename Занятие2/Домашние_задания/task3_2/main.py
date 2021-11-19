def decorator(fn):
    def wrapper(*args):
        for i in args:
            if not isinstance(i, int):
                raise TypeError(f'Аргументы функции {fn} должны быть целыми числами')
        result = fn(*args)
        return result

    return wrapper


@decorator
def func(*args):
    pass


if __name__ == "__main__":
    func(1, 2, 3, 4.1)
