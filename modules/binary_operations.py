# Unsigned
def division_unsigned(binary1, binary2):
    pass

def multiplication_unsigned(binary1, binary2):
    pass

def subtraction_unsigned(binary1, binary2):
    borrow = 0
    result = ""
    decimal_index = None

    # check for decimal
    if '.' in binary1 and '.' in binary2:
        decimal_index = binary1.index('.') - len(binary1) + 1

    # adding decimal if one have decimal and other have no decimal
    if '.' in binary1 and '.' not in binary2:
        decimal_index = binary1.index('.') - len(binary1) + 1
        binary2 = binary2 + '.' + ("0" * (decimal_index * -1))

    elif '.' in binary2 and '.' not in binary1:
        decimal_index = binary2.index('.') - len(binary2) + 1
        binary1 = binary1 + '.' + ("0" * (decimal_index * -1))

    # padding with 0s to make sure that both have same length
    max_len = max(len(binary1), len(binary2))
    binary1 = binary1.zfill(max_len)
    binary2 = binary2.zfill(max_len)

    # subtracting
    for i in range(max_len - 1, -1, -1):
        if binary1[i] == '.' or binary2[i] == '.':
            continue
        else:
            diff = int(binary1[i]) - int(binary2[i]) - borrow
            result = str(diff % 2) + result
            borrow = 1 if diff < 0 else 0

    if decimal_index:
        result = result[:decimal_index] + '.' + result[decimal_index:]

    print(f"\n{binary1} - {binary2} = {result}")

def addition_unsigned(binary1, binary2):
    carry = 0
    result = ""
    decimal_index = None

    # check for decimal
    if '.' in binary1 and '.' in binary2:
        decimal_index = binary1.index('.') - len(binary1) + 1

    # adding decimal if one have decimal and other have no decimal
    if '.' in binary1 and '.' not in binary2:
        decimal_index = binary1.index('.') - len(binary1) + 1
        binary2 = binary2 + '.' + ("0" * (decimal_index * -1))

    elif '.' in binary2 and '.' not in binary1:
        decimal_index = binary2.index('.') - len(binary2) + 1
        binary1 = binary1 + '.' + ("0" * (decimal_index * -1))

    # padding with 0s to make sure that both have same length
    max_len = max(len(binary1), len(binary2))
    binary1 = binary1.zfill(max_len)
    binary2 = binary2.zfill(max_len)

    # adding
    for i in range(max_len - 1, -1, -1):
        if binary1[i] == '.' or binary2[i] == '.':
            continue
        else:
            sum = int(binary1[i]) + int(binary2[i]) + carry
            result = str(sum % 2) + result
            carry = sum // 2

    if carry:
        result = "1" + result

    if decimal_index:
        result = result[:decimal_index] + '.' + result[decimal_index:]

    print(f"\n{binary1} + {binary2} = {result}")

def negative_unsigned(binary1, binary2):
    pass

# Signed
def division_signed(binary1, binary2):
    pass

def multiplication_signed(binary1, binary2):
    pass

def subtraction_signed(binary1, binary2):
    pass

def addition_signed(binary1, binary2):
    pass

def negative_signed(binary1, binary2):
    pass