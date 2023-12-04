import sqlite3

def rezervasyon_detaylarini_al(rezervasyon_id):
    # Veritabanına bağlan
    conn = sqlite3.connect("rezervasyonlar.db")
    cursor = conn.cursor()

    # Veritabanında rezervasyonu sorgula
    cursor.execute("SELECT * FROM rezervasyonlar WHERE id=?", (rezervasyon_id,))
    rezervasyon = cursor.fetchone()

    # Bağlantıyı kapat
    conn.close()

    return rezervasyon

# Örnek olarak rezervasyon ID'si 1 olan rezervasyonun detaylarını alalım
rezervasyon_id = 1
rezervasyon_detaylari = rezervasyon_detaylarini_al(rezervasyon_id)

# Rezervasyon detaylarını yazdır
if rezervasyon_detaylari:
    print("Rezervasyon Detayları:")
    print("ID:", rezervasyon_detaylari[0])
    print("Müşteri Adı:", rezervasyon_detaylari[1])
    print("Rezervasyon Tarihi:", rezervasyon_detaylari[2])
    # Diğer detayları da aynı şekilde ekleyebilirsiniz
else:
    print("Belirtilen ID'ye sahip rezervasyon bulunamadı.")
    
    import sqlite3

def rezervasyon_bilgilerini_goster(musteri_id):
    # Veritabanına bağlan
    conn = sqlite3.connect("rezervasyonlar.db")
    cursor = conn.cursor()

    # Müşteriye ait rezervasyon bilgilerini sorgula
    cursor.execute("""
        SELECT rezervasyon_tarihi, nereden_yapildi, odeme_para_birimi, baslangic_tarihi, bitis_tarihi, kisi_sayisi
        FROM rezervasyonlar
        WHERE musteri_id = ?
    """, (musteri_id,))

    rezervasyon_bilgileri = cursor.fetchall()

    # Bağlantıyı kapat
    conn.close()

    return rezervasyon_bilgileri

# Örnek olarak müşteri ID'si 1 olan müşteri için rezervasyon bilgilerini alalım
musteri_id = 1
rezervasyonlar = rezervasyon_bilgilerini_goster(musteri_id)

# Rezervasyon bilgilerini yazdır
if rezervasyonlar:
    print(f"Müşteri ID'si {musteri_id} için Rezervasyon Bilgileri:")
    for rezervasyon in rezervasyonlar:
        print("Rezervasyon Tarihi:", rezervasyon[0])
        print("Nereden Yapıldı:", rezervasyon[1])
        print("Ödeme Para Birimi:", rezervasyon[2])
        print("Başlangıç Tarihi:", rezervasyon[3])
        print("Bitiş Tarihi:", rezervasyon[4])
        print("Kişi Sayısı:", rezervasyon[5])
        print("-" * 30)
else:
    print(f"Müşteri ID'si {musteri_id} için rezervasyon bulunamadı.")
