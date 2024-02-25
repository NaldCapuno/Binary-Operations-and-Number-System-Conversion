import os
from modules import binary_operations as menu2
from modules import number_system_conversion as menu3

# Menu-1 (Main Menu)
def main_menu():
    while True:
        os.system('cls')
        print("[1] Binary Operations\n[2] Number System Conversion\n[3] Exit")
        select = input("Choose an option: ")

        if select == '1':
            binary_operations()
        
        elif select == '2':
            conversion()

        elif select == '3':
            break

# Menu-2 (Binary Operations)
def binary_operations():
    os.system('cls')
    print("Binary Operations\n[1] Division\n[2] Multiplication\n[3] Subtraction\n[4] Addition\n[5] Negative (2's Complement)\n[6] Back")
    select = input("Choose an option: ")

    operations = ["Division", "Multiplication", "Subtraction", "Addition", "Negative (2's Complement)"]

    if select == '6':
        main_menu()

    if int(select) >= 1 and int(select) <= 4:
        os.system('cls')
        print(f"Binary {operations[int(select)-1]}\n[1] Signed Binary\n[2] Unsigned Binary")
        option = input("Choose an option: ")

        sign = ["Signed", "Unsigned"]

        if option:
            os.system('cls')
            print(f"Binary {operations[int(select)-1]} ({sign[int(option)-1]})")

            binary1 = input("Input Binary 1: ")
            binary2 = input("Input Binary 2: ")

            if select == '1':
                if option == '1':
                    quotient = menu2.operations(binary1, binary2, select, option)
                    quotient_binary = menu3.decimal_to_binary(str(quotient))

                    if '-' in str(quotient):
                        quotient_binary = '1111 ' + menu2.twos_complement(quotient_binary)

                    else:
                        quotient_binary = '0000 ' + quotient_binary
                
                elif option == '2':
                    quotient = menu2.operations(binary1, binary2, select, option)
                    quotient_binary = menu3.decimal_to_binary(str(quotient))

                print(f"\n{binary1} / {binary2} = {quotient_binary}")

            elif select == '2':
                if option == '1':
                    product = menu2.operations(binary1, binary2, select, option)
                    product_binary = menu3.decimal_to_binary(str(product))

                    if '-' in str(product):
                        product_binary = '1111 ' + menu2.twos_complement(product_binary)

                    else:
                        product_binary = '0000 ' + product_binary

                elif option == '2':
                    product = menu2.operations(binary1, binary2, select, option)
                    product_binary = menu3.decimal_to_binary(str(product))

                print(f"\n{binary1} * {binary2} = {product_binary}")

            elif select == '3':
                if option == '1':
                    difference = menu2.operations(binary1, binary2, select, option)
                    difference_binary = menu3.decimal_to_binary(str(difference))

                    if '-' in str(difference):
                        difference_binary = '1111 ' + menu2.twos_complement(difference_binary)

                    else:
                        difference_binary = '0000 ' + difference_binary

                elif option == '2':
                    difference = menu2.operations(binary1, binary2, select, option)
                    difference_binary = menu3.decimal_to_binary(str(difference))

                print(f"\n{binary1} - {binary2} = {difference_binary}")

            elif select == '4':
                if option == '1':
                    sum = menu2.operations(binary1, binary2, select, option)
                    sum_binary = menu3.decimal_to_binary(str(sum))

                    if '-' in str(sum):
                        sum_binary = '1111 ' + menu2.twos_complement(sum_binary)

                    else:
                        sum_binary = '0000 ' + sum_binary
                    
                elif option == '2':
                    sum = menu2.operations(binary1, binary2, select, option)
                    sum_binary = menu3.decimal_to_binary(str(sum))

                print(f"\n{binary1} + {binary2} = {sum_binary}")

    elif select == '5':
        os.system('cls')
        print(f"{operations[int(select)-1]}")
        binary = input("Input Binary: ")
        twos_complement = menu2.twos_complement(binary)

        print(f"\n{binary} = {twos_complement}")

    input('Press Enter to continue...')

# Menu-3 (Conversion)
def conversion():
    os.system('cls')
    print("Conversion\n[1] Binary to X\n[2] Decimal to X\n[3] Octal to X\n[4] Hexa to X\n[5] Back")
    select = input("Choose an option: ")

    conversions = ["Binary", "Decimal", "Octal", "Hexa"]
    
    if select == '5':
        main_menu()

    if select:
        os.system('cls')
        print(f"Number System Conversion\n[1] Signed Binary\n[2] Unsigned Binary")
        option = input("Choose an option: ")

        sign = ["Signed", "Unsigned"]

        if option:
            os.system('cls')
            print(f"{conversions[int(select)-1]} Conversion ({sign[int(option)-1]})")

            x = input(f"Input {conversions[int(select)-1]}: ")

            if select == '1':
                decimal = menu3.binary_to_decimal(x, option)
                hexa = menu3.binary_to_hexa(x, option)
                octal = menu3.binary_to_octal(x, option)

                print(f"Output:\n\nDecimal: {decimal}\nHexa: {hexa}\nOctal: {octal}")

            elif select == '2':
                binary = menu3.decimal_to_binary(x)
                if '-' in x and option == '1':
                    binary = menu2.twos_complement(binary)
                hexa = menu3.binary_to_hexa(binary, option)
                octal = menu3.binary_to_octal(binary, option)

                print(f"Output:\n\nBinary: {binary}\nHexa: {hexa}\nOctal: {octal}")

            elif select == '3':
                binary = menu3.octal_to_binary(x)
                decimal = menu3.binary_to_decimal(binary, option)
                hexa = menu3.binary_to_hexa(binary, option)

                print(f"Output:\n\nBinary: {binary}\nDecimal: {decimal}\nHexa: {hexa}")

            elif select == '4':
                binary = menu3.hexa_to_binary(x)
                decimal = menu3.binary_to_decimal(binary, option)
                octal = menu3.binary_to_octal(binary, option)

                print(f"Output:\n\nBinary: {binary}\nDecimal: {decimal}\nOctal: {octal}")

    input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()