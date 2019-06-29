print('''
********************************

Bankamıza Hoşgeldiniz!

Lütfen Yapmak İstediğiniz İşlemi Listeden Seçiniz!

Çıkmak İçin q'ya Basın...

*********************************
''')
TC = 0000000000000
Müşteri_No = 0000000

while True:
    islem = input('''
    1: TC Kimlik No İle Sıra Alma
    2: Müşteri No İle Sıra Alma
    3: Gişe İşlemleri

Lütfen Yapmak İstediğiniz İşlemi Seçiniz:
    ''')

    if (islem == "q"):
        print("Tekrar Bekleriz! ")
        break


    elif (islem == "1"):
        tc = int(input("Lütfen TC Kimlik Numaranızı Giriniz: "))
        print("İşlem Sıranız: Fis{}".format(TC))


    elif (islem == "2"):
        m_no =int(input("Lütfen Müşteri Numaranızı Giriniz: "))
        print("İşlem Sıranız: {}".format(Müşteri_No))


    elif (islem == "3"):
        print('''
        Lütfen Yapacağınız İşlemi Seçiniz:
        
        1: Bireysel Hesap Açma
        2: Vadeli Hesap Açma
        3: Fatura Yatırma
        4: Vergi Ödemesi
        5: Kira Ödemesi
        6: Eğitim Ödemesi
        7: Üniversite Harç Parası
        8: Diğer İşlemler
        ''')

    else:
        print("Geçersiz İşlem! Tekrar Deneyiniz!")

