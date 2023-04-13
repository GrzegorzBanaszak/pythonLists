def convert(number):
    return dec_to_bin(number), dec_to_hex(number)


def dec_to_bin(value):
    bin_value = bin(value)
    print(bin_value[2:])


def dec_to_oct(value):
    oct_value = oct(value)
    print(oct_value[2:])


def dec_to_hex(value):
    hex_value = hex(value)
    print(hex_value[2:])


def bin_to_hex(value):
    dec_num = int(value, 2)
    dec_to_hex(dec_num)


def hex_to_bin(value):
    dec_num = int(value, 16)
    dec_to_bin(dec_num)


def hex_to_oct(value):
    dec_num = int(value, 16)
    dec_to_oct(dec_num)


def bin_to_oct(value):
    dec_num = int(value, 2)
    dec_to_oct(dec_num)


convert(255)
hex_to_bin("f")
bin_to_hex("1001")
