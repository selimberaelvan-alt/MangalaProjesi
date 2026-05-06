import json
import os
from datetime import datetime

class SkorServisi:
    """
    Oyun skorlarını kalıcı olarak saklamak ve yönetmekten sorumlu servis katmanı.
    Hocanın istediği 'Modüler Sistem Tasarımı' gereği iş mantığı burada tutulur.
    """
    
    @staticmethod
    def skor_kaydet(p1_skor, p2_skor, kazanan):
        """Oyun sonuçlarını data/skorlar.json dosyasına güvenli bir şekilde kaydeder."""
        skor_dosyasi = os.path.join('data', 'skorlar.json')
        
        # Yeni oyun verisi
        yeni_skor = {
            "tarih": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "oyuncu1_skor": p1_skor,
            "oyuncu2_skor": p2_skor,
            "kazanan": kazanan
        }

        try:
            # Data klasörü yoksa oluştur (Hata yönetiminin bir parçası)
            if not os.path.exists('data'):
                os.makedirs('data')

            # Eğer dosya zaten varsa, eski verileri oku ve listeye ekle
            veriler = []
            if os.path.exists(skor_dosyasi):
                with open(skor_dosyasi, 'r', encoding='utf-8') as f:
                    try:
                        veriler = json.load(f)
                        if not isinstance(veriler, list): veriler = []
                    except json.JSONDecodeError:
                        veriler = []

            # Yeni skoru listeye ekle ve dosyayı güncelle
            veriler.append(yeni_skor)
            
            with open(skor_dosyasi, 'w', encoding='utf-8') as f:
                json.dump(veriler, f, ensure_ascii=False, indent=4)
            
            print("Skor başarıyla kaydedildi.")

        except Exception as e:
            # Hocanın istediği hata yönetimi (try-catch) yapısı
            print(f"Skor Servisi Hatası: Skor kaydedilirken bir sorun oluştu -> {e}")

    @staticmethod
    def en_yuksek_skoru_getir():
        """Geçmiş oyunlar arasındaki en yüksek skoru döndürür."""
        skor_dosyasi = os.path.join('data', 'skorlar.json')
        try:
            if os.path.exists(skor_dosyasi):
                with open(skor_dosyasi, 'r', encoding='utf-8') as f:
                    veriler = json.load(f)
                    # Tüm oyuncu skorlarını bir listeye topla ve en büyüğünü bul
                    tum_skorlar = [d["oyuncu1_skor"] for d in veriler] + [d["oyuncu2_skor"] for d in veriler]
                    return max(tum_skorlar) if tum_skorlar else 0
        except:
            return 0
        return 0