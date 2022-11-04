from pprint import pprint

def number_systems() -> list:

    pprint([{'bin': bin(i),'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(16)])

number_systems()