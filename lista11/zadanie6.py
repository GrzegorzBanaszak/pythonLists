def dec_to_bin(value):
    try:
        bin_value = bin(value)
        print(bin_value[2:])
    except TypeError:
        print("Podana wartość jest nieprawidłowa")


def dec_to_oct(value):
    try:
        oct_value = oct(value)
        print(oct_value[2:])
    except TypeError:
        print("Podana wartość jest nieprawidłowa")


def dec_to_hex(value):
    try:
        hex_value = hex(value)
        print(hex_value[2:])
    except TypeError:
        print("Podana wartość jest nieprawidłowa")


def bin_to_hex(value):
    try:
        dec_num = int(value, 2)
        dec_to_hex(dec_num)
    except TypeError:
        print("Podana wartość jest nieprawidłowa")


def bin_to_oct(value):
    try:
        dec_num = int(value, 2)
        dec_to_oct(dec_num)
    except TypeError:
        print("Podana wartość jest nieprawidłowa")


def hex_to_bin(value):
    try:
        dec_num = int(value, 16)
        dec_to_bin(dec_num)
    except TypeError:
        print("Podana wartość jest nieprawidłowa")


def hex_to_oct(value):
    try:
        dec_num = int(value, 16)
        dec_to_oct(dec_num)
    except TypeError:
        print("Podana wartość jest nieprawidłowa")


def oct_to_bin(value):
    try:
        dec_num = int(value, 8)
        dec_to_bin(dec_num)
    except TypeError:
        print("Podana wartość jest nieprawidłowa")


def oct_to_hex(value):
    try:
        dec_num = int(value, 8)
        dec_to_hex(dec_num)
    except TypeError:
        print("Podana wartość jest nieprawidłowa")


dec_to_bin(30)
dec_to_oct(30)
dec_to_hex(30)


hex_to_bin("ff")
