def decorator(fn):
    def wrapper(*args, **kwargs):
        for index, arg in enumerate(args):
            try:
                iter(arg)
                print(f"Объект {index} - {arg} является итерируемым")
            except TypeError:
                print(f"Объект {index} - {arg} НЕ является итерируемым")

        for key, kwarg in kwargs.items():
            try:
                iter(kwarg)
                print(f"Объект {key}: {kwarg} является итерируемым")
            except TypeError:
                print(f"Объект {key}: {kwarg} НЕ является итерируемым")

        result = fn(*args, **kwargs)
        return result

    return wrapper


@decorator
def func(*args, **kwargs):
    print('End')


if __name__ == "__main__":
    func([1, 2, 3], (5, 6), 'arg', 1.1, k1='str', k2=1)
    # print((_ for _ in enumerate([1, 2, 3])) is True)
