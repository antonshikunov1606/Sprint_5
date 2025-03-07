import random


def generate_unique_email():
    unique_id = random.randint(10000, 999999)
    return f"anton_shikunov_{unique_id}@yandex.ru"
