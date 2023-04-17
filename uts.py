class Atm:
    print('nama     :Muniri')
    print('npm      :2021020200041')

    print('prodi    :Sistem informasi')
    print('angkatan :21')
    print('kelas    :B')
    print('')
    print('==== SELAMAT DATANG DI ATM BARENG SAYA ====')
    print('')
    def __init__(self):
        self.pin = 123
        self.saldo = 500000
        self.menu()
    def menu(self):
        print("""
            apa yang anda ingin lakukan!
                1. cek saldo
                2. tarik saldo
                3. setor tunai
                    """)
        option = int(input("Masukkan pilihan anda: "))
        if option == 1:
            self.Cek_saldo()
        elif option == 2:
            self.Tarik_saldo()
        elif option == 3:
            self.Setor_tunai()

    def Cek_saldo(self):
        input_pin = int(input("Masukkan pin anda: "))
        if input_pin == self.pin:
           print("*" * 50)
           print(f"Saldo anda adalah {self.saldo}")
           print("*" * 50)
        else:
            print("Pin yang anda masukkan salah")
        self.menu()

    def Tarik_saldo(self):
        input_pin = int(input("Masukkan pin anda: "))
        if input_pin == self.pin:
            input_saldo = int(input("Masukkan jumlah penarikan anda: "))
            if input_saldo <= self.saldo:
                self.saldo = self.saldo - input_saldo
                print("*" * 50)
                print(f"Sisa saldo anda adalah {self.saldo}")
                print("*" * 50)
            else:
                print("Anda tidak memiliki banyak saldo!")
        else:
            print("Pin yang anda masukkan salah!")
        self.menu()

    def Setor_tunai(self):
        input_pin = int(input("Masukkan pin anda: "))
        if input_pin == self.pin:
            input_setor_tunai = int(input("Masukkan jumlah setoran anda: "))
            self.saldo = self.saldo + input_setor_tunai
            print("*" * 50)
            print(f"Sisa saldo anda adalah {self.saldo}")
            print("*" * 50)
        else:
            print("Pin yang anda masukkan salah!")
        
    def tarik_tunai(self):
        input.pin = int(input("masukan pin anda: "))
        if input_setor_tunai == self.pin:
            input_setor_tunai = int(input("Masukkan jumlah setoran anda: "))
            self.saldo = self.saldo + input_setor_tunai
            print("*" * 50)
            print(f"Sisa saldo anda adalah {self.saldo}")
            print("*" * 50)
        else:
             print("pin yang anda masukan salah!")  

sbi = Atm()
