import string
import secrets


def generate_key(size):
    key = string.ascii_lowercase + string.digits
    return ''.join(secrets.choice(key) for _ in range(size))
