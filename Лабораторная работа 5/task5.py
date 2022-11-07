import random
import string

def get_random_password() -> str:
    from random import sample
    return ''.join(random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 8))

print(get_random_password())