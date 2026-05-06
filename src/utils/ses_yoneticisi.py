import winsound
import os

class SesYoneticisi:
    """Oyun içi ses efektlerini yöneten yardımcı sınıf."""
    
    @staticmethod
    def hamle_sesi_cal():
        # Dosya yolunu işletim sistemine uygun şekilde birleştir
        # assets/sounds/click.wav yoluna bakar
        ses_yolu = os.path.join("assets", "sounds", "click.wav")
        
        try:
            if os.path.exists(ses_yolu):
                # SND_ASYNC: Ses çalarken oyunun (arayüzün) donmasını engeller
                winsound.PlaySound(ses_yolu, winsound.SND_FILENAME | winsound.SND_ASYNC)
            else:
                print(f"Uyarı: Ses dosyası bulunamadı -> {ses_yolu}")
        except Exception as e:
            # Hata Yönetimi: Ders dökümanındaki try-catch zorunluluğu
            print(f"Ses çalma hatası: {e}")