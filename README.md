# Efsane Mangala - BGT 132 Final Projesi

Bu proje, Türk kültürünün köklü strateji oyunlarından biri olan Mangala'nın Python ve Tkinter kullanılarak geliştirilmiş dijital bir versiyonudur. Yazılım Geliştirme Teknolojileri dersi final gereksinimlerini %100 karşılayacak şekilde, modüler bir yapıda ve Nesne Yönelimli Programlama (OOP) prensipleriyle tasarlanmıştır.

## 🎯 Proje Amacı
Projenin temel amacı, geleneksel bir oyunu modern yazılım geliştirme süreçlerine (Gereksinim Analizi, UML, Git Versiyonlama) uygun şekilde dijital ortama aktarmaktır. Kod yapısında OOP (Kalıtım, Kapsülleme) ve modüler mimari kullanılarak sürdürülebilir bir yazılım örneği sunulmuştur.

## 🛠️ Kullanılan Teknolojiler
- **Dil:** Python 3.x
- **Kütüphane:** Tkinter (GUI)
- **Veri Yönetimi:** JSON (Skor kayıtları için)
- **Versiyon Kontrol:** Git & GitHub

## 📂 Proje Klasör Yapısı (Görsel 1 Uyumlu)
Hocanın belirttiği standart klasör yapısı titizlikle uygulanmıştır:
- **docs/**: Gereksinim analizi ve UML diyagramları (PDF).
- **src/**: 
    - **core/**: Oyunun ana mantığı ve Mangala motoru.
    - **modules/**: Kuyu ve HazineKuyusu sınıf modelleri.
    - **services/**: Skor kayıt ve JSON işlemleri.
    - **ui/**: Tkinter arayüz dosyaları.
    - **utils/**: Yardımcı fonksiyonlar.
- **assets/**: Oyun içi görsel ve ses dosyaları.
- **data/**: `skorlar.json` ve örnek veri dosyaları.
- **tests/**: Mantıksal birim testleri.

## ⚙️ Nesne Yönelimli Programlama (OOP) Yapısı
Proje kapsamında puanlama kriterlerine uygun olarak şu yapılar kullanılmıştır:
- **En Az 3 Sınıf:** `Kuyu`, `HazineKuyusu`, `MangalaMotoru` ve `SkorServisi`.
- **Kalıtım (Inheritance):** `HazineKuyusu` sınıfı, `Kuyu` sınıfından miras alınarak türetilmiştir.
- **Kapsülleme (Encapsulation):** Taş sayıları ve kuyu durumları `private` değişkenlerle korunmuş, `getter/setter` metotları ile erişim sağlanmıştır.
- **Hata Yönetimi:** Dosya işlemleri ve kullanıcı hamleleri `try-except` blokları ile kontrol altına alınmıştır.

## 🚀 Kurulum ve Çalıştırma Talimatı

1. **Python Yüklemesi:** Bilgisayarınızda Python 3.x sürümünün yüklü olduğundan emin olun.
2. **Projeyi İndirme:** Bu repoyu klonlayın veya .zip olarak indirin.
3. **Bağımlılıklar:** Proje standart Python kütüphanelerini kullanmaktadır. Ek bir yükleme gerektirmez (Tkinter Python ile birlikte gelir).
4. **Çalıştırma:** Terminal veya Komut İstemi'ni açıp proje ana dizinine gidin ve şu komutu çalıştırın:
   ```bash
   python main.py