-- Örnek SQL sorgusu: Belirli bir rezervasyon ID'sine sahip rezervasyonun detaylarını al
SELECT *
FROM rezervasyonlar
WHERE id = 'buraya_rezervasyon_idsi_gelecek';

-- Örnek SQL sorgusu: Belirli bir müşteri ID'sine sahip müşterinin rezervasyon bilgilerini çek
SELECT rezervasyon_tarihi, nereden_yapildi, odeme_para_birimi, baslangic_tarihi, bitis_tarihi, kisi_sayisi
FROM rezervasyonlar
WHERE musteri_id = 'buraya_musteri_idsi_gelecek';

-- Musteri tablosu
CREATE TABLE musteri (
    musteri_id INT PRIMARY KEY,
    adi VARCHAR(255),
    soyadi VARCHAR(255),
    email VARCHAR(255)
);

-- Rezervasyon tablosu
CREATE TABLE rezervasyon (
    rezervasyon_id INT PRIMARY KEY,
    musteri_id INT,
    rezervasyon_tarihi DATE,
    nereden_yapildi VARCHAR(255),
    odeme_para_birimi VARCHAR(3),
    baslangic_tarihi DATE,
    bitis_tarihi DATE,
    kisi_sayisi INT,
    FOREIGN KEY (musteri_id) REFERENCES musteri(musteri_id)
);

-- Musteri ve rezervasyon bilgilerini çekme sorgusu
SELECT
    musteri.musteri_id,
    musteri.adi,
    musteri.soyadi,
    musteri.email,
    rezervasyon.rezervasyon_tarihi,
    rezervasyon.nereden_yapildi,
    rezervasyon.odeme_para_birimi,
    rezervasyon.baslangic_tarihi,
    rezervasyon.bitis_tarihi,
    rezervasyon.kisi_sayisi
FROM
    musteri
JOIN
    rezervasyon ON musteri.musteri_id = rezervasyon.musteri_id
WHERE
    musteri.musteri_id = 'buraya_musteri_idsi_gelecek';
