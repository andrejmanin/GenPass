import random

def symbol(upper, lover, nums, specifyc_sym):
    pas = ""
    symbols = []
    up = ""
    lov = ""
    num = ""
    sp_sym = ""

    if upper:
        up = [chr(s) for s in range(65, 90)]
    if lover:
        lov = [chr(s) for s in range(97, 122)]
    if nums:
        num = [chr(s) for s in range(48, 57)]
    if specifyc_sym:
        sp_sym = [chr(s) for s in range(33, 47)]
    for el in up, lov, num, sp_sym:
        symbols += el
    return symbols

def generate(nums_count):
    symbols = symbol(True, True, True, True)
    password = ""
    for i in range(nums_count):
        password += random.choice(symbols)
    print(password)

generate(12)