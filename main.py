import os
from modules import binary_operations as menu2
from modules import number_system_conversion as menu3

# Menu-1 (Main Menu)
def main_menu():
    while True:
        os.system('cls')
        print("[1] Binary Operations\n[2] Number System Conversion\n[3] Exit")
        select = int(input("Choose an option: "))

        if select == 1:
            binary_operations()
        
        elif select == 2:
            conversion()

        elif select == 3:
            break

# Menu-2 (Binary Operations)
def binary_operations():
    os.system('cls')
    print("Binary Operations\n[1] Division\n[2] Multiplication\n[3] Subtraction\n[4] Addition\n[5] Negative (2's Complement)\n[6] Back")
    select = int(input("Choose an option: "))

    if select == 1:
        menu2.division()

    elif select == 2:
        menu2.multiplication()

    elif select == 3:
        menu2.subtraction()

    elif select == 4:
        menu2.addition()

    elif select == 5:
        menu2.negative()

    elif select == 6:
        main_menu()

# Menu-3 (Conversion)
def conversion():
    os.system('cls')
    print("Conversion\n[1] Binary to X\n[2] Decimal to X\n[3] Octal to X\n[4] Hexa to X\n[5] Back")
    select = int(input("Choose an option: "))

    if select == 1:
        menu3.binary()

    elif select == 2:
        menu3.decimal()

    elif select == 3:
        menu3.octal()

    elif select == 4:
        menu3.hexa()
    
    elif select == 5:
        main_menu()

main_menu()