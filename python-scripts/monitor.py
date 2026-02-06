import platform
import os
import subprocess
from datetime import datetime

def sistem_bilgisi():
    print("-" * 40)
    print(f"RAPOR TARIHI: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)

    # 1. Temel İşletim Sistemi Bilgileri
    print(f"Isletim Sistemi: {platform.system()} {platform.release()}")
    print(f"Makine Adi (Hostname): {platform.node()}")
    print(f"Islemci Mimarisi: {platform.machine()}")
    
    # 2. CPU Bilgisi (Cekirdek Sayisi)
    try:
        cpu_sayisi = os.cpu_count()
        print(f"CPU Cekirdek Sayisi: {cpu_sayisi}")
    except:
        print("CPU bilgisi alinamadi.")

    # 3. RAM Bilgisi (Linux komutu çalıştırarak)
    print("-" * 40)
    print("BELLEK (RAM) DURUMU:")
    try:
        # Python içinden Linux terminal komutu (free -h) çalıştırıyoruz
        sonuc = subprocess.check_output("free -h", shell=True).decode("utf-8")
        # Sadece başlık ve ilk satırı yazdıralım
        satirlar = sonuc.split("\n")
        print(satirlar[0]) # Başlıklar (total used free...)
        print(satirlar[1]) # Mem satırı
    except:
        print("RAM bilgisi okunamadi.")
        
    print("-" * 40)
    print("Rapor Tamamlandi.")

if __name__ == "__main__":
    sistem_bilgisi()
