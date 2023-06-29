import tkinter as tk
import random

adaylar = ["ihsan", "mehmet", "ali"]

def aday_ekle():
    yeni_aday = entry_ekle.get()
    if yeni_aday:
        adaylar.append(yeni_aday)
        adaylari_goster()
        entry_ekle.delete(0, tk.END)

def aday_cikar():
    secilen_index = adaylar_listbox.curselection()
    if secilen_index:
        secilen_index = secilen_index[0]
        cikan_aday = adaylar[secilen_index]
        adaylar.pop(secilen_index)
        adaylari_goster()
        kurada_secilen.config(text=f"{cikan_aday} adayı çıkarıldı.")

def kuraya_katil():
    if len(adaylar) == 0:
        kurada_secilen.config(text="Hiç aday bulunmamaktadır.")
        return

    secilen = random.choice(adaylar)
    adaylar.remove(secilen)
    kurada_secilen.config(text=f"Kurada seçilen aday: {secilen}")

def adaylari_goster():
    adaylar_listbox.delete(0, tk.END)
    for i, aday in enumerate(adaylar):
        adaylar_listbox.insert(tk.END, f"{i+1}. aday: {aday}")

root = tk.Tk()
root.title("Kura Çekimi")

# Liste Kutusu
adaylar_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30, height=10)
adaylar_listbox.pack(side=tk.LEFT, padx=10, pady=10)

# Kaydırma Çubuğu
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

# Listeyi Kaydırma Çubuğuna Bağlama
adaylar_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=adaylar_listbox.yview)

# Adayları Göster Butonu
adaylari_goster_button = tk.Button(root, text="Adayları Göster", command=adaylari_goster)
adaylari_goster_button.pack(pady=5)

# Aday Ekleme
frame_ekle = tk.Frame(root)
frame_ekle.pack(pady=5)

label_ekle = tk.Label(frame_ekle, text="Yeni aday:")
label_ekle.pack(side=tk.LEFT)

entry_ekle = tk.Entry(frame_ekle, width=20)
entry_ekle.pack(side=tk.LEFT, padx=5)

ekle_button = tk.Button(frame_ekle, text="Ekle", command=aday_ekle)
ekle_button.pack(side=tk.LEFT)

# Aday Çıkarma
cikar_button = tk.Button(root, text="Seçilen Adayı Çıkar", command=aday_cikar)
cikar_button.pack(pady=5)

# Kura Çekme
kurada_secilen = tk.Label(root, text="")
kurada_secilen.pack(pady=10)

katil_button = tk.Button(root, text="Kura Çek", command=kuraya_katil)
katil_button.pack(pady=5)

root.mainloop()
