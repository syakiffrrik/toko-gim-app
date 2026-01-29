import random
import main

def start():
    while True:
        bentuk_goa = "|O|"

        goa_kosong = [bentuk_goa] * 4      #ini tetep harus kosong

        cuypy = random.randint(1, 4)

        goa = goa_kosong.copy()            #ini untuk si cuypy
        goa[cuypy - 1] = "|O_O|"

        goa_kosong = ' '.join(goa_kosong)
        goa = ' '.join(goa)
        
        print(f'Coba perhatikan goa di bawah ini \n\n{goa_kosong}\n')

        pilihan_user = int(input('Dari empat Goa di atas, menurut kamu si CUYPY berada dimana? [1 / 2 / 3 / 4]: '))
    #error
        # if pilihan_user not in ['0', '1', '2', '3', '4']:
        #     pilihan_user = input('Pilihannya cuma 1 sampai 4 bro, gausah nambah-nambah yang lain, lanjut nih pilih goa ke berapa: ')

        if pilihan_user == cuypy:
            print(f'\n{goa}\n\nNah lu menang bro!!')
        else:
            print(f'\n{goa}\n\nBatu lu bro, kalah lu.. liat noh CUYPY nya ada dimana')

        play_again = input("\n\nlu bakal lanjut main ini game gak bro? [y/n]: ")
        if play_again == "n":
            main.menu()
            break


if __name__ == '__main__':
    start()