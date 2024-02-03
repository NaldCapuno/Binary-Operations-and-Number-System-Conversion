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

    if select:
        os.system('cls')
        print(f"Binary {options[int(select)-1]}\n[1] Signed Binary\n[2] Unsigned Binary")
        option = input("Choose an option: ")

        if option == '1':
            os.system('cls')
            print(f"Binary {options[int(select)-1]} (Signed)")

            binary1 = input("Enter Binary 1: ")
            binary2 = input("Enter Binary 2: ")

            if select == '1':
                menu2.division_signed(binary1, binary2)

            elif select == '2':
                menu2.multiplication_signed(binary1, binary2)

            elif select == '3':
                menu2.subtraction_signed(binary1, binary2)

            elif select == '4':
                menu2.addition_signed(binary1, binary2)

            elif select == '5':
                menu2.negative_signed(binary1, binary2)

        elif option == '2':
            os.system('cls')
            print(f"Binary {options[int(select)-1]} (Unsigned)")

            binary1 = input("Enter Binary 1: ")
            binary2 = input("Enter Binary 2: ")

            if select == '1':
                menu2.division_unsigned(binary1, binary2)

            elif select == '2':
                menu2.multiplication_unsigned(binary1, binary2)

            elif select == '3':
                menu2.subtraction_unsigned(binary1, binary2)

            elif select == '4':
                menu2.addition_unsigned(binary1, binary2)

            elif select == '5':
                menu2.negative_unsigned(binary1, binary2)

        input("\nPress Enter to continue...")

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
        print(f"{options[int(select)-1]} to X")

        x = input(f"Enter {options[int(select)-1]}: ")

        if select == '1':
            menu3.binary(x)

        elif select == '2':
            menu3.decimal(x)

        elif select == '3':
            menu3.octal(x)

        elif select == '4':
            menu3.hexa(x)

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()