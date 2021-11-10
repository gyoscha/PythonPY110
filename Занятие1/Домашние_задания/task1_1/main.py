if __name__ == "__main__":
    # Write your solution here
    from random import randint

    print('Список продуктов:')

    price = [randint(51, 199) for value in range(20)]
    product = ['яйца', 'колбаса', 'хлеб', 'сыр']

    for i, (price, product) in enumerate(zip(price, product), start=1):
        print(f'№ {i}: - {product}: {price} руб.')
