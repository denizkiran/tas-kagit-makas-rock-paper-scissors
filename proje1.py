import random


secenekler = ['Taş', 'Kağıt', 'Makas']

def sonucu_belirle(kullanici_secimi, bilgisayar_secimi):

    print(f"Sizin seçiminiz: {kullanici_secimi}")
    print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

    if kullanici_secimi == bilgisayar_secimi:
        print(f"Berabere! İkiniz de '{kullanici_secimi}' seçtiniz.")
    elif (kullanici_secimi == 'Taş' and bilgisayar_secimi == 'Makas') or \
         (kullanici_secimi == 'Kağıt' and bilgisayar_secimi == 'Taş') or \
         (kullanici_secimi == 'Makas' and bilgisayar_secimi == 'Kağıt'):
        print(f"Kazandınız! {kullanici_secimi}, {bilgisayar_secimi}'ı yener.")
    else:
        print(f"Kaybettiniz! {bilgisayar_secimi}, {kullanici_secimi}'ı yener.")

def ana_menu():

    secim_map = {'1': 'Taş', '2': 'Kağıt', '3': 'Makas'}

    while True:
        print("\n--- Taş Kağıt Makas Oyunu ---")
        print("Lütfen yapmak istediğiniz hamleyi seçiniz:")
        print("1. Taş")
        print("2. Kağıt")
        print("3. Makas")
        print("4. Oyunu kapat")
        secim = input("Seçiminizi giriniz: ")

        if secim in secim_map:
            kullanici_hamlesi = secim_map[secim]
            bilgisayar_hamlesi = random.choice(secenekler)
            sonucu_belirle(kullanici_hamlesi, bilgisayar_hamlesi)
        elif secim == '4':
            print("Oyun kapatılıyor...")
            break
        else:

            print("Geçersiz seçim yaptınız. Lütfen tekrar deneyiniz.")


ana_menu()
