def kelime_sayisi_bul():
    while True:
        cumle = input("Bir Cümle Giriniz : ")
        cumleyi_kelimelere_bol = cumle.split()
        kelime_sayisi = len(cumleyi_kelimelere_bol)
        if kelime_sayisi in [1, 2, 5, 7, 8,]:
            print(f"Girdiğiniz Cümlenin Kelime Sayısı {kelime_sayisi} dir")
        elif kelime_sayisi in [3, 4, 9, 10]:
            print(f"Girdiğiniz Cümlenin Kelime Sayısı {kelime_sayisi} dür")
        elif kelime_sayisi in [6]:
            print(f"Girdiğiniz Cümlenin Kelime Sayısı {kelime_sayisi} dır")
        else:
            print(f"Girdiğiniz Cümlenin Kelime sayısı 10 dan Büyüktür")
kelime_sayisi_bul()