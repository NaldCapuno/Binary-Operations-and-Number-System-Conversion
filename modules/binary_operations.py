def division_unsigned(binary1, binary2):
    strings = [binary1, binary2]
    decimals = []

    for x in strings:
        decimal = 0
        # checking for radix
        if '.' in x:
            whole, frac = x.split('.')

            # converting binary to decimal
            for i in range(len(whole)-1, -1, -1):
                decimal += int(whole[i]) * (2**(len(whole)-1-i))

            for i in range(1, len(frac)+1):
                decimal += int(frac[i-1]) * (2**(-i))

        else:
            for i in range(len(x)-1, -1, -1):
                decimal += int(x[i]) * (2**(len(x)-1-i))
        
        decimals.append(decimal)

    quotient = str(decimals[0] / decimals[1])
    return quotient

def multiplication_unsigned(binary1, binary2):
    strings = [binary1, binary2]
    decimals = []

    for x in strings:
        decimal = 0
        # checking for radix
        if '.' in x:
            whole, frac = x.split('.')

            # converting binary to decimal
            for i in range(len(whole)-1, -1, -1):
                decimal += int(whole[i]) * (2**(len(whole)-1-i))

            for i in range(1, len(frac)+1):
                decimal += int(frac[i-1]) * (2**(-i))

        else:
            for i in range(len(x)-1, -1, -1):
                decimal += int(x[i]) * (2**(len(x)-1-i))
        
        decimals.append(decimal)

    product = str(decimals[0] * decimals[1])
    return product

def subtraction_unsigned(binary1, binary2):
    strings = [binary1, binary2]
    decimals = []

    for x in strings:
        decimal = 0
        # checking for radix
        if '.' in x:
            whole, frac = x.split('.')

            # converting binary to decimal
            for i in range(len(whole)-1, -1, -1):
                decimal += int(whole[i]) * (2**(len(whole)-1-i))

            for i in range(1, len(frac)+1):
                decimal += int(frac[i-1]) * (2**(-i))

        else:
            for i in range(len(x)-1, -1, -1):
                decimal += int(x[i]) * (2**(len(x)-1-i))
        
        decimals.append(decimal)

    difference = str(decimals[0] - decimals[1])
    return difference

def addition_unsigned(binary1, binary2):
    strings = [binary1, binary2]
    decimals = []

    for x in strings:
        decimal = 0
        # checking for radix
        if '.' in x:
            whole, frac = x.split('.')

            # converting binary to decimal
            for i in range(len(whole)-1, -1, -1):
                decimal += int(whole[i]) * (2**(len(whole)-1-i))

            for i in range(1, len(frac)+1):
                decimal += int(frac[i-1]) * (2**(-i))

        else:
            for i in range(len(x)-1, -1, -1):
                decimal += int(x[i]) * (2**(len(x)-1-i))
        
        decimals.append(decimal)

    sum = str(decimals[0] + decimals[1])
    return sum

def negative_unsigned(binary):
    pass