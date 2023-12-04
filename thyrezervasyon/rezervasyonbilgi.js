<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rezervasyon Bilgileri</title>
</head>
<body>

  <h1>Rezervasyon Bilgileri</h1>

  <div id="rezervasyonBilgileri"></div>

  <script>
    function rezervasyonBilgileriniGetir(musteriId) {
      // Simüle edilmiş veritabanı bilgileri
      var rezervasyonlar = [
        { musteri_id: 1, rezervasyon_tarihi: '2023-12-01', nereden_yapildi: 'Online', odeme_para_birimi: 'USD', baslangic_tarihi: '2023-12-15', bitis_tarihi: '2023-12-20', kisi_sayisi: 2 },
        // Diğer rezervasyonlar buraya eklenebilir
      ];

      // Müşteriye ait rezervasyonları filtrele
      var musteriRezervasyonlari = rezervasyonlar.filter(function(rezervasyon) {
        return rezervasyon.musteri_id === musteriId;
      });

      // HTML içeriğini oluştur
      var rezervasyonBilgileriHTML = '';
      if (musteriRezervasyonlari.length > 0) {
        rezervasyonBilgileriHTML += '<ul>';
        musteriRezervasyonlari.forEach(function(rezervasyon) {
          rezervasyonBilgileriHTML += '<li>';
          rezervasyonBilgileriHTML += 'Rezervasyon Tarihi: ' + rezervasyon.rezervasyon_tarihi + '<br>';
          rezervasyonBilgileriHTML += 'Nereden Yapıldı: ' + rezervasyon.nereden_yapildi + '<br>';
          rezervasyonBilgileriHTML += 'Ödeme Para Birimi: ' + rezervasyon.odeme_para_birimi + '<br>';
          rezervasyonBilgileriHTML += 'Başlangıç Tarihi: ' + rezervasyon.baslangic_tarihi + '<br>';
          rezervasyonBilgileriHTML += 'Bitiş Tarihi: ' + rezervasyon.bitis_tarihi + '<br>';
          rezervasyonBilgileriHTML += 'Kişi Sayısı: ' + rezervasyon.kisi_sayisi + '<br>';
          rezervasyonBilgileriHTML += '</li>';
        });
        rezervasyonBilgileriHTML += '</ul>';
      } else {
        rezervasyonBilgileriHTML = 'Müşteriye ait rezervasyon bulunamadı.';
      }

      // HTML'i sayfaya ekle
      document.getElementById('rezervasyonBilgileri').innerHTML = rezervasyonBilgileriHTML;
    }

    // Örnek olarak müşteri ID'si 1 olan müşterinin rezervasyon bilgilerini getir
    rezervasyonBilgileriniGetir(1);
  </script>

</body>
</html>
