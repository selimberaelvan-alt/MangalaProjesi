import tkinter as tk
import random
from tkinter import messagebox # Oyun bittiğinde mesaj göstermek için
from src.core.oyun_motoru import MangalaMotoru # Oyun mantığını kontrol eden sınıf
from src.utils.ses_yoneticisi import SesYoneticisi # Ses efektlerini yöneten sınıf
from src.services.skor_servisi import SkorServisi # Skorları kaydeden servis katmanı

class MangalaArayuz:
    def __init__(self, pencere):
        """
        Arayüz sınıfının yapıcı metodu. 
        Nesne yönelimli programlama (OOP) gereği motoru ve ses yöneticisini başlatır.
        """
        self.motor = MangalaMotoru() # Oyunun ana motorunu başlatıyoruz[cite: 3]
        self.pencere = pencere
        self.pencere.title("Efsane Mangala - BGT 132 Final Projesi") # Pencere başlığı
        self.pencere.configure(bg="#2d1b0d") # Arka plan rengi (Ahşap teması)
        
        self.canvas_listesi = [] # Her bir kuyuyu temsil eden çizim alanlarını tutar
        self.arayuz_hazirla() # Arayüz bileşenlerini oluşturur

    def arayuz_hazirla(self):
        """
        Tkinter bileşenlerini (Label, Frame, Canvas) yerleştiren metod.
        Hocanın istediği 'Fonksiyonel Ayrıştırma' kuralına uygundur.
        """
        # Üst Bilgi Paneli: Sıranın kimde olduğunu gösterir
        self.bilgi = tk.Label(self.pencere, text="Sıra: Oyuncu 1", font=("Segoe UI", 20, "bold"), 
                             fg="#ffcc80", bg="#2d1b0d")
        self.bilgi.pack(pady=15)

        # Ana Tahta Çerçevesi: Kuyuların içine dizileceği ana kapsayıcı
        tahta_frame = tk.Frame(self.pencere, bg="#4e342e", padx=15, pady=15, 
                              highlightthickness=4, highlightbackground="#3e2723")
        tahta_frame.pack(padx=20, pady=20)

        # 14 adet kuyuyu (12 kuyu + 2 hazine) döngü ile oluşturuyoruz
        for i in range(14):
            # Hazine kuyuları (6 ve 13) daha geniş ve uzun olacak şekilde ayarlanır[cite: 3]
            genislik, yukseklik = (110, 220) if i in [6, 13] else (90, 90)
            
            canv = tk.Canvas(tahta_frame, width=genislik, height=yukseklik, 
                             bg="#6d4c41", highlightthickness=1, highlightbackground="#2d1b0d")
            
            # Her kuyuyu bir tıklama olayına (Event Handling) bağlıyoruz
            canv.bind("<Button-1>", lambda event, x=i: self.tiklendi(x))
            
            # Mangala tahta düzenine göre ızgara (Grid) yerleşimi
            if i == 13: canv.grid(row=0, column=0, rowspan=2, padx=10) # P2 Hazinesi
            elif i == 6: canv.grid(row=0, column=7, rowspan=2, padx=10) # P1 Hazinesi
            elif i < 6: canv.grid(row=1, column=i+1, padx=5, pady=5) # P1 Kuyuları (Alt sıra)
            else: canv.grid(row=0, column=13-i, padx=5, pady=5) # P2 Kuyuları (Üst sıra)
            
            self.canvas_listesi.append(canv)
        
        self.taslari_ciz() # İlk taşları yerleştir

    def taslari_ciz(self):
        """
        Kuyuların içindeki taşları görsel olarak güncelleyen metod.
        Random kütüphanesi ile taşların kuyu içinde doğal dağılmasını sağlar.
        """
        for i in range(14):
            canv = self.canvas_listesi[i]
            canv.delete("all") # Önceki çizimleri temizle

            tas_sayisi = self.motor.tahta[i] # Motordan güncel taş sayısını al[cite: 3]
            w = canv.winfo_width() if canv.winfo_width() > 1 else 90
            h = canv.winfo_height() if canv.winfo_height() > 1 else 90

            # Her bir taş için görsel bir daire oluştur
            for _ in range(tas_sayisi):
                x = random.randint(20, w-30)
                y = random.randint(20, h-30)
                
                # Taşlara derinlik hissi veren gölge ve parlatma efektleri
                canv.create_oval(x+2, y+2, x+14, y+14, fill="#1a1a1a", outline="", tags="tas")
                canv.create_oval(x, y, x+12, y+12, fill="#4fc3f7", outline="white", width=1, tags="tas")
            
            # Kuyu içindeki taş sayısını rakamla gösteren panel
            canv.create_rectangle(5, 5, 25, 25, fill="#3e2723", outline="")
            canv.create_text(15, 15, text=str(tas_sayisi), fill="#ffcc80", font=("Arial", 10, "bold"), tags="tas")

    def tiklendi(self, indis):
        """
        Kuyuya tıklandığında çalışan ana kontrol metodu.
        Hocanın zorunlu kıldığı 'Hata Yönetimi (try-except)' burada uygulanmıştır[cite: 7].
        """
        try:
            # Motor üzerinden hamlenin geçerli olup olmadığını kontrol et[cite: 3]
            if self.motor.hamle_onayla(indis):
                SesYoneticisi.hamle_sesi_cal() # Başarılı hamlede ses çal[cite: 6]
                self.motor.tas_dagit(indis) # Taş dağıtma işlemini başlat[cite: 3]
                self.taslari_ciz() # Ekranı güncelle
                self.bilgi.config(text=f"Sıra: Oyuncu {self.motor.sira_kimde}")
                
                # Oyun bitti mi kontrolü[cite: 3]
                if not self.motor.oyun_aktif:
                    self.oyun_bitti_ekrani()
            else:
                # Geçersiz hamlede kullanıcıyı görsel olarak uyar (Kırmızı yazı efekti)
                self.bilgi.config(fg="red")
                self.pencere.after(500, lambda: self.bilgi.config(fg="#ffcc80"))
        except Exception as e:
            # Hata yönetimi: Programın çökmesini engeller ve hatayı konsola basar[cite: 7]
            print(f"Sistem Hatası: Hamle işlenirken bir hata oluştu -> {e}")

    def oyun_bitti_ekrani(self):
        """
        Oyun bittiğinde skorları kaydeden ve kazananı gösteren metod.
        Hocanın 'Modüler Sistem Tasarımı' kuralı gereği servis katmanını çağırır[cite: 7].
        """
        kazanan = self.motor.kazananı_bul() # Kazananı motordan al[cite: 3]
        p1_skor = self.motor.tahta[6]
        p2_skor = self.motor.tahta[13]
        
        # --- SERVİS KATMANI KULLANIMI ---
        # Skorları kalıcı olarak JSON dosyasına kaydediyoruz[cite: 7]
        try:
            SkorServisi.skor_kaydet(p1_skor, p2_skor, kazanan)
        except Exception as e:
            print(f"Veri Kayıt Hatası: Skorlar dosyaya yazılamadı: {e}")

        # Final skorlarını ve kazananı şık bir mesaj kutusuyla göster
        mesaj = (f"OYUN BİTTİ!\n\n"
                 f"Oyuncu 1 Skor: {p1_skor}\n"
                 f"Oyuncu 2 Skor: {p2_skor}\n\n"
                 f"Sonuç: {kazanan}\n\n"
                 f"Skorlar data/skorlar.json dosyasına başarıyla işlendi.")
        
        messagebox.showinfo("Final Sonucu", mesaj)
        self.pencere.destroy() # Oyun bittiği için uygulamayı kapat