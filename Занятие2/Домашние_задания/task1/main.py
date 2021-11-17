def count(start_number, geom):
    while True:
        yield start_number
        start_number *= geom


if __name__ == "__main__":
    my_count = count(6, 2)
    for _ in range(20):
        print(next(my_count))
