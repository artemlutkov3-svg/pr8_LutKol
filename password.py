import random
import string

def generate_password(n):
    symbols = string.ascii_lowercase + string.ascii_uppercase
    password = ''.join(random.choice(symbols) for _ in range(n))
    return password

n = int(input("Введите длину пароля: "))
print("Сгенерированный пароль:", generate_password(n))