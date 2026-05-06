# Efsane Mangala - BGT 132 Final Projesi

Bu proje, Türk kültürünün önemli bir parçası olan Mangala oyununun Python ve Tkinter kütüphanesi kullanılarak geliştirilmiş dijital bir versiyonudur. Yazılım Geliştirme Teknolojileri dersi final gereksinimlerini karşılamak üzere tasarlanmıştır.

## 🚀 Proje Amacı
Geleneksel Mangala kurallarını modern yazılım prensipleriyle (OOP) birleştirerek, hatasız ve modüler bir oyun deneyimi sunmak.

## 🛠️ Kullanılan Teknolojiler
- **Dil:** Python 3.x
- **Arayüz:** Tkinter
- **Veri Yönetimi:** JSON (Skor kayıtları için)
- **Versiyon Kontrol:** Git

## 📂 Klasör Yapısı
- **docs/**: Gereksinim analizi ve UML diyagramları.
- **src/**: Kaynak kodlar (Core, UI, Models, Services, Utils).
- **assets/**: Ses ve görsel dosyalar.
- **data/**: Oyun skorlarının tutulduğu JSON dosyası.
- **tests/**: Mantıksal test dosyaları.

## 💻 Kurulum ve Çalıştırma
1. Python'un sisteminizde yüklü olduğundan emin olun.
2. Proje ana klasöründe terminali açın.
3. Aşağıdaki komutu çalıştırın:
   ```bash
   python main.py
   ---

### 2. `docs/GereksinimAnalizi.pdf` (Word'e yapıştırıp PDF yap)
Hoca bu belgede projenin neyi, neden ve nasıl yaptığını görmek ister[cite: 7].

**GEREKSİNİM ANALİZİ DOKÜMANI**

**1. Projenin Tanımı:**
Geleneksel Mangala oyununun dijital platforma aktarılmasıdır. Oyun iki kişilik olup, strateji ve mantık yürütmeye dayalıdır.

**2. Fonksiyonel Gereksinimler:**
*   **Oyun Kuralları:** Başlangıç kuyusuna taş bırakma, rakibi çiftleme, boş kuyuya düşme ve hazine kuralı tam olarak işletilmelidir[cite: 3].
*   **Skor Yönetimi:** Oyun bitiminde skorlar `data/skorlar.json` dosyasına kalıcı olarak kaydedilmelidir[cite: 7].
*   **Hata Yönetimi:** Geçersiz hamlelerde (rakip kuyusuna tıklama vb.) kullanıcı uyarılmalıdır[cite: 5].

**3. Fonksiyonel Olmayan Gereksinimler:**
*   **Performans:** Hamleler anlık olarak arayüze yansımalıdır.
*   **Güvenilirlik:** Program beklenmedik kullanıcı girişlerinde çökmemeli (try-except blokları)[cite: 6, 7].
*   **Modülerlik:** Kodlar; motor, arayüz ve servisler olarak ayrı klasörlerde tutulmalıdır[cite: 7].

---

### 3. `docs/UML_Diyagramlari.pdf` (Çizim Rehberi)
Hocan en az 1 Use Case ve 1 Class Diagram istiyor[cite: 7]. Bunları bir online araçla (draw.io gibi) çizip PDF yapmalısın.

**A. Use Case (Kullanım Durumu) Diyagramı:**
*   **Aktör:** Oyuncu.
*   **İşlemler (Daireler):** "Hamle Yap", "Skorları Görüntüle", "Oyun Kurallarını Uygula".
*   **Oklar:** Oyuncudan bu işlemlere ok çekmelisin.

**B. Class (Sınıf) Diyagramı:**
*   **MangalaMotoru:** Kuyuları ve hamleleri yönetir[cite: 3].
*   **Kuyu ve HazineKuyusu:** Kalıtım ilişkisini gösterir (HazineKuyusu, Kuyu'dan miras alır)[cite: 4].
*   **SkorServisi:** JSON dosyasına veri yazar[cite: 7].
*   **MangalaArayuz:** Kullanıcı ile etkileşime geçer[cite: 5].

---

**Son Kontrol:**
1.  `README.md` dosyasını ana dizine koydun mu?
2.  `docs/` klasörüne bu iki PDF'i ekledin mi?
3.  `src/services/skor_servisi.py` içine yazdığımız kod duruyor mu?

Eğer bunlar tamamsa, Git ve GitHub kısmına geçmeye hazır mısın? Yoksa bu belgelerin içeriğiyle ilgili sormak istediğin bir şey var mı?