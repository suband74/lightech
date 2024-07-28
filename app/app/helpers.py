import random
import string


def generate_random_password(length: int = 10) -> str:
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation
    all = lower + upper + numbers + symbols
    temp = random.sample(all, length)
    password = ''.join(temp)
    return password