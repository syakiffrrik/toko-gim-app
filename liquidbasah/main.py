# random adalah nama library nya
import random
from libs import welcome_message, exit_program
from libs import words
from games import pinguinkutub
from tools import warkop

def menu():
    user_option = int(input(f'Menu programnya:\n1. Games CUYPY\n2. Warung Mini\n3. Keluar\n\nSilahkan pilih: '))

    if user_option == 1:
        pinguinkutub.start()
    elif user_option == 2:
        warkop.start()
    elif user_option == 3:
        exit_program()
    else:
        print('Hanya bisa memilih yang sudah tersedia di menu!')
        
        exit_program()

def main():
    welcome_message()
    words()
    menu()

if __name__ == '__main__':
    main()