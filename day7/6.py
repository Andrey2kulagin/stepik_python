import random

def generate_ip():
    out_str = ""
    while out_str.count('.')<4:
        out_str += (str(random.randint(0,255))+'.')
    return out_str[:-1]




