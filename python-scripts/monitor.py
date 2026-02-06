import platform
import os
import subprocess
from datetime import datetime

def sistem_bilgisi():
    print("-" * 40)
    print(f"RAPOR TARIHI: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)

    # 1. Isletim Sistemi
    print(f"Sistem: {platform.system()} {platform.release()}")
    
    # 2. CPU
    try:
        print(f"CPU Cekirdek: {os.cpu_count()}")
    except:
        pass

    # 3. AKILLI RAM KONTROLU (Logic Kismi)
    print("-" * 40)
    try:
        # 'free -m' komutu RAM'i Megabyte (sayi) olarak verir. Islem yapmasi kolaydir.
        ram_cikti = subprocess.check_output("free -m", shell=True).decode("utf-8")
        satirlar = ram_cikti.split("\n")
        
        # Verileri ayiklayalim (Total, Used, Free, ..., Available)
        # Linux 'free' ciktisinda son sutun genellikle "Available" (Kullanilabilir) olandir.
        degerler = satirlar[1].split()
        bos_ram = int(degerler[-1]) # En sondaki degeri al ve tamsayiya cevir
        
        print(f"Kullanilabilir RAM: {bos_ram} MB")
        
        # --- KARAR MEKANIZMASI (IF/ELSE) ---
        LIMIT = 500 # Alarm limiti (MB)
        
        if bos_ram < LIMIT:
            print(f"!!! ALARM !!! RAM Kritik Seviyenin Altinda ({bos_ram} MB < {LIMIT} MB)")
            print("ONERI: Gereksiz servisleri kapatin veya sunucuyu yeniden baslatin.")
        else:
            print(f"DURUM: YESIL (Normal). Sistem saglikli calisiyor.")
            
    except Exception as e:
        print(f"RAM bilgisi okunamadi: {e}")
        
    print("-" * 40)

if __name__ == "__main__":
    sistem_bilgisi()
