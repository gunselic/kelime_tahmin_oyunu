import tkinter as tk
from tkinter import messagebox
import random

class KelimeTahminOyunu:
    def __init__(self, root):
        self.root = root
        self.root.title("Kelime Tahmin Oyunu")
        self.root.geometry("450x350")
        self.root.configure(bg="#f0f4f8")

        # Algoritmik kelime üretimi için kelime havuzu
        self.kelimeler = [
            "algoritma", "python", "programlama", "geliştirici", 
            "yazılım", "arayüz", "etkileşim", "değişken", 
            "fonksiyon", "döngü", "nesne", "kütüphane"
        ]
        self.secilen_kelime = ""
        self.tahmin_edilen_harfler = []
        self.kalan_hak = 6

        # Arayüz elemanları
        self.baslik_label = tk.Label(root, text="Kelime Tahmin Oyunu", font=("Helvetica", 18, "bold"), bg="#f0f4f8", fg="#333333")
        self.baslik_label.pack(pady=15)

        self.kelime_label = tk.Label(root, text="", font=("Helvetica", 24, "bold"), bg="#f0f4f8", fg="#1a73e8")
        self.kelime_label.pack(pady=15)

        self.bilgi_label = tk.Label(root, text="Bir harf tahmin edin:", font=("Helvetica", 12), bg="#f0f4f8", fg="#555555")
        self.bilgi_label.pack(pady=5)

        self.harf_entry = tk.Entry(root, font=("Helvetica", 16), width=5, justify="center")
        self.harf_entry.pack(pady=5)
        # Enter tuşuna basıldığında tahmin et
        self.harf_entry.bind("<Return>", lambda event: self.tahmin_et())

        self.tahmin_buton = tk.Button(root, text="Tahmin Et", command=self.tahmin_et, font=("Helvetica", 12, "bold"), bg="#4caf50", fg="white", activebackground="#45a049", cursor="hand2")
        self.tahmin_buton.pack(pady=15)

        self.hak_label = tk.Label(root, text=f"Kalan Hak: {self.kalan_hak}", font=("Helvetica", 12, "bold"), fg="#d32f2f", bg="#f0f4f8")
        self.hak_label.pack(pady=5)

        self.yeni_oyun_baslat()

    def yeni_oyun_baslat(self):
        # Yeni bir kelime seçilir (algoritmik üretim/seçim kısmı)
        self.secilen_kelime = random.choice(self.kelimeler).upper()
        self.tahmin_edilen_harfler = []
        self.kalan_hak = 6
        self.guncelle_arayuz()

    def guncelle_arayuz(self):
        gosterilen_kelime = ""
        for harf in self.secilen_kelime:
            if harf in self.tahmin_edilen_harfler:
                gosterilen_kelime += harf + " "
            else:
                gosterilen_kelime += "_ "
        
        self.kelime_label.config(text=gosterilen_kelime.strip())
        self.hak_label.config(text=f"Kalan Hak: {self.kalan_hak}")
        self.harf_entry.delete(0, tk.END)

    def tahmin_et(self):
        # Türkçe karakter desteği ile birlikte harfi büyüt
        harf = self.harf_entry.get().replace('i', 'İ').upper()
        
        # Sadece tek bir harf girildiğinden ve harf olduğundan emin ol
        if not harf or len(harf) != 1 or not harf.isalpha():
            messagebox.showwarning("Geçersiz Giriş", "Lütfen geçerli bir tek harf giriniz.")
            return

        if harf in self.tahmin_edilen_harfler:
            messagebox.showinfo("Bilgi", "Bu harfi zaten tahmin ettiniz.")
            return

        self.tahmin_edilen_harfler.append(harf)

        # Harf kelimenin içinde yoksa hakkı azalt
        if harf not in self.secilen_kelime:
            self.kalan_hak -= 1
            if self.kalan_hak <= 0:
                self.guncelle_arayuz()
                messagebox.showerror("Oyun Bitti", f"Maalesef kaybettiniz!\nDoğru kelime: {self.secilen_kelime}")
                self.yeni_oyun_baslat()
                return
        
        self.guncelle_arayuz()

        # Kazanma durumu kontrolü
        if all(h in self.tahmin_edilen_harfler for h in self.secilen_kelime):
            messagebox.showinfo("Tebrikler!", "Kazandınız! Kelimeyi doğru tahmin ettiniz.")
            self.yeni_oyun_baslat()

if __name__ == "__main__":
    root = tk.Tk()
    oyun = KelimeTahminOyunu(root)
    root.mainloop()
