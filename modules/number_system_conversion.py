def binary(x):
    # Binary to Decimal
    decimal = 0

    if '.' in x:
        whole = x[:x.index('.')]
        frac = x[x.index('.')+1:]

        for i in range(len(whole)-1, -1, -1):
            decimal += int(whole[i]) * (2**(len(whole)-1-i))

        for i in range(1, len(frac)+1):
            decimal += int(frac[i-1]) * (2**(-i))

    else:
        for i in range(len(x)-1, -1, -1):
            decimal += int(x[i]) * (2**(len(x)-1-i))

    # Binary to Hexa
    hexa = 0
            
    # Binary to Octal
    octal = 0
    
    print(f"\nDecimal: {decimal}\nHexa: {hexa}\nOctal: {octal}")
    

def decimal(x):
    pass

def octal(x):
    pass

def hexa(x):
    pass