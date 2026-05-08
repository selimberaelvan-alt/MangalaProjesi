import json # JSON formatındaki dosyalarla işlem yapabilmek için gerekli kütüphane.
import os # Bilgisayardaki dosya ve klasör yollarına erişmek için kullanılan kütüphane.
from datetime import datetime # Oyunun ne zaman oynandığını (tarih/saat) kaydetmek için gerekli modül.

class SkorServisi:
    """
    Oyun skorlarını kalıcı olarak saklamak ve yönetmekten sorumlu servis katmanı.
    Hocanın istediği 'Modüler Sistem Tasarımı' gereği iş mantığı burada tutulur.
    """
    
    @staticmethod # Bu metodu sınıfı örneklemeden (instance oluşturmadan) kullanabilmek için tanımladık.
    def skor_kaydet(p1_skor, p2_skor, kazanan):
        """Oyun sonuçlarını data/skorlar.json dosyasına güvenli bir şekilde kaydeder."""
        # Skorların kaydedileceği dosyanın yolunu 'data/skorlar.json' olarak belirliyoruz.
        skor_dosyasi = os.path.join('data', 'skorlar.json')
        
        # O ana ait tarih ve oyun sonuçlarını içeren bir sözlük (dictionary) yapısı oluşturuyoruz.
        yeni_skor = {
            "tarih": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # Tarihi okunabilir formatta alır.
            "oyuncu1_skor": p1_skor,
            "oyuncu2_skor": p2_skor,
            "kazanan": kazanan
        }

        try: # Hocanın istediği hata yönetimi (Hata oluşabilecek kod bloğu başlangıcı).
            # Eğer 'data' isimli klasör bilgisayarda yoksa, programın çökmemesi için otomatik oluşturur.
            if not os.path.exists('data'):
                os.makedirs('data')

            # Mevcut skorları korumak için önce dosyayı okumamız gerekiyor.
            veriler = [] # Verileri tutacağımız boş bir liste başlatıyoruz.
            if os.path.exists(skor_dosyasi): # Eğer dosya zaten varsa (eski oyunlar kaydedilmişse):
                with open(skor_dosyasi, 'r', encoding='utf-8') as f: # Dosyayı okuma modunda aç.
                    try:
                        veriler = json.load(f) # JSON içeriğini Python listesine dönüştür.
                        # Veri liste formatında değilse bozulma ihtimaline karşı listeye eşitle.
                        if not isinstance(veriler, list): veriler = []
                    except json.JSONDecodeError: # JSON dosyası bozuksa veya boşsa hata almamak için:
                        veriler = []

            # Az önce oluşturduğumuz 'yeni_skor' bilgisini mevcut listeye ekliyoruz.
            veriler.append(yeni_skor)
            
            # Güncellenmiş listeyi tekrar dosyaya yazıyoruz.
            with open(skor_dosyasi, 'w', encoding='utf-8') as f: # Yazma modunda aç.
                # ensure_ascii=False Türkçe karakterler için, indent=4 ise dosyanın okunabilir görünmesi içindir.
                json.dump(veriler, f, ensure_ascii=False, indent=4)
            
            print("Skor başarıyla kaydedildi.")

        except Exception as e: # Dosya yazma veya klasör erişimi gibi bir hata olursa burası çalışır.
            # Programın kapanması yerine hatayı ekrana basar (Hata Yönetimi).
            print(f"Skor Servisi Hatası: Skor kaydedilirken bir sorun oluştu -> {e}")

    @staticmethod
    def en_yuksek_skoru_getir():
        """Geçmiş oyunlar arasındaki en yüksek skoru döndürür."""
        skor_dosyasi = os.path.join('data', 'skorlar.json')
        try:
            if os.path.exists(skor_dosyasi): # Dosya var mı kontrol et.
                with open(skor_dosyasi, 'r', encoding='utf-8') as f:
                    veriler = json.load(f) # Verileri çek.
                    # List comprehension kullanarak tüm oyuncu puanlarını tek bir listede topluyoruz.
                    tum_skorlar = [d["oyuncu1_skor"] for d in veriler] + [d["oyuncu2_skor"] for d in veriler]
                    # Liste boş değilse en yüksek puanı döndür, boşsa 0 döndür.
                    return max(tum_skorlar) if tum_skorlar else 0
        except: # Okuma sırasında hata olursa sessizce 0 döndür.
            return 0
        return 0 # Dosya yoksa veya başka bir durum varsa varsayılan 0 döndür.