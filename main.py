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

def generate(nums_count, symbols):
    password = ""
    for i in range(nums_count):
        password += random.choice(symbols)
    print(password)

def show():
    len = int(input("Enter a len of your pass: "))
    is_example = str(input("Did you have an example (y/n): "))
    if is_example == 'n' or is_example == 'N':
        up = str(input("Upper latters (y/n): "))
        low = str(input("Lover latters (y/n): "))
        nums = str(input("Numbers (y/n): "))
        sp = str(input("Spesific symbols (y/n): "))

        up_sym = False
        low_sym = False
        nums_sym = False
        sp_sym = False

        if up == 'y' or up == 'Y':
            up_sym = True

        if low == 'y' or low == 'Y':
            low_sym = True

        if nums == 'y' or nums == 'Y':
            nums_sym = True

        if sp == 'y' or sp == 'Y':
            sp_sym = True

        generate(len, symbol(up_sym, low_sym, nums_sym, sp_sym))
    else:
        example_let = input("Enter your example letters: ")
        symbols = [el for el in example_let]
        generate(len, symbols)

show()