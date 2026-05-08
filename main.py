import tkinter as tk # Python'un standart grafik arayüz kütüphanesini (GUI) içe aktarıyoruz.
from src.ui.pencere import MangalaArayuz # Hazırladığımız arayüz sınıfını ui klasöründen projeye dahil ediyoruz.

# Programın başka bir yerden çağrılmadığını, doğrudan bu dosyadan başlatıldığını kontrol eder.
if __name__ == "__main__":
    # Tkinter kütüphanesinin ana uygulama penceresini (root) oluşturuyoruz.
    root = tk.Tk()
    
    # Pencerenin arka plan rengini projenin temasına uygun şekilde (kahverengi tonu) ayarlıyoruz.
    root.configure(bg="#3e2723")
    
    # 'MangalaArayuz' sınıfından bir nesne oluşturup, ana pencereyi (root) bu sınıfa parametre olarak gönderiyoruz.
    # Bu adımda Nesne Yönelimli Programlama (OOP) yapısı devreye girer.
    uygulama = MangalaArayuz(root)
    
    # Görsel bileşenlerin ekrana tam olarak yerleşmesi ve koordinatların hesaplanması için pencereyi güncelliyoruz.
    root.update()
    
    # Oyun başladığında kuyulardaki taşların (4'er adet) arayüzde ilk kez görselleştirilmesini sağlıyoruz.
    uygulama.taslari_ciz()
    
    # Pencerenin kullanıcı kapatana kadar ekranda açık kalmasını ve etkileşimleri dinlemesini sağlayan ana döngü.
    root.mainloop()