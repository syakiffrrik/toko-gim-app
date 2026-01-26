import main
from services import db

def add():
    kode_menu = input('kode menu: ')
    nama_menu = input('nama menu: ')
    harga_menu = int(input('harga barang: '))
    stok_menu = int(input('stok menu: '))
    
    db.insert_item(kode_menu, nama_menu, harga_menu, stok_menu)

def check():
    items = db.fetch_item()
    for item in items:
        kode_menu = item[1]
        nama_menu = item[2]
        harga_menu = item[3]
        stok_menu = item[4]
        print(f'''
Kode {kode_menu}
{nama_menu} | Rp{harga_menu}
Stok {stok_menu}
              ''')

def start():
    while True:
        menu = int(input('Menu:\n\n1. Tambah Menu\n2. Check Menu\n3. Kembali\n\nSilahkan pilih: '))
        
        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            main.menu()
        else:
            break
            
        # selesai = 'n'
        # play_again = 'y'
        # print('INI WARKOP TENGAH APPS')
        # menu_warung = ['Mie Pangsit','Kopi Item', 'Teh Anget', 'Gorengan']
        
        # for index in range(len(menu_warung)):
        #     no = index + 1
        #     print(f'{no} {menu_warung[index]}')
    
        # pesen = int(input(f'Silahkan pilih menu: '))
        # print(f'Pilihannya adalah: {menu_warung[pesen - 1]}')
        
        # selesai = input('Pesanan selesai? [y/n] ')
        # if selesai == 'n':
        #     print('Silahkan pilih menu lagi:\n')
        #     continue
        # elif selesai == 'y':
        #     print('Terimakasih sudah pesan di Warkop Tengah')
        # else:
        #     print('Input tidak dikenali, lanjut ke menu lagi:\n')
            
if __name__ == '__main__':
    start()