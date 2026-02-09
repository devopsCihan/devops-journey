import platform
import os
import subprocess
import shutil
from datetime import datetime

def sistem_bilgisi():
    zaman = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("-" * 50)
    print(f"RAPOR TARIHI: {zaman}")
    print("-" * 50)

    # 1. Isletim Sistemi
    print(f"Sistem: {platform.system()} {platform.release()}")
    
    # 2. RAM KONTROLU
    print("-" * 20 + " BELLEK (RAM) " + "-" * 20)
    try:
        ram_cikti = subprocess.check_output("free -m", shell=True).decode("utf-8")
        satirlar = ram_cikti.split("\n")
        degerler = satirlar[1].split()
        bos_ram = int(degerler[-1]) 
        
        RAM_LIMIT = 500
        if bos_ram < RAM_LIMIT:
            print(f"!!! ALARM !!! RAM Kritik Seviyenin Altinda ({bos_ram} MB)")
        else:
            print(f"DURUM: RAM Normal ({bos_ram} MB bos).")
    except:
        print("RAM bilgisi alinamadi.")

    # 3. DISK KONTROLU (YENI OZELLIK)
    print("-" * 20 + " DISK ALANI " + "-" * 20)
    try:
        # Kök dizini (/) kontrol et
        disk = shutil.disk_usage("/")
        
        # Byte'ı Gigabyte'a (GB) cevir
        toplam_gb = disk.total / (1024**3)
        bos_gb = disk.free / (1024**3)
        kullanilan_gb = disk.used / (1024**3)
        doluluk_orani = (disk.used / disk.total) * 100
        
        print(f"Toplam: {toplam_gb:.2f} GB | Kullanilan: {kullanilan_gb:.2f} GB | Bos: {bos_gb:.2f} GB")
        print(f"Doluluk Orani: %{doluluk_orani:.2f}")

        DISK_LIMIT = 90.0 # Yuzde 90
        
        if doluluk_orani > DISK_LIMIT:
            print(f"!!! KRITIK UYARI !!! Disk doluyor! (%{doluluk_orani:.2f})")
        else:
            print(f"DURUM: Disk saglikli.")
            
    except Exception as e:
        print(f"Disk bilgisi alinamadi: {e}")

    print("-" * 50)

if __name__ == "__main__":
    sistem_bilgisi()


# ... Disk kodlarının bittiği yer ...

    # 4. UPTIME (CALISMA SURESI) KONTROLU
    print("-" * 20 + " CALISMA SURESI " + "-" * 20)
    try:
        uptime_suresi = subprocess.check_output("uptime -p", shell=True).decode("utf-8").strip()
        print(f"Sistem {uptime_suresi} suredir ayakta.")
    except Exception as e:
        print(f"Uptime bilgisi alinamadi: {e}")

    print("-" * 50)
