import tkinter as tk
from src.ui.pencere import MangalaArayuz

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#3e2723")
    uygulama = MangalaArayuz(root)
    
    # Ekranın tam yüklenmesi için kısa bir bekleme ve taşları ilk kez çizme
    root.update()
    uygulama.taslari_ciz()
    
    root.mainloop()