# binary
def binary_to_decimal(x, option):
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

    return decimal

def binary_to_hexa(x, option):
    hexa = []

    # checking for radix
    if '.' in x:
        whole, frac = x.split('.')

        # padding 0s or 1s to the binary to make sure it is divisible by 4
        # signed
        if whole[0] == '1' and option == '1':
            whole = '1' * (4 - len(whole) % 4) + whole if len(whole) % 4 != 0 else whole
            whole = '1111' + whole

        # unsigned
        else:
            whole = '0' * (4 - len(whole) % 4) + whole if len(whole) % 4 != 0 else whole

        frac = ''.join(list(frac) + ['0' * (4 - len(frac) % 4)]) if len(frac) % 4 != 0 else frac
        
        # slicing the binary by 4
        strings_whole = [whole[i:i+4] for i in range(0, len(whole), 4)]
        strings_frac = [frac[i:i+4] for i in range(0, len(frac), 4)]

        # conversion
        for string in strings_whole:
            temp = 0
            for i in range(len(string)-1, -1, -1):
                temp += int(string[i]) * (2**(len(string)-1-i))
            hexa.append(temp)

        hexa.append('.')

        for string in strings_frac:
            temp = 0
            for i in range(len(string)-1, -1, -1):
                temp += int(string[i]) * (2**(len(string)-1-i))
            hexa.append(temp)

    # conversion without radix
    else:
        # padding 0s or 1s to the binary to make sure it is divisible by 4
        # signed
        if x[0] == '1' and option == '1':
            x = '1' * (4 - len(x) % 4) + x if len(x) % 4 != 0 else x
            x = '1111' + x

        # unsigned
        else:
            x = '0' * (4 - len(x) % 4) + x if len(x) % 4 != 0 else x

        # slicing the binary by 4
        strings = [x[i:i+4] for i in range(0, len(x), 4)]

        # conversion
        for string in strings:
            temp = 0
            for i in range(len(string)-1, -1, -1):
                temp += int(string[i]) * (2**(len(string)-1-i))
            hexa.append(temp)

    # hex mapping
    hex_mapping = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

    for x in hexa:
        if x == '.':
            continue

        elif x >= 10:
            hexa[hexa.index(x)] = hex_mapping[x]

    for x in hexa:
        hexa[hexa.index(x)] = str(x)

    hexa = ''.join(hexa)
    return hexa

def binary_to_octal(x, option):
    octal = []

    # checking for radix
    if '.' in x:
        whole, frac = x.split('.')

        # padding 0s or 1s to the binary to make sure it is divisible by 3
        # signed
        if whole[0] == '1' and option == '1':
            whole = '1' * (3 - len(whole) % 3) + whole if len(whole) % 3 != 0 else whole
            whole = '111' + whole

        # unsigned
        else:
            whole = '0' * (3 - len(whole) % 3) + whole if len(whole) % 3 != 0 else whole

        frac = ''.join(list(frac) + ['0' * (3 - len(frac) % 3)]) if len(frac) % 3 != 0 else frac
        
        # slicing the binary by 3
        strings_whole = [whole[i:i+3] for i in range(0, len(whole), 3)]
        strings_frac = [frac[i:i+3] for i in range(0, len(frac), 3)]

        # conversion
        for string in strings_whole:
            temp = 0
            for i in range(len(string)-1, -1, -1):
                temp += int(string[i]) * (2**(len(string)-1-i))
            octal.append(str(temp))

        octal.append('.')

        for string in strings_frac:
            temp = 0
            for i in range(len(string)-1, -1, -1):
                temp += int(string[i]) * (2**(len(string)-1-i))
            octal.append(str(temp))

    # conversion without radix
    else:
        # padding 0s and 1s to the binary to make sure it is divisible by 3
        # signed
        if x[0] == '1' and option == '1':
            x = '1' * (3 - len(x) % 3) + x if len(x) % 3 != 0 else x
            x = '111' + x

        # unsigned
        else:
            x = '0' * (3 - len(x) % 3) + x if len(x) % 3 != 0 else x
            
        # slicing the binary by 3
        strings = [x[i:i+3] for i in range(0, len(x), 3)]

        # conversion
        for string in strings:
            temp = 0
            for i in range(len(string)-1, -1, -1):
                temp += int(string[i]) * (2**(len(string)-1-i))
            octal.append(str(temp))

    octal = ''.join(octal)
    return octal

# decimal
def decimal_to_binary(x):
    binary = []

    # check if negative
    if '-' in x:
        x = x.replace('-', '')

    # checking for radix
    if '.' in x:
        whole = int(x[:x.index('.')])
        frac = float(x) - whole

        temp_whole = []

        # conversion
        while True:
            temp_whole.append('1' if int(whole) % 2 != 0 else '0')

            whole = whole // 2
            if whole == 0:
                temp_whole.reverse()
                for i in temp_whole:
                    binary.append(i)
                break

        binary.append('.')
        decimal_count = 0

        while True:
            binary.append('1' if frac * 2 >= 1 else '0')
            frac = frac * 2 - 1 if frac * 2 >= 1 else frac * 2

            decimal_count += 1
            if frac == 0 or decimal_count == 9:
                break
        
    # conversion without radix
    else:
        x = int(x)
        while True:
            binary.append('1' if int(x) % 2 != 0 else '0')

            x = x // 2
            if x == 0:
                binary.reverse()
                break
    
    binary = ''.join(binary)

    # padding
    if '.' in binary:
        binary = '0' * (4 - len(binary[:binary.index('.')]) % 4) + binary if len(binary[:binary.index('.')]) % 4 != 0 else binary
    
    else:
        binary = '0' * (4 - len(binary) % 4) + binary if len(binary) % 4 != 0 else binary

    return binary
    
# octal
def octal_to_binary(x):
    binary = []
    
    # checking for radix
    if '.' in x:
        whole, frac = x.split('.')

        # conversion
        for i in whole:
            temp_whole = []

            while True:
                temp_whole.append('1' if int(i) % 2 != 0 else '0')

                i = int(i) // 2
                if int(i) == 0:
                    temp_whole.reverse()
                    temp_whole = ''.join(temp_whole)
                    temp_whole = temp_whole.zfill(3)
                    binary.append(temp_whole)
                    break

        binary.append('.')

        for i in frac:
            temp_frac = []

            while True:
                temp_frac.append('1' if int(i) % 2 != 0 else '0')

                i = int(i) // 2
                if int(i) == 0:
                    temp_frac.reverse()
                    temp_frac = ''.join(temp_frac)
                    temp_frac = temp_frac.zfill(3)
                    binary.append(temp_frac)
                    break

    # conversion without radix
    else:
        for i in x:
            temp = []
            while True:
                temp.append('1' if int(i) % 2 != 0 else '0')

                i = int(i) // 2
                if int(i) == 0:
                    temp.reverse()
                    temp = ''.join(temp)
                    temp = temp.zfill(3)
                    binary.append(temp)
                    break
    
    binary = ''.join(binary)
    return binary

# hexa
def hexa_to_binary(x):
    binary = []

    # hex mapping
    x = list(x)
    hex_mapping = {'1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9',
                   'A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'15',
                   'a':'10', 'b':'11', 'c':'12', 'd':'13', 'e':'14', 'f':'15'}

    for i in x:
        if i == '.' or i == '0':
            continue

        elif isinstance(i, str): 
            x[x.index(i)] = hex_mapping[i]
    
    # checking for radix
    if '.' in x:
        whole = x[:x.index('.')]
        frac = x[x.index('.')+1:]

        # conversion
        for i in whole:
            temp_whole = []

            while True:
                temp_whole.append('1' if int(i) % 2 != 0 else '0')

                i = int(i) // 2
                if int(i) == 0:
                    temp_whole.reverse()
                    temp_whole = ''.join(temp_whole)
                    temp_whole = temp_whole.zfill(4)
                    binary.append(temp_whole)
                    break

        binary.append('.')

        for i in frac:
            temp_frac = []

            while True:
                temp_frac.append('1' if int(i) % 2 != 0 else '0')

                i = int(i) // 2
                if int(i) == 0:
                    temp_frac.reverse()
                    temp_frac = ''.join(temp_frac)
                    temp_frac = temp_frac.zfill(4)
                    binary.append(temp_frac)
                    break

    # conversion without radix
    else:
        for i in x:
            temp = []
            while True:
                temp.append('1' if int(i) % 2 != 0 else '0')
                i = int(i) // 2
                if int(i) == 0:
                    temp.reverse()
                    temp = ''.join(temp)
                    temp = temp.zfill(4)
                    binary.append(temp)
                    break
    
    binary = ''.join(binary)
    return binary