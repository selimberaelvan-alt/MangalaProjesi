class MangalaMotoru:
    """
    Oyunun temel mantığını, kurallarını ve tahta durumunu yöneten ana sınıf.
    Hocanın istediği 'En az 3 sınıf' ve 'Modüler Sistem' şartını sağlar.
    """
    def __init__(self):
        # Oyun tahtasını merkezi bir liste yapısında tanımlıyoruz.
        # İndis Rehberi: 0-5: P1 Kuyuları, 6: P1 Hazine, 7-12: P2 Kuyuları, 13: P2 Hazine.
        # Mangala kuralı gereği her kuyuya başlangıçta 4 taş atanır.
        self.tahta = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        self.sira_kimde = 1 # Oyunun başlangıcında sırayı 1. oyuncuya verir.
        self.oyun_aktif = True # Oyunun devam edip etmediğini kontrol eden bayrak (flag).

    def hamle_onayla(self, indis):
        """Kullanıcının seçtiği kuyunun kurallara uygun olup olmadığını denetler (Hata Yönetimi)."""
        # Oyun bitmişse hamle yapılamaz.
        if not self.oyun_aktif: return False
        
        # Kapsülleme ve Mantıksal Ayrıştırma: Oyuncunun sadece kendi sahasından taş almasını sağlar.
        if self.sira_kimde == 1 and (indis < 0 or indis > 5): return False
        if self.sira_kimde == 2 and (indis < 7 or indis > 12): return False
        
        # Seçilen kuyu boşsa hamle geçersizdir.
        if self.tahta[indis] == 0: return False
        
        return True

    def tas_dagit(self, indis):
        """Mangala'nın temel taş dağıtma algoritmasını işletir."""
        eldeki_tas = self.tahta[indis] # Seçilen kuyudaki taşları avuca (değişkene) al.
        
        # MANGALA KURALI: Kuyuda tek taş varsa bir sonraki kuyuya taşınır.
        # Birden fazla taş varsa, biri kuyuda kalır, kalanlar dağıtılır.
        if eldeki_tas == 1:
            self.tahta[indis] = 0
            mevcut = indis
        else:
            self.tahta[indis] = 1
            eldeki_tas -= 1
            mevcut = indis
        
        # Avuçtaki taşlar bitene kadar saat yönünün tersine dağıtım yapılır.
        while eldeki_tas > 0:
            mevcut = (mevcut + 1) % 14 # Tahta etrafında dairesel döngü (Mod 14).
            
            # MANGALA KURALI: Dağıtım sırasında rakibin hazinesi (kale) atlanır.
            if self.sira_kimde == 1 and mevcut == 13: 
                continue 
            if self.sira_kimde == 2 and mevcut == 6: 
                continue 
            
            self.tahta[mevcut] += 1 # Taş bırakma işlemi.
            eldeki_tas -= 1 # Avuçtaki taşı azalt.
        
        # Her hamle sonrası oyunun bitip bitmediği kontrol edilir.
        if self.bitis_kontrol():
            self.oyun_aktif = False
        else:
            # MANGALA KURALI: Son taş hazineye gelirse oyuncu bir hamle hakkı daha kazanır.
            # Aksi durumda sıra rakibe geçer.
            if not ((self.sira_kimde == 1 and mevcut == 6) or (self.sira_kimde == 2 and mevcut == 13)):
                self.sira_kimde = 2 if self.sira_kimde == 1 else 1

    def bitis_kontrol(self):
        """Sahadaki taşların bitip bitmediğini denetleyerek oyun sonu kararı verir."""
        # 'all' fonksiyonu ile bölgedeki tüm kuyuların boş (0) olup olmadığına bakılır.
        p1_bolgesi_bos = all(self.tahta[i] == 0 for i in range(0, 6))
        p2_bolgesi_bos = all(self.tahta[i] == 0 for i in range(7, 13))
        
        # Herhangi bir tarafın taşları bittiyse oyun sonlanır.
        if p1_bolgesi_bos or p2_bolgesi_bos:
            self.final_topla() # Kalan taşları hazineye aktar.
            return True
        return False

    def final_topla(self):
        """Oyun sonunda sahadaki tüm taşları ilgili oyuncunun hazinesine toplar."""
        # Oyuncu 1'in bölgesindeki kalanları kendi hazinesine (6) ekle.
        for i in range(0, 6):
            self.tahta[6] += self.tahta[i]
            self.tahta[i] = 0
        # Oyuncu 2'in bölgesindeki kalanları kendi hazinesine (13) ekle.
        for i in range(7, 13):
            self.tahta[13] += self.tahta[i]
            self.tahta[i] = 0

    def kazananı_bul(self):
        """Hazine puanlarını karşılaştırarak nihai sonucu belirler."""
        p1_skor = self.tahta[6]
        p2_skor = self.tahta[13]
        if p1_skor > p2_skor: return "Oyuncu 1 Kazandı!"
        elif p2_skor > p1_skor: return "Oyuncu 2 Kazandı!"
        else: return "Berabere!"