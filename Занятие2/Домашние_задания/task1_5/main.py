from string import ascii_lowercase, ascii_uppercase, digits
import random


if __name__ == "__main__":
    print(ascii_lowercase)
    print(ascii_uppercase)
    print(digits)

    alphabet = ascii_lowercase + ascii_uppercase + digits
    password = ''.join(random.sample(alphabet, 8))
    print(f'Рекомендуемый пароль: {password}')
