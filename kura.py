import random

adaylar = ["ihsan", "mehmet", "ali"]

def aday_ekle(isim):
    adaylar.append(isim)

def aday_cikar(isim):
    adaylar.remove(isim)

def adaylari_goster():
    for i, aday in enumerate(adaylar):
        print(f"{i+1}. aday: {aday}")

def kuraya_katil():
    if len(adaylar) == 0:
        print("Hiç aday bulunmamaktadır.")
        return

    secilen = random.choice(adaylar)
    adaylar.remove(secilen)
    print(f"Kurada seçilen aday: {secilen}")


while True:
    print("1 - Adayları göster")
    print("2 - Kura çek")
    print("3 - Aday ekle")
    print("4 - Aday çıkar")
    print("5 - Çıkış")
    
    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        adaylari_goster()
    elif secim == "2":
        kuraya_katil()
    elif secim == "3":
        yeni_aday = input("Yeni adayın ismini girin: ")
        aday_ekle(yeni_aday)
        print("Aday başarıyla eklendi.")
    elif secim == "4":
        cikan_aday = input("Çıkarılacak aday ismi: ")
        aday_cikar(cikan_aday)
        print("Aday başarıyl çıkartıldı.")
    elif secim == "5":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
