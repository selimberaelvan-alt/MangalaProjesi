class MangalaMotoru:
    def __init__(self):
        # Oyun tahtasını bir liste olarak tanımlıyoruz.
        # 0-5: P1 kuyuları, 6: P1 hazine, 7-12: P2 kuyuları, 13: P2 hazine.
        self.tahta = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        self.sira_kimde = 1 
        self.oyun_aktif = True 

    def hamle_onayla(self, indis):
        # Yanlış kuyu seçimlerini engeller.
        if not self.oyun_aktif: return False
        
        # Oyuncu sadece kendi tarafındaki kuyulardan taş alabilir.
        if self.sira_kimde == 1 and (indis < 0 or indis > 5): return False
        if self.sira_kimde == 2 and (indis < 7 or indis > 12): return False
        
        # Seçilen kuyu boşsa hamle yapılamaz.
        if self.tahta[indis] == 0: return False
        
        return True

    def tas_dagit(self, indis):
        # Taşları kurallara uygun şekilde dağıtma mekanizması.
        eldeki_tas = self.tahta[indis] 
        
        # MANGALA KURALI: Eğer kuyuda 1 taş varsa bir sonrakine geçer.
        # Eğer birden fazla taş varsa, biri başlangıç kuyusunda kalır.
        if eldeki_tas == 1:
            self.tahta[indis] = 0
            mevcut = indis
        else:
            self.tahta[indis] = 1
            eldeki_tas -= 1
            mevcut = indis
        
        while eldeki_tas > 0:
            mevcut = (mevcut + 1) % 14
            
            # MANGALA KURALI: Oyuncu, rakibin hazinesine taş koyamaz.
            if self.sira_kimde == 1 and mevcut == 13: 
                continue 
            if self.sira_kimde == 2 and mevcut == 6: 
                continue 
            
            self.tahta[mevcut] += 1 
            eldeki_tas -= 1 
        
        # OYUN BİTİŞ KONTROLÜ
        if self.bitis_kontrol():
            self.oyun_aktif = False
        else:
            # MANGALA KURALI: Son taş hazineye gelirse sıra değişmez.
            if not ((self.sira_kimde == 1 and mevcut == 6) or (self.sira_kimde == 2 and mevcut == 13)):
                self.sira_kimde = 2 if self.sira_kimde == 1 else 1

    def bitis_kontrol(self):
        # Bölgelerin boş olup olmadığını kontrol eder.
        p1_bolgesi_bos = all(self.tahta[i] == 0 for i in range(0, 6))
        p2_bolgesi_bos = all(self.tahta[i] == 0 for i in range(7, 13))
        
        if p1_bolgesi_bos or p2_bolgesi_bos:
            self.final_topla()
            return True
        return False

    def final_topla(self):
        # Oyun bittiğinde sahadaki taşları hazineye aktarır.
        for i in range(0, 6):
            self.tahta[6] += self.tahta[i]
            self.tahta[i] = 0
        for i in range(7, 13):
            self.tahta[13] += self.tahta[i]
            self.tahta[i] = 0

    def kazananı_bul(self):
        p1_skor = self.tahta[6]
        p2_skor = self.tahta[13]
        if p1_skor > p2_skor: return "Oyuncu 1 Kazandı!"
        elif p2_skor > p1_skor: return "Oyuncu 2 Kazandı!"
        else: return "Berabere!"