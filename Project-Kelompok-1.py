import os

# Fungsi untuk membersihkan layar konsol
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

sb = 50
uang_saya = 200000

# Mengecek jika file penyimpanan sudah ada, kemudian membaca nilai uang_saya jika ada
file_path = 'saldo.txt'
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        uang_saya = int(file.read())

while True:
    clear_screen()
    print('SELAMAT DATANG DI ATM'.center(sb))
    print('PILIH OPTION')
    print('1. CHECK UANG SAYA')
    print('2. AMBIL UANG SAYA')
    print('3. TABUNG UANG SAYA')

    option = int(input('SILAHKAN PILIH OPTION: '))

    if option == 1:
        clear_screen()
        print(f'UANG KAMU BERJUMLAH Rp.{uang_saya}')
        confirm = input('Apakah anda ingin melanjutkan [y/n]: ')
        if confirm.lower() != 'y':
            break
    elif option == 2:
        clear_screen()
        while True:
            if uang_saya != 0:
                print(f'UANG SAYA BERJUMLAH Rp.{uang_saya}, MAU AMBIL BERAPA?')
                print('1. Rp.50.000')
                print('2. Rp.100.000')
                option2 = int(input('option: '))

                if option2 == 1 or option2 == 2:
                    jumlah_penarikan = int(input(f'MASUKKAN JUMLAH UANG {option2 * 50000} YANG INGIN ANDA TARIK: '))
                    if jumlah_penarikan % (option2 * 50000) == 0:
                        if uang_saya >= jumlah_penarikan:
                            uang_saya -= jumlah_penarikan
                            with open(file_path, 'w') as file:
                                file.write(str(uang_saya))
                            print(f'BERHASIL MENARIK Rp.{jumlah_penarikan}')
                            print(f'UANG KAMU SEKARANG BERJUMLAH Rp.{uang_saya}')
                            
                            # Tambahkan pengecekan untuk melanjutkan penarikan
                            continue_with_withdrawal = input('Apakah anda ingin melanjutkan penarikan? [y/n]: ')
                            if continue_with_withdrawal.lower() != 'y':
                                break  # Keluar dari loop penarikan
                        else:
                            print('MAAF, SALDO TIDAK CUKUP')
                    else:
                        print(f'MAAF, PENARIKAN HARUS LEBIH DARI Rp.{option2 * 50000} DAN KELIPATAN {option2 * 50000}')
                else: 
                    print('Pilihan tidak valid!')
                    confirm = input('Apakah anda ingin melanjutkan [y/n]: ')
                    if confirm.lower() != 'y':
                        break
            else:
                print('MAAF, SALDO ANDA SUDAH KOSONG')
                confirm = input('Apakah anda ingin melanjutkan [y/n]: ')
                if confirm.lower() != 'y':
                    break
    elif option == 3:
        clear_screen()
        print(f'UANG SAYA BERJUMLAH Rp.{uang_saya}, MAU TABUNG BERAPA?')
        option3 = input('MASUKKAN JUMLAH UANG : ')

        if option3.isdigit() and int(option3) > 0: 
            uang_saya += int(option3)
            with open(file_path, 'w') as file:
                file.write(str(uang_saya))
            print(f'BERHASIL MENABUNG Rp.{option3}')
            print(f'JUMLAH UANG KAMU SEKARANG ADALAH Rp.{uang_saya}')
            confirm = input('Apakah anda ingin melanjutkan [y/n]: ')
            if confirm.lower() != 'y':
                break
        else:
            print('MAAF, INPUT HARUS ANGKA POSITIF')
            confirm = input('Apakah anda ingin melanjutkan [y/n]: ')
            if confirm.lower() != 'y':
                break
    else:
        print('OPTION TIDAK VALID')
        confirm = input('Apakah anda ingin melanjutkan [y/n]: ')
        if confirm.lower() != 'y':
            break
