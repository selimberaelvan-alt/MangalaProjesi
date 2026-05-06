# Projenin ana mantığını içeren MangalaMotoru sınıfını test etmek üzere içe aktarıyoruz.
from src.core.oyun_motoru import MangalaMotoru 

def test_oyun_baslangic():
    """
    Oyunun başlangıç kurulumunun Mangala standartlarına uygunluğunu test eder.
    """
    # Test için taze bir MangalaMotoru nesnesi (instance) oluşturuyoruz.
    motor = MangalaMotoru() 
    
    # KURAL: Oyun başında her kuyuda (0. kuyu dahil) tam 4 taş bulunmalıdır.
    # assert komutu, belirtilen şart sağlanmazsa hata fırlatarak testi durdurur.
    assert motor.tahta[0] == 4 
    
    # KURAL: 6. indis Oyuncu 1'in hazinesidir ve oyun başında boş (0) olmalıdır.
    assert motor.tahta[6] == 0 
    
    # Eğer yukarıdaki assert komutları hata vermezse testin geçtiğini konsola yazar.
    print("Başlangıç testi başarılı!")

def test_hamle_gecerliligi():
    """
    Oyun sırası kurallarının ve kuyu sahipliği güvenliğinin doğruluğunu test eder.
    Hocanın istediği 'Kullanıcı hatalarına karşı kontrol' gereksinimini denetler.
    """
    # Test için yeni bir oyun motoru başlatıyoruz (Sıra varsayılan olarak P1'dedir).
    motor = MangalaMotoru() 
    
    # GÜVENLİK TESTİ: Oyuncu 1, rakibi olan Oyuncu 2'nin kuyusuna (7. indis) müdahale edemez.
    # hamle_onayla fonksiyonunun burada 'False' döndürmesi beklenir.
    assert motor.hamle_onayla(7) == False
    
    # DOĞRULAMA TESTİ: Oyuncu 1, kendi bölgesindeki (0. indis) kuyuya hamle yapabilmelidir.
    # Fonksiyonun bu durumda 'True' döndürmesi gerekir.
    assert motor.hamle_onayla(0) == True
    
    # Tüm mantıksal sınamalar geçerse konsola bilgi mesajı basar.
    print("Hamle onay testi başarılı!")

if __name__ == "__main__":
    # Python dosyası doğrudan çalıştırıldığında test fonksiyonlarını sırayla tetikler.
    test_oyun_baslangic()
    test_hamle_gecerliligi()