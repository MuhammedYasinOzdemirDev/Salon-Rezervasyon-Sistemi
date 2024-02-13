# Salon Rezervasyon Sistemi
Salon Rezervasyon Sistemi iki kısımdan oluşur. 
- 1 Kısım Sinema sınıfı Sinema ile ilgili bilgileri tutar. Örnek verirsem toplam sinema cirosu, Salonların doluluk oranı ve film bilgileri işleyen sınıftır. Her bir Salon Bilgisi Json veri yapısında tutulur. Ek olarak sinema bilgisi de txt dosyasında tutularak program kapatılsa bile eski başladığı yerden başlayabilir.

- 2 Kısım Salon sınıfı Salon ile ilgili bilgileri tutar. Örnek Verirsem kategoriye göre fiyat bilgileri, salon doluluk oranları, bilet satışı ve sahnenin gösterilmesiyle ilgili bilgileri işleyen sınıftır. Her Sahne ve Kategori bilgisi Json veri yapısında tutulur. Kategoriye göre bilet satımı yapılır. Bilet satışında indirim.txt bilgiler okunarak Kategori ve koltuk numarasına göre indirim yapılır. Ve fiş yazdırılır.
Program geliştirme sürecinde süreklilik ve hataların en aza indirilmesi hedeflenmiştir. Json yapısı kullanılarak bilgi kapanıp açılsa bile program kaydedilmiştir ve hatalar en aza indirilmiştir.
