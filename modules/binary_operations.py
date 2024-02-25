def operations(binary1, binary2, select, option):
    strings = [binary1, binary2]
    decimals = []

    for x in strings:
        decimal = 0

        # checking for radix
        if '.' in x:
            whole, frac = x.split('.')

            # converting binary to decimal
            for i in range(len(whole)-1, -1, -1):
                # signed
                if i == 0 and whole[i] == '1' and option == '1':
                    decimal += (int(whole[i]) * -1) * (2**(len(whole)-1-i))
    
                # unsigned
                else:
                    decimal += int(whole[i]) * (2**(len(whole)-1-i))

            for i in range(1, len(frac)+1):
                decimal += int(frac[i-1]) * (2**(-i))

        # conversion without radix
        else:
            for i in range(len(x)-1, -1, -1):
                # signed
                if i == 0 and x[i] == '1' and option == '1':
                    decimal += (int(x[i]) * -1) * (2**(len(x)-1-i))

                # unsigned
                else:
                    decimal += int(x[i]) * (2**(len(x)-1-i))
    
        decimals.append(decimal)

    binary1, binary2 = decimals[0], decimals[1]

    # division
    if select == '1':
        quotient = binary1 / binary2
        return quotient
        
    # multiplication
    elif select == '2':
        product = binary1 * binary2
        return product

    # subtraction
    elif select == '3':
        difference = binary1 - binary2
        return difference

    # addition
    elif select == '4':
        sum = binary1 + binary2
        return sum
    
def twos_complement(binary):
    binary = list(binary)

    for i in range(len(binary)-1, -1, -1):
        if binary[i] == '1':
            for j in range(i-1, -1, -1):
                if binary[j] == '.':
                    continue
                elif binary[j] == '1':
                    binary[j] = '0'
                else:
                    binary[j] = '1'
            break

    binary = ''.join(binary)
    return binary