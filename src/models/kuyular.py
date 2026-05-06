class Kuyu: # 'Kuyu' adında bir ana sınıf (base class) tanımlıyoruz.
    def __init__(self, sahip, tas_sayisi=4): 
        # __init__ yapıcı metodur. Nesne yaratıldığında çalışır.
        self.__tas_sayisi = tas_sayisi  
        # İki alt çizgi (__) bu değişkeni 'private' yapar. 
        # Buna ENCAPSULATION (Kapsülleme) denir. Veri güvenliğini sağlar.
        self.sahip = sahip # Kuyunun hangi oyuncuya ait olduğunu tutar.

    def get_tas(self): 
        # Private değişkene dışarıdan erişmek için kullanılan 'Getter' metodu.
        return self.__tas_sayisi

    def set_tas(self, miktar): 
        # Private değişkeni değiştirmek için kullanılan 'Setter' metodu.
        # Burada veri kontrolü yapabiliriz (miktar 0'dan küçük olamaz gibi).
        if miktar >= 0:
            self.__tas_sayisi = miktar

    def bilgi_ver(self):
        # Bu metod POLYMORPHISM için temel oluşturur.
        return f"Standart kuyu: {self.__tas_sayisi} taş var."

class HazineKuyusu(Kuyu): # KALITIM (Inheritance): HazineKuyusu sınıfı Kuyu'dan miras alır.
    def __init__(self, sahip):
        # super() kullanarak ana sınıfın yapıcı metodunu çağırıyoruz.
        # Hazine her zaman 0 taşla başladığı için tas_sayisi'nı 0 yolluyoruz.
        super().__init__(sahip, tas_sayisi=0)

    def bilgi_ver(self):
        # POLYMORPHISM (Çok Biçimlilik): Ana sınıftaki 'bilgi_ver' ismini 
        # burada eziyoruz (Override) ve hazineye özel bir mesaj yazdırıyoruz.
        return f"HAZİNE: Oyuncu {self.sahip} için skor alanı!"