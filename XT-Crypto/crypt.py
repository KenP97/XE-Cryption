import random


def encrypt(message, password):

    code = [ord(i) for i in message]
    password = sum([ord(i) for i in password])
    code = [i+password for i in code]
    e_message = []
    for i in code:
        c = sorted(random.sample(range(1, i), 3 - 1))
        e_message += (a - b for a, b in zip(c + [i], [0] + c))
    e_message = "." + ".".join(str(i) for i in e_message)
    return e_message


def decrypt(code, password):

    password = sum([ord(i) for i in password])
    code = code.replace(".", " ").split()
    code = [int(i) for i in code]
    code = [sum(code[i:i + 3]) for i in range(0, len(code), 3)]
    code = [i-password for i in code]
    d_message = ''.join(chr(i) for i in code)
    return d_message


