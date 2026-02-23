import psutil
import time
import psycopg2
import datetime

print("Ajan-007 Veritabanina Baglaniyor...", flush=True)

conn = psycopg2.connect(
    dbname="raporlar",
    user="devops",
    password="gizlisifre123",
    host="veritabani",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS sistem_raporlari (
        id SERIAL PRIMARY KEY,
        zaman TIMESTAMP,
        cpu_kullanimi FLOAT,
        ram_kullanimi FLOAT
    )
""")
conn.commit()

print("Tablo hazir! Veri toplanmaya basliyor...", flush=True)

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    su_an = datetime.datetime.now()

    cur.execute(
        "INSERT INTO sistem_raporlari (zaman, cpu_kullanimi, ram_kullanimi) VALUES (%s, %s, %s)",
        (su_an, cpu, ram)
    )
    conn.commit()

    print(f"Veritabanina Kaydedildi: CPU %{cpu} | RAM %{ram}", flush=True)
    time.sleep(5)
