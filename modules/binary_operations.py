# Unsigned
def division_unsigned(binary1, binary2):
    pass

def multiplication_unsigned(binary1, binary2):
    pass

def subtraction_unsigned(binary1, binary2): # Not sure if working correctly
    max_len = max(len(binary1), len(binary2))
    binary1 = binary1.zfill(max_len)
    binary2 = binary2.zfill(max_len)

    borrow = 0
    result = ""
    decimal_index = None

    if '.' in binary1 or '.' in binary2:
        decimal_index = binary1.index('.') - len(binary1) + 1

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
    max_len = max(len(binary1), len(binary2))
    binary1 = binary1.zfill(max_len)
    binary2 = binary2.zfill(max_len)

    carry = 0
    result = ""
    decimal_index = None

    if '.' in binary1 or '.' in binary2:
        decimal_index = binary1.index('.') - len(binary1) + 1

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