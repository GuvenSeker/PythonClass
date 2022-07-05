class Insan:
    def __init__(self, ad="Mahmut", soyad="Tuncer", yas=0, ulke="Turkiye", sehir="Izmir"):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return self.ad, self.soyad, self.yas, self.ulke, self.sehir, self.yetenekler

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)

        return self


gs = Insan("Güven", "Şeker", 34, "Türkiye", "İzmir")
gs.yetenek_ekle("python inş")
gs.yetenek_ekle("age of")
print(gs.kisi_bilgileri())
