import random
import time
import json
import datetime
import os
import sys


class Sinema():  # Sinema classı oluşturulur
    def __init__(self, isim):  # nesne oluştuğunda çalışan methoddur.Paremetre olarak sinema ismini alır
        self.salonlar = ["Salon-1", "Salon-2",
                         "Salon-3", "Salon-4", "Salon-5", "Salon-6"]  # Salon isimleri sınıfın değişkeni olan salonlar listesine atanır.
        self.durum = True  # Programın çalışma durumu belirlenir.
        print("Program Başlatılıyor...")
        time.sleep(0.2)
        print("Filmler çekiliyor...")
        # Sinema classının filmCek methodu çağrılır. İnternetten filmler çekilerek Sinema classının filmler listesine atanır.
        self.filmler = self.filmCek()
        # Oynatilan filmler listesi her salon için default olarak Yok atanır.
        self.OynatilanFilmler = ["Yok", "Yok", "Yok", "Yok", "Yok", "Yok"]
        self.isim = isim  # Sinema ismi Sinema clasının isim adlı değişkene atanır

    def filmCek(self):
        try:  # Eğerki Kütüphane olmama veya İnternet bağlantısı olmama durumundan dolayı hata varmı kontrol edilir
            import requests  # Request kütüphanesi dahil edilir.
            from bs4 import BeautifulSoup
            # Fikmin çekileceği web sitesi adresi girilir.
            url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
            response = requests.get(url)  # Html bilgisi çekilir.
            html_icerigi = response.content
            # Html içeriği html parser gore kullanabileceğimiz değişkene atanır
            soup = BeautifulSoup(html_icerigi, "html.parser")
            liste = list()
            for i, j in zip(soup.find_all("td", {"class": "titleColumn"}), soup.find_all("td", {"class": "ratingColumn imdbRating"})):
                a = i.text.split("\n")
                liste.append(a[2])  # Film ismi listeye atanır.
        except:  # Hata varsa default film listesi atanır
            liste = ["Hababam Sınıfı", "GORA",
                     "Hızlı ve Öfkeli", "Transformans", "Açlık Oyunları"]  # Hata olması durumunda default olarak listedeki filmler atanır.
        return liste

    def rasgeleFilm(self):
        a = random.choice(self.filmler)
        return "{}".format(a)  # Çekilen Filmlerden rasgele film dondurur.

    def menu(self):
        return """
    \t***************** {} *****************

    0. Kapat
    1. Salon sec
    2. Bilgileri Göster

secim:""".format(self.isim)  # Sinema Menusu Belirlenir.self.isim adlı degisken Film ismini Yazar {} parentezi yerine

    def Baslat(self):  # Program Başlatılır
        while self.durum:
            secim = input(self.menu())  # Menu çağrılıp secim yapılır
            if secim == "1":
                self.salonSec()  # Secim 1 ise salon seçim menusune girer
            elif secim == "2":
                # self metodu ile classın __str__() metodunu kullanarak nesneye referans olan self sinema bilgisi yazdırır
                print(self)
                input("\nDevam Et(Herhangi bir tusa basınız)")
            elif secim == "0":
                self.durum = False  # Program sonlandırılır.
                # Sonlandırılırken program ile alakalı bilgi yazdırılır.
                self.sinamaBilgiYaz()
                print("Program sonlandırılıyor...")
                time.sleep(0.7)
                print("Program sonlandı...")
            else:
                print("Hatalı kodlama...")
            time.sleep(0.2)

    def salonSec(self):  # Salon Menusunu çağırır.
        while True:
            secim = input("""
        \t*********** Salonlar ***********

        0. Geri
        1. Salon
        2. Salon
        3. Salon
        4. Salon
        5. Salon
        6. Salon
        7. Kapat

    secim:""")
            if secim == "0":  # Ust menuye gecmeye yarar
                break
            elif secim == "1":
                self.Salon("Salon-1")
            elif secim == "2":
                self.Salon("Salon-2")
            elif secim == "3":
                self.Salon("Salon-3")
            elif secim == "4":
                self.Salon("Salon-4")
            elif secim == "5":
                self.Salon("Salon-5")
            elif secim == "6":
                self.Salon("Salon-6")
            elif secim == "7":
                print("Kapatılıyor...")
                time.sleep(0.75)
                print("Kapandı...")  # Programı Kapatır
                sys.exit(1)
            else:
                print("Hatalı kodlama...\nTekrar deneyiniz...")
            time.sleep(0.3)

    def Salon(self, salon):  # Secilen Salononu menusune girilir
        self.filmDegistir(salon)  # Salona film atanır başlangıcda
        # Atılan film yazdırılır
        print("\nFilm :", self.OynatilanFilmler[int(salon[-1])-1])
        while(True):
            sec = input("""
            \t*********** {} ***********

            0. Geri
            1. Salon Düzenle
            2. Film değistir
            3. Kapat

    secim:""".format(salon))  # Salon menusu yazdırılıp seçim yapılması istenir
            if sec == "0":
                break
            elif sec == "1":
                s = Salon(
                    salon, self.OynatilanFilmler[int(salon[-1])-1], self.isim)  # Salon sınıfından obje oluşup salon
                s.Calis()  # Salon başlatılır.
            elif sec == "2":
                print("Film değiştiriliyor...")
                self.filmDegistir(salon)  # Film değiştiriliyor
                print("Film değişti...")
                print("Yeni Film :", self.OynatilanFilmler[int(salon[-1])-1])
            elif sec == "3":
                print("Kapatılıyor...")
                time.sleep(0.75)  # Program kapatılır
                print("Kapandı...")
                sys.exit(1)
            else:
                print("Hatalı kodlama...")
            time.sleep(0.2)

    def filmDegistir(self, salon):
        time.sleep(0.4)
        # Rasgele film değitirir method
        self.OynatilanFilmler[int(salon[-1])-1] = self.rasgeleFilm().strip()

    def __str__(self):  # refaransın yazdırcağı print(self) de veya oluşturulan objede döndüreceği değeri verir
        for i in range(6):
            Salon("Salon-{}".format(str(i+1)), "Yok", self.isim).BilgileriAl()

        return """
                \t\t************** Sinema Bilgileri **************

    Saat : {0}                                                                          Tarih : {1}

Toplam Film : {2}
Toplam Salon : 6
    Salonlar:
                 Oynatılan Film                Dolu Koltuk Sayısı         Boş Koltuk Sayısı      Toplam Kazanç
        Salon-1:       {3}                              {9}                        {15}               {21} TL
        Salon-2:       {4}                              {10}                       {16}               {22} TL
        Salon-3:       {5}                              {11}                       {17}               {23} TL
        Salon-4:       {6}                              {12}                       {18}               {24} TL
        Salon-5:       {7}                              {13}                       {19}               {25} TL
        Salon-6:       {8}                              {14}                       {20}               {26} TL

""".format(datetime.datetime.now().strftime("%H:%M"), datetime.datetime.now().strftime("%d/%m/%Y"), len(self.filmler), self.OynatilanFilmler[0], self.OynatilanFilmler[1], self.OynatilanFilmler[2], self.OynatilanFilmler[3], self.OynatilanFilmler[4], self.OynatilanFilmler[5], Salon("Salon-1", "Yok", self.isim).totalKoltuklar, Salon("Salon-2", "Yok", self.isim).totalKoltuklar, Salon("Salon-3", "Yok", self.isim).totalKoltuklar, Salon("Salon-4", "Yok", self.isim).totalKoltuklar, Salon("Salon-5", "Yok", self.isim).totalKoltuklar, Salon("Salon-6", "Yok", self.isim).totalKoltuklar, (400-Salon("Salon-1", "Yok", self.isim).totalKoltuklar), (400-Salon("Salon-2", "Yok", self.isim).totalKoltuklar), (400-Salon("Salon-3", "Yok", self.isim).totalKoltuklar), (400-Salon("Salon-4", "Yok", self.isim).totalKoltuklar), (400-Salon("Salon-5", "Yok", self.isim).totalKoltuklar), (400-Salon("Salon-6", "Yok", self.isim).totalKoltuklar), Salon("Salon-1", "Yok", self.isim).kazanc, Salon("Salon-2", "Yok", self.isim).kazanc, Salon("Salon-3", "Yok", self.isim).kazanc, Salon("Salon-4", "Yok", self.isim).kazanc, Salon("Salon-5", "Yok", self.isim).kazanc, Salon("Salon-6", "Yok", self.isim).kazanc)

    def sinamaBilgiYaz(self):  # Sinema bigisini SinemaBilgisi.txt yazar
        with open("SinemaBilgisi.txt", "w") as file:
            # yazılan değer sınıfın __str__ fonksiyonundaki degeri yazar
            file.write(self.__str__())


class Salon():  # Salon sınıfı oluşturulur

    def __init__(self, salon, film, sinemaİsim):
        self.durum = True  # Salon çalışma durumu belirlenir
        self .f = 0  # fiş sayısı default olarak 0 atanır
        self.salon = salon  # Salon ismi salon değişkenine atanır
        self.sinemaİsim = sinemaİsim  # Sinema ismi sinemaİsim değişkenine  ataanır
        try:  # Sahne verileri Veriler klasörün içindeki Sahne içerisinde {} -> bu işaret salon ismidir
            # Salonu çekmeye calisir cekemzse hata alinir except bloguna girer
            with open("Veriler\\Sahne\\{}.json".format(salon), "r") as file:
                self.sahne = json.load(file)
        except:
            self.sahne = []  # Sahne boş liste atanır
            # Sahne doldur metodu yeni bir sahne oluşturur
            self.SahneDoldur(salon, self.sahne)
        try:
            # Kategorileri alır verileri Veriler\\Kategoriler klasorunden Kategori yoksa except bloguna girer
            self.kategorileriAl()
        except:
            self.KategorileriSifirla()  # Sıfırdan Kategorileri sifirlar
        # Salon Bilgilerini Salon Bilgileri adlı klasorde {}.txt salon ismine gore txt den alır
        self.BilgileriAl()
        self.film = film
        self.totalKoltuklar = self.dolulukDurumu(
            1)+self.dolulukDurumu(2)+self.dolulukDurumu(3)+self.dolulukDurumu(4)  # Tum kategorileri doluluk durumu dolulukDurumu adlı methodla Veriler\\Kategoriler klasorunun icinde Salona gore Kategori verisinin uzunlugu alınır.
        # her kategori icin ve her kategori toplanıp toplam dolu koltuk sayısı bulunu

    def SahneGoster(self, liste):  # Sahne print() metodu ile konsola yazdırılır
        print("\n")
        print("*  "*39)
        print("*  "*18, "SAHNE  ", "*  "*18)
        print("*  "*39, "\n")
        for i in range(len(liste)):
            for j in range(len(liste[i])):
                print(liste[i][j], end="     ")
            print()

    def sahneGuncelle(self, salon):  # Sahne verisi Jsona yazılır ve guncellenmis olur
        while True:
            try:
                with open("Veriler\\Sahne\\{}.json".format(salon), "w") as file:
                    json.dump(self.sahne, file)
                    break  # veriyi gıncelleyip break ile cikilir
            except:  # Eger klasor yoksa klasor olustup tekrar denenir
                os.makedirs("Veriler\\Sahne")

    def SahneDoldur(self, salon, liste):  # Sahne verisi sıfırlanip sahne guncellenir
        self.sahne.clear()  # Sahne listesi sıfırlanır
        for i in range(20):  # yeni sahne olusturulur
            liste.append([])
            for j in range(20):
                liste[i].append("_")
        self.sahneGuncelle(salon)

    # Kategorileri Veriler\\Kategoriler adlı klasorden Salon ismine gore kategorileri alir
    def kategorileriAl(self):
        with open("Veriler\\Kategoriler\\{}_Kategoriler.json".format(self.salon), "r+") as file:
            self.kategoriler = json.load(file)

    # Kategori verisini Salon ismine gore ekler
    def kategorilerDoldur(self, koltuk, kategori):
        self.kategorileriAl()
        with open("Veriler\\Kategoriler\\{}_Kategoriler.json".format(self.salon), "w+") as file:
            # Kategoriler sozluk yapısına gore yapıldı her Kategori ismi altinda liste yapısı bulunur ve Kategori ismine gore listeye ekler
            self.kategoriler[kategori].append(koltuk)
            json.dump(self.kategoriler, file)

    def KategorileriSifirla(self):  # Kategoriler sifirlanir
        self.kategoriler = {"Kategori 1": [], "Kategori 2": [
        ], "Kategori 3": [], "Kategori 4": []}  # Sozluk yapisi olusturulur kategori ismine gore ve her kategori karsisinda liste bulunur
        while True:
            try:  # Kontrol eder klasor varmı
                with open("Veriler\\Kategoriler\\{}_Kategoriler.json".format(self.salon), "w") as file:
                    json.dump(self.kategoriler, file)
                    break
            except:  # yoksa klasor olusturur
                os.makedirs("Veriler\\Kategoriler")

    def dosyaOku(self):  # Fiyat bilgisi ve indirim bilgileri indirim.txt den çekilir
        with open("indirim.txt", "r") as file:
            liste = file.readlines()  # liste dondurur
        return liste

    def ucretleriOku(self):  # dosyadan ucretler okunur
        dosya = self.dosyaOku()  # indirim.txt cekilen liste dosya listesine eşitlenir
        liste = list()  # bos liste olusturulur
        # indirim.txt sirasiyla kategori 1, kategori 2, kategori 3, kategori 4 un satir satir fiyatlari yazar
        for i in dosya[1:5]:  # dosya listesinde belli bolumler alinip liste adlı listeye aktarilir
            liste.append(float(i.split("-")[1].strip("\n")))
        return liste  # Aktarılan liste donus tipi olarak dondurulur

    def indirimleriOku(self):  # dosyadan ucretler okunur
        dosya = self.dosyaOku()  # indirim.txt cekilen liste dosya listesine eşitlenir
        liste = list()  # bos liste olusturulur
        # indirim.txt deki her kategori için 5 indirim kodu vardir
        c = -1  # if ile kontrol amacli 5 degeri ayrı ayri almak icin c adli degisken olusturlup -1 den baslatilir
        """-1 denmesinin nedeni 5 eleman oldugu icin 0%5 =0 eder 20 eleman gezicegi ve her kategori icin 5 indirim kodu 
        ve 4 tane kategori oldugu icin  her 5 bolumunden kalanda yeni liste olusturulup eklenir liste içinde liste olusur
        [['10-25-20','10-25-20'",'10-25-20'",'10-25-20'",'10-25-20'],['10-25-20','10-25-20'",'10-25-20'",'10-25-20'",'10-25-20'],
        ,['10-25-20','10-25-20'",'10-25-20'",'10-25-20'",'10-25-20'],['10-25-20','10-25-20'",'10-25-20'",'10-25-20'",'10-25-20']]
        ornegin boyle liste olusur ama olusan listede her deger farkli txt den okur"""
        for i in range(5, len(dosya[5:])+5):  # dosya listesin 5 elemanindan baslanip son eleman  kadar gezer
            if i % 5 == 0:  # i degiskeni 5 bolumunden kalan 0 sa c 1 arttirilir
                c += 1
                liste.append([])  # ve liste icine liste eklenir
            # indirim kodu  '-' karekterine gore bolunup yeni listeye atilir.Burda String split metodu kullanilarak gecici listeye atanmistir
            temp = dosya[i].split("-")
            liste[c].append([int(temp[0]), int(temp[1]),
                            int(temp[2]), float(temp[3].strip("\n"))])  # sırasıyla kategori,baslangic koltuk , son koltuk,fiyat listeye eklenir
        # Kategoriye gore indirimler daha iyi alinabilmesi ve daha guzel gorunebilmesi icin sozluk yapisi kurulur
        kategoriİndirimListesi = dict()
        for i in range(len(liste)):
            # Kategori numarasina gore liste 4 kere doner listenin icindeki liste sozluk yapisina aktarilir
            kategoriİndirimListesi["Kategori {}".format(i+1)] = liste[i]
            # format metodu ile kategori sayilari her for dondugunde listeye eklenir
        """{"Kategori 1":['10-25-20','10-25-20'",'10-25-20'",'10-25-20'",'10-25-20'],"Kategori 2":['10-25-20','10-25-20'",'10-25-20'",'10-25-20'",'10-25-20'],
        "Kategori 3:['10-25-20','10-25-20'",'10-25-20'",'10-25-20'",'10-25-20'],"Kategori 4":['10-25-20','10-25-20'",'10-25-20'",'10-25-20'",'10-25-20']}
        """
        # Yapi bu sekildedir degerler ayni ve ornek amaclidir indirm.txt den cekilir
        return kategoriİndirimListesi  # Sozluk metod tarafindan dondurulur

    def Menu(self):  # Salon duzenle ye girildiginde cikacak menu belirlenir
        return """\n
    \t\t************************
    \t\t******* Ana Menu *******
    \t\t************************

        0. Çıkış
        1. Rezervasyon
        2. Salonu Yazdır
        3. Yeni Etkinlik
        4. Bilgileri Göster

    secim:"""  # Menu Menu() metodunun donus degeri olarak dondurulur

    # Fiyat belirleme yapılır. Paremetre olarak girilen kategori ile rezerve edilen koltularin listesini alir
    def fiyatBelirle(self, kategori, liste):
        # indirimleriOku() metodundan donen sozluk yapısı indirimListesi degiskenine aktarilir
        indirimListesi = self.indirimleriOku()
        ucretler = self.ucretleriOku()
        # kategoriye gore indirim alinip liste olarak a degiskenine atanir
        a = indirimListesi["Kategori {}".format(kategori)]
        # Her rezerve edilen koltuk icin fiyatListesi adlı liste olusturulur
        fiyatListesi = list()
        for z in liste:  # rezerve edilen koltuklarda gezinir for dongusu ile
            for i in a:  # kategori ile hangi alanda ise bulana kadar for dongusunde gezinir.Her kategori icin 5 alan var indirim miktarlari farklidir hepsi icin
                # degerler kontrol edilir dogru araligi bulduysa fiyatListesine eklenir.Dogru aralik koltugun konumudur satir ve sutuna gore karsilastirilir
                if i[1] <= z[2] and z[2] < i[2]:
                    fiyatListesi.append(
                        ucretler[kategori-1]-((ucretler[kategori-1]*i[3])/100))  # ilk deger fiyati ikinci deger indirimi fiyat gore ucret indirimden cikarilarak ona gore fiyat verilip listeye eklenir
                    break
        return fiyatListesi  # Fiyat listesi donrulur liste olarak

    def fisYazdir(self, liste, f, total):
        # Fiş Yazdirma İşlemini yapar.Paremetre olarak fiyatlistesi,fis sayisi,toplam tutar alinir.
        while True:
            try:  # Klasor varmi kontrol eder
                # Fis bilgisi Fişler klasorune yazdırılır.Salon ve fiş sayisina gore yazdirma yapar
                with open("Fişler\\{}_fiş{}.txt".format(self.salon, f), "w") as file:
                    # self.salon salon ismini temsil eder. f degiskeni fis sayisini temsil eder
                    # printte oldugu gibi \n ,\t ve carpam ametodu ile birden fazla strin yazdirma kullanilarak fis olusturlur
                    file.write("\n"+"\t" + "*"*47 + "\n")
                    file.write("\t" + "*"*21 + " Fiş " + "*"*21+"\n")
                    file.write("\t" + "*"*47 + "\n\n")
                    file.write("  Saat : " + datetime.datetime.now().strftime("%H:%M")+" " +
                               "\t"*7 + " Tarih : " + datetime.datetime.now().strftime("%d/%m/%Y") + "\n\n")  # şimdiki zamaninsaat ve tarih bilgisi datetime modulu ile alinir.
                    file.write("\t" + " Oynatilan Film : " + self.film+" "
                               "\t"*3 + " Salon : " + self.salon+"\n\n")  # oynatilan filme ve salon ismi yazdirilir
                    for i, j in enumerate(liste):
                        file.write(str(i+1)+" -  " + str(j[0][0])+". sıra " +
                                   str(j[0][1])+" koltuk" + "\t\t" + str(j[1]) + " TL"+"\n")  # Fiyatlar yazdirilir
                    file.write("\n"+"\t"*3 + "   Total : " +
                               str(total) + " TL"+"\n")  # Total deger yazdirirlir
                    file.write("\n"*2 + "   " + "*"*12 +
                               self.sinemaİsim+" " + "*"*12 + "\n")  # Ve en son olarak sinema ismi yazdirilir
                break  # klasor hatasi olmadiginda dongu kirarak donguden cikar
            except:  # klasor yoksa klasor olusturulup tekrar denenir
                os.mkdir("Fişler")

    # Fiş çıkarma işini gerçekleştirir hem konsola hemde txt dosyasina.Paremetre olarak kategori ile rezerve edilen koltuk listesi alinir
    def fisCıkar(self, kategori, liste):
        fiyatListesi = self.fiyatBelirle(kategori, liste)  # Fiyat belirlenir
        # self.kazanc adli degiskene tutan tutar sum metodu ile listedeki fiyatlar toplanir.
        self.kazanc += sum(fiyatListesi)
        # Ek olarak self.kazanc metodu self ile referans alarak sınıfa ait kazanc degiskeni ile tutar toplanir.sef.kazanc baslangic degeri BilgileriAl() metodunda verilmistir.
        print("\n\n", "\t\t", "*"*46)
        print("\t\t", "*"*20, " Fiş", "*"*20)
        print("\t\t", "*"*46, "\n")
        print("  Saat :", datetime.datetime.now().strftime("%H:%M"),
              "\t"*7, "Tarih :", datetime.datetime.now().strftime("%d/%m/%Y"), "\n")  # Saat ve tarih bilgisi konsolda yazilir
        print("\t", "Oynatilan Film :", self.film,
              "\t"*3, "Salon :", self.salon)  # Oynatilan solon ve film konsolda yazilir
        total = 0  # toplam fiyatin belirlenmesi icin total adli degisken olusturulur.Baslangic deger 0 atanir
        for i, j in enumerate(zip(liste, fiyatListesi)):
            if i % 5 == 0:  # Guzel gorulmesi icin her i nin 5 bolumunde \n yapilir
                print("\n")
            print("\t", str(i+1)+". ", str(j[0][0])+" sıra",
                  str(j[0][1])+" koltuk", "\t\t", str(j[1]), "TL")  # fiyatlar yazilir sirasiyla
            total += j[1]  # total fiyata fiyatlistesindeki fiyat eklenir
        # total fiyat konsolda yazılır
        print("\n", "\t"*3, "Total:", total, "TL")
        print("\n"*3, "  ", "*"*12, self.sinemaİsim, "*" *
              12, "\n")  # sinama ismi konsolda yazilir
        self.f += 1  # sınıfa ait fis sayisi 1 arttirilir
        print("Fiş çıkarıldı...")
        input("\nDevam Et(Herhangi bir tusa basınız)")
        print("\nFiş yazdırılıyor...")
        time.sleep(1)
        # fis txt yazdirilir.listeler zip ile indise gore birlesstirilip ,fis sayisi,total fiyat paremtre olarak gonderilir
        self.fisYazdir(zip(liste, fiyatListesi), self.f, total)
        print("Fiş yazdırıldı...")

    # Salon sınıfınin işlemlerin yapildiği Calis adli metoddur.
    def Calis(self):
        bilgiler = self.dosyaOku()  # bilgiler dosyadan alinir
        # max alinabilecek bilet sayisi max adli degiskene esitlenir
        max = int(bilgiler[0].split('-')[1].strip("\n"))
        ucretler = self.ucretleriOku()  # ucretler okunur
        self.indirimleriOku()  # indirimler okunur
        son = [self.dolulukDurumu(1), self.dolulukDurumu(
            2), self.dolulukDurumu(3), self.dolulukDurumu(4)]  # son rezerve edilen koltuklar alinabilmesi icin boyutlari alinir her kategori için.
        while(self.durum):  # Sınıfın boolean degerli durum degiskenine gore dongu doner
            sec = input(self.Menu())  # menu gosterilir ve secim yapilir
            if sec == "0":  # 0  secilirse menuden cikilir
                # menu cikilirken degerler gucellenir
                # sahne guncellenir.Json formatinda Solon-{}.json {}->salon numarasi
                self.sahneGuncelle(self.salon)
                # salon ile ilgili bilgiler yazilir txt formatinda Salon adiyla Salon bilgileri klasorune
                self.BilgileriYaz()
                print("Salon kapatılıyor...")
                time.sleep(0.5)
                self.durum = False  # siniftaki durum degiskeni false yapilark donguden cikilir
            elif sec == "1":  # bilet satisi yapilir
                while(True):  # dogru kategori sayisi girildi mi kontrol eder
                    try:  # sayi mi kontrol eder
                        # sayiysa devam eder.Ve sayiya donusturulur
                        kategori = int(input("Kategori(1-4):"))
                    except ValueError:
                        print("lutfen sayı giriniz...")
                        continue  # sayi degilse continue ile tekrarlar
                    if kategori > 0 and kategori < 5:  # kategori aralaliğindami kontrol eder
                        break  # donguden break ile cikilir
                    else:  # aralikta degilse msaj birakir ve donguu tekrarlar
                        print(
                            "Kategori 1 ve 4 arasında olmalıdır...\nTekrar secim yapınız...")
                k = 0  # kategori dolu olup olmadigini kontrol amacli k degiskeni olusturulur.baslangic deger 0 atanir
                while(True):  # Bilet girisi icin girilen deger dogru mu kontrol edilir
                    try:  # bilet sayimi kontrol eder
                        bilet = int(input("Bilet(1-{}):".format(max)))
                    except ValueError:
                        print("lutfen sayı giriniz...")
                        continue
                    # biletin kategori de dolumu degil mi kontrol eder.son degiskeni doluluk  durumlarindan alina listedir
                    if (bilet+int(son[kategori-1])) > 100:
                        # son degiskenin 4 degeri vardir sırasıyla [kategori 1 dolulukdurum,kategori 2 dolulukdurum,kategori 3 dolulukdurum,kategori 4 dolulukdurum]
                        print("Kategori doludur...")
                        # kategori dolmussa k 1 yapilir ve dongu tekrerlamasi saglanir
                        k = 1
                        break
                    if bilet > 0 and bilet <= max:  # bilet sayisi belirlenen alinabilecek max degiskenindeki degerdenn alinir aralikta mi kontrol edilir
                        break
                    else:  # while dongusu oldugu icin tekrar sorar
                        print(
                            "Bilet 1 ve 10 arasında olmalıdır...\nTekrar secim yapınız...")
                if k == 1:  # donguyu tekralar
                    continue
                print("Bilet alınıyor...")
                time.sleep(0.5)
                print("Rezerve ediliyor...")
                time.sleep(1)
                # biletler rezerve edilir
                rezerveListesi, son[kategori -
                                    1] = self.RezerveEt(bilet, kategori)
                # Paremetre olarak rezerve dilen koltuk listesi ile son elemanin koltuk numarasi alinir
                input("\nDevam Et(Herhangi bir tusa basınız)")
                print("Fiş çıkarılıyor...")
                time.sleep(1)
                # Fis cikarilir.Bu islemde fiyatlar belirlenip kaydedilir
                self.fisCıkar(kategori, rezerveListesi)

            elif sec == "2":  # Sahne gosterilir
                print("Sahne Açılıyor...\n")
                time.sleep(0.6)
                self.SahneGoster(self.sahne)
            elif sec == "3":  # Sahne sifirlanir
                # Sahne burada sifirlanip tekrar doldurulur
                self.SahneDoldur(self.salon, self.sahne)
                self.KategorileriSifirla()  # kategorilerde bilgiler sifirlanir
                self.BilgileriYaz()  # son bilgiler guncellenir
                # film koymak icin sinema clasina gidip film belirlenir
                print("Yeni Film başlatılıyor...\nLütfen Film koyunuz...")
                self.film = "Yok"
                self.durum = False  # Menuden cikilir sifirlandiginda. Gercekci olmasi için
                time.sleep(0.6)
            elif sec == "4":  # salon bilgisi yazdırılır
                # self burda sınıfın degiskeni temsil ediyor.Sınıfın degiskeni __str__() metodu ile printe deger dondurur
                print(self)
                input("Devam Et")
            else:
                print("Hatalı secim...")
            time.sleep(0.25)
        print("\nSalon kapatıldı...")

    # Kategori 1 in yapisi belirlenip 1 bilet kesmeye yarar.Paremetre olarak sahneyi alır
    def Kategori1(self, liste):
        for i in range(100):  # Her Kategorinde oldugu gibi Kategori 1 in 100 tane koltugu vardir bu yuzden for 100 kere donmeye ayarlanmistir
            if liste[i//10][(i % 10)+5] == "_":
                # İlk ne zaman bos koltuga gelirse koltuk doldurulup bilet kesilir.Ve donguden break ile cikilir
                # koltugu i//10 tam sayi bolmesi ile satir (i % 10)+5 salonun 5 basamagından baslanarak koltuga deger atilir
                liste[i//10][(i % 10)+5] = "#"
                # koltugun konumu satir,sutun olarak a degiskenine atanir.Listelerde sayma 0 dan basladginda satir ve sutun 1 arttirilir
                a = [(i//10)+1, (i % 10)+6, i+1]
                # kategoriler Salon ismine gore rezerve edilen koltuklar Json veri saklama yapısına eklenir
                self.kategorilerDoldur(a, "Kategori 1")
                break  # bilet kesilip donguden break ile cikilir
        return a  # biletin kesildigi konum deger olarak dondurulur

    # Kategori 3 in yapisi belirlenip 1 bilet kesmeye yarar.Paremetre olarak sahneyi alır
    def Kategori3(self, liste):
        # Her Kategorinde oldugu gibi Kategori 3 in 100 tane koltugu vardir bu yuzden for 100 kere donmeye ayarlanmistir
        for i in range(100):
            if liste[10+(i//10)][(i % 10)+5] == "_":
                # İlk ne zaman bos koltuga gelirse koltuk doldurulup bilet kesilir.Ve donguden break ile cikilir
                liste[10+(i//10)][(i % 10)+5] = "#"
                # koltugu 10+(i//10) tam sayi bolmesi ile satir (i % 10)+5 salonun 5 basamagından baslanarak koltuga deger atilir
                # koltugun konumu satir,sutun olarak a degiskenine atanir
                a = [11+(i//10), (i % 10)+6, i+1]
                # kategoriler Salon ismine gore rezerve edilen koltuklar Json veri saklama yapısına eklenir
                self.kategorilerDoldur(a, "Kategori 3")
                break  # bilet kesilip donguden break ile cikilir
        return a  # biletin kesildigi konum deger olarak dondurulur

    # Kategori 2 in yapisi belirlenip 1 bilet kesmeye yarar.Paremetre olarak sahneyi alır
    def Kategori2(self, liste):
        # ic ice fonsiyon oldugu icin cikis icin degisken tanımlanır.Baslangic deger 0 atanir.
        c = 0
        # Her Kategorinde oldugu gibi Kategori 3 in 100 tane koltugu vardir.Ama iki for dongusuyle 10 satir 10 sutun donmek Kategori 2 algoritmasi icin daha mantıklı oldugu için Kategori 1 ve Kategori 3 den farkli olarak iki for yapilmistir
        # satir degerleri gezilir.Satirlar bastan 10 tanedir.
        for i in range(10):
            for j in range(10):  # sutun degerleri gezilir
                if j < 5:  # satir degeri ilk 5 sırada satir bu donguye girer
                    # satir ve sutun degerlerind bos koltuk ise donguye girilir
                    if liste[i][4-j] == "_":
                        liste[i][4-j] = "#"  # koltuk doldurulur
                        c = 1  # ikinci donguden cikmak icin c 1 yapilir
                        a = [i+1, 5-j, (i*10)+j+1]  # koltuk konumu alinir
                        # Koltuk Salon un Json la kategoriler bilgisi kaydedilir
                        self.kategorilerDoldur(a, "Kategori 2")
                        break  # birinci donguden cikar
                else:  # egerki son 5 satirda is bu donguye girer
                    if liste[i][j+10] == "_":
                        liste[i][j+10] = "#"  # koltuk doldurulur
                        c = 1   # ikinci donguden cikmak icin c 1 yapilir
                        a = [i+1, j+11, (i*10)+j+1]  # koltuk konumu alinir
                        self.kategorilerDoldur(a, "Kategori 2")
                        # Koltuk Salon un Json la kategoriler bilgisi kaydedilir
                        break
            if c == 1:
                break  # ikinci donguden cikar
        return a  # biletin kesildigi konum deger olarak dondurulur
    # Kategori 4 in yapisi belirlenip 1 bilet kesmeye yarar.Paremetre olarak sahneyi alır

    def Kategori4(self, liste):
        # ic ice fonsiyon oldugu icin cikis icin degisken tanımlanır.Baslangic deger 0 atanir.
        c = 0
        # satir degerleri gezilir.Satirlar sondan 10 tanedir.
        for i in range(10):
            for j in range(10):  # sutun degerleri gezilir.
                if j < 5:  # satir ve sutun degerlerind bos koltuk ise donguye girilir
                    if liste[10+i][4-j] == "_":  # satir degeri ilk 5 sırada satir  bu donguye girer
                        liste[10+i][4-j] = "#"  # koltuk doldurulur
                        c = 1  # ikinci donguden cikmak icin c 1 yapilir
                        a = [11+i, 5-j, (i*10)+j+1]  # koltuk konumu alinir
                        self.kategorilerDoldur(a, "Kategori 4")
                        # Koltuk Salon un Json la kategoriler bilgisi kaydedilir
                        break
                else:  # egerki son 5 satirda is bu donguye girer
                    if liste[10+i][j+10] == "_":
                        liste[10+i][j+10] = "#"  # koltuk doldurulur
                        c = 1  # ikinci donguden cikmak icin c 1 yapilir
                        a = [11+i, j+11, (i*10)+j+1]  # koltuk konumu alinir
                        self.kategorilerDoldur(a, "Kategori 4")
                        # Koltuk Salon un Json la kategoriler bilgisi kaydedilir
                        break
            if c == 1:
                break  # ikinci donguden cikar
        return a  # biletin kesildigi konum deger olarak dondurulur

    # bilet kesiminin yapıldıgi bolumdur.Paremetre olarak kesilecek bilet sayısı bve kategoriyi alir
    def RezerveEt(self, bilet, kategori):
        if kategori == 1:  # Kategori 1 ise bu bloga girilir
            b = [self.Kategori1(self.sahne) for i in range(bilet)]
        # list comprehension metodu ile bilet sayısı kadar self.Kategori1(self.sahne) yi cagrir ve bilet kestirip konumlari biletlerin b listesine atanir
        elif kategori == 2:  # Kategori 2 ise bu bloga girilir
            b = [self.Kategori2(self.sahne) for i in range(bilet)]
        # list comprehension metodu ile bilet sayısı kadar self.Kategori2(self.sahne) yi cagrir ve bilet kestirip konumlari biletlerin b listesine atanir
        elif kategori == 3:  # Kategori 3 ise bu bloga girilir
            b = [self.Kategori3(self.sahne) for i in range(bilet)]
        # list comprehension metodu ile bilet sayısı kadar self.Kategori3(self.sahne) yi cagrir ve bilet kestirip konumlari biletlerin b listesine atanir
        elif kategori == 4:  # Kategori 4 ise bu bloga girilir
            b = [self.Kategori4(self.sahne) for i in range(bilet)]
        # list comprehension metodu ile bilet sayısı kadar self.Kategori4(self.sahne) yi cagrir ve bilet kestirip konumlari biletlerin b listesine atanir
        print("Rezerve edilen Koltuklar (Sıra-Koltuk) : ", end="")
        for i in range(len(b)):  # rezerve edilen Koltuklar yazdirilir
            if i % 5 == 0:  # daha guzel gorulmesi icin i%5==0 da \n eklenir
                print("\n")
            print(str(b[i][0])+" sıra", str(b[i][1]) +
                  " koltuk", sep=" - ", end=", ")  # satir sayisi ve sutun sayisi yazdırılır degiskenlere sirasiyla
        print("\n\nRezerve edildi...")
        return b, b[-1][-1]

    def dolulukDurumu(self, kategori):  # Kategorilerin doluluk durumu ogrenilir
        self.kategorileriAl()  # Kategorileri yeniler herhangi bir hata olmussa ek onlem icin
        if kategori == 1:    # Kategori 1 ise bu bloga girilir
            return len(self.kategoriler["Kategori 1"])
        # Girilen sozluk yapısından Kategori 1 anahtari girilerek kategori 1 deki rezerve edilen koltuklara erişilir.
        # Ve erişilen listte yapısı oldugu icin uznlugu heseplanarak doluluk durumu belirlenir
        elif kategori == 2:  # Kategori 2 ise bu bloga girilir
            return len(self.kategoriler["Kategori 2"])
        # Girilen sozluk yapısından Kategori 1 anahtari girilerek kategori 2 deki rezerve edilen koltuklara erişilir.
        # Ve erişilen listte yapısı oldugu icin uznlugu heseplanarak doluluk durumu belirlenir
        elif kategori == 3:  # Kategori 3 ise bu bloga girilir
            return len(self.kategoriler["Kategori 3"])
        # Girilen sozluk yapısından Kategori 1 anahtari girilerek kategori 3 deki rezerve edilen koltuklara erişilir.
        # Ve erişilen listte yapısı oldugu icin uznlugu heseplanarak doluluk durumu belirlenir
        elif kategori == 4:  # Kategori 4 ise bu bloga girilir
            return len(self.kategoriler["Kategori 4"])
        # Girilen sozluk yapısından Kategori 1 anahtari girilerek kategori 4 deki rezerve edilen koltuklara erişilir.
        # Ve erişilen listte yapısı oldugu icin uznlugu heseplanarak doluluk durumu belirlenir

    # Salon sınıfının str fonksiyonudur.print icinde yazdırırken ve salon bilgisi txt yazdırılırken kullanilir.
    def __str__(self):
        self.totalKoltuklar = self.dolulukDurumu(
            1)+self.dolulukDurumu(2)+self.dolulukDurumu(3)+self.dolulukDurumu(4)
        return """
    Saat : {13}                           {14}                                        Tarih:{0}
                                                                                    
        Oynatılan Film:{1}                                              
        
        Boş Koltuk Sayısı:                     Dolu Koltuk Sayısı:       
            Kategori 1:{2}                          Kategori 1:{8}
            Kategori 2:{3}                          Kategori 2:{9}
            Kategori 3:{4}                          Kategori 3:{10}
            Kategori 4:{5}                          Kategori 4:{11}
            Toplam Bos Koltuklar:{6}                Toplam Dolu Koltuklar:{12}
        Toplam Kazanç:{7} TL""".format(datetime.datetime.now().strftime("%d/%m/%Y"), self.film, (100-self.dolulukDurumu(1)), (100-self.dolulukDurumu(2)), (100-self.dolulukDurumu(3)), (100-self.dolulukDurumu(4)), (400-self.totalKoltuklar), self.kazanc, self.dolulukDurumu(1), self.dolulukDurumu(2), self.dolulukDurumu(3), self.dolulukDurumu(4), self.totalKoltuklar, datetime.datetime.now().strftime("%H:%M"), self.salon)

    def BilgileriYaz(self):  # Salon Bilgileri txt formatında Salon Bİlgileri klasorune yazdirilir
        while True:
            try:  # Klasor varmı kontrole eder
                with open("Salon Bilgileri\\{}.txt".format(self.salon), "w") as file:
                    # str fonksiyonu kullanilark sınıfın yazilir
                    file.write(self.__str__())
                break
            except:  # yoksa klasor olusturup tekrar yazmaya denenir
                os.mkdir("Salon Bilgileri")

    def BilgileriAl(self):  # Salon Bilgileri txt formatında Salon Bİlgileri klasorunden alinir
        try:  # Salon Bilgileri t var mi diye kontrol eder
            with open("Salon Bilgileri\\{}.txt".format(self.salon), "r") as file:
                self.bilgiler = file.readlines()  # bilgiler liste halinde self.bilgilere atanir
            self.kazanc = int(
                self.bilgiler[-1].split(":")[1].strip("TL").split(".")[0])  # Kazanc salon bilgilerinden cekilir
        except:  # yoksaolusturulur
            # baslangic olarak bos liste olusturulur sınıfın bilgiler adlı degiskenine
            self.bilgiler = []
            self.kazanc = 0  # kazanc herhangi bir kazanc yoksa 0 baslangic degeri atanir


sinema = Sinema("Muhammed Yasin Sinema Salonu")  # Sinema objesi olusturulur
sinema.Baslat()  # program baslatilir
