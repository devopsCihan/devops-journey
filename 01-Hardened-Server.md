# Gün 1: B2B Güvenli Sunucu İnşası (Hardening)

Bu repoda, sıfırdan kurulan bir Ubuntu sunucusunun B2B güvenlik standartlarına göre nasıl zırhlandığı (hardened) gösterilmektedir.

## Uygulanan Güvenlik Adımları:
1. `root` hesabı devre dışı bırakıldı.
2. Sadece yetkili operasyonlar için `cihan_admin` kullanıcısı oluşturuldu (`sudo` yetkisi ile).
3. UFW (Uncomplicated Firewall) aktif edildi.
4. Sadece Port 22 (SSH), Port 80 (HTTP) ve Port 443 (HTTPS) erişimine izin verildi. Diğer tüm portlar dış dünyaya kapatıldı.
