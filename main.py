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

    options = ["Division", "Multiplication", "Subtraction", "Addition", "Negative (2's Complement)"]

    if select == '6':
        main_menu()

    if int(select) >= 1 and int(select) <= 4:
        os.system('cls')
        print(f"Binary {options[int(select)-1]}\n[1] Signed Binary\n[2] Unsigned Binary")
        option = input("Choose an option: ")

        if option == '1':
            os.system('cls')
            print(f"Binary {options[int(select)-1]} (Signed)")

            if select == '1':
                pass

            elif select == '2':
                pass

            elif select == '3':
                pass

            elif select == '4':
                pass

        elif option == '2':
            os.system('cls')
            print(f"Binary {options[int(select)-1]} (Unsigned)")

            if select == '1':
                binary1 = input("Input Binary 1: ")
                binary2 = input("Input Binary 2: ")
                quotient = menu2.division_unsigned(binary1, binary2)
                quotient_binary = menu3.decimal_to_binary(quotient)

                print(f"\n{binary1} / {binary2} = {quotient_binary}")

            elif select == '2':
                binary1 = input("Input Binary 1: ")
                binary2 = input("Input Binary 2: ")
                product = menu2.multiplication_unsigned(binary1, binary2)
                product_binary = menu3.decimal_to_binary(product)

                print(f"\n{binary1} * {binary2} = {product_binary}")

            elif select == '3':
                binary1 = input("Input Binary 1: ")
                binary2 = input("Input Binary 2: ")
                difference = menu2.subtraction_unsigned(binary1, binary2)
                difference_binary = menu3.decimal_to_binary(difference)

                print(f"\n{binary1} - {binary2} = {difference_binary}")

            elif select == '4':
                binary1 = input("Input Binary 1: ")
                binary2 = input("Input Binary 2: ")
                sum = menu2.addition_unsigned(binary1, binary2)
                sum_binary = menu3.decimal_to_binary(sum)

                print(f"\n{binary1} + {binary2} = {sum_binary}")

    elif select == '5':
        os.system('cls')
        print(f"{options[int(select)-1]}")
        binary = input("Input Binary: ")
        menu2.negative_unsigned(binary)

    input('Press Enter to continue...')

# Menu-3 (Conversion)
def conversion():
    os.system('cls')
    print("Conversion\n[1] Binary to X\n[2] Decimal to X\n[3] Octal to X\n[4] Hexa to X\n[5] Back")
    select = input("Choose an option: ")

    options = ["Binary", "Decimal", "Octal", "Hexa"]
    
    if select == '5':
        main_menu()

    if select:
        os.system('cls')
        print(f"{options[int(select)-1]} to X\n")

        x = input(f"Input {options[int(select)-1]}: ")

        if select == '1':
            decimal = menu3.binary_to_decimal(x)
            hexa = menu3.binary_to_hexa(x)
            octal = menu3.binary_to_octal(x)

            print(f"Output:\n\nDecimal: {decimal}\nHexa: {hexa}\nOctal: {octal}")

        elif select == '2':
            binary = menu3.decimal_to_binary(x)
            hexa = menu3.binary_to_hexa(binary)
            octal = menu3.binary_to_octal(binary)

            print(f"Output:\n\nBinary: {binary}\nHexa: {hexa}\nOctal: {octal}")

        elif select == '3':
            binary = menu3.octal_to_binary(x)
            decimal = menu3.binary_to_decimal(binary)
            hexa = menu3.binary_to_hexa(binary)

            print(f"Output:\n\nBinary: {binary}\nDecimal: {decimal}\nHexa: {hexa}")

        elif select == '4':
            binary = menu3.hexa_to_binary(x)
            decimal = menu3.binary_to_decimal(binary)
            octal = menu3.binary_to_octal(binary)

            print(f"Output:\n\nBinary: {binary}\nDecimal: {decimal}\nOctal: {octal}")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()