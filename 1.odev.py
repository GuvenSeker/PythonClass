class Ogrenci:
    def __init__(self, ogrenci_adi, ogrenci_soyadi, ogrenci_sinif):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadi = ogrenci_soyadi
        self.ogrenci_sinif = ogrenci_sinif


class Soru(Ogrenci):
    def net_sayisi(self, dogru_sayisi, yanlis_sayisi):
        net = dogru_sayisi - (yanlis_sayisi // 4)

        print("net sayisi :", net)

        return self.hesapla(net)

    def hesapla(self, net_sayisi):
        print("Öğrenci adı : {}\nÖğrenci soyadı : {}\nÖğrencinin sınıfı {}\nOgrenci puani : {}".format
              (self.ogrenci_adi, self.ogrenci_soyadi, self.ogrenci_sinif, net_sayisi * 2))


gs = Ogrenci("guven", "seker", 3)
dogru_sayisi = int(input("dogru sayisini giriniz: "))
yanlis_sayisi = int(input("yanlis sayisini giriniz :"))

if dogru_sayisi + yanlis_sayisi == 50:
    Soru(gs.ogrenci_adi, gs.ogrenci_soyadi, gs.ogrenci_sinif).net_sayisi(dogru_sayisi, yanlis_sayisi)
else:
    print("Hatalı soru adeti girdiniz programdan çıkış yapılıyor!..")
