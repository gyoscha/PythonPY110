import json


def task():
    filename = "input.json"
    with open(filename) as f:   # TODO считать содержимое JSON файла
        json_data = json.load(f)

    gen_exr = (i['contains_improvement_appeals'] for i in json_data)  # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
