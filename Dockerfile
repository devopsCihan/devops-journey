# 1. TEMEL (Base Image): Bize Python kurulu, hafif bir Linux ver.
# "slim" versiyonu gereksiz dosyalardan arındırılmış, küçük boyuttur.
FROM python:3.9-slim
RUN apt-get update && apt-get install -y procps
# 2. ÇALIŞMA ALANI (Workdir): Konteynerin içinde '/app' diye bir klasör aç.
# Bundan sonraki her şeyi orada yap.
WORKDIR /app

# 3. KOPYALA (Copy): Bilgisayarımdaki scripti, konteynerin içine at.
# (Sol taraf: Bizim PC, Sağ taraf: Konteynerin içi)
COPY python-scripts/monitor.py .

# 4. KOMUT (Command): Konteyner çalışınca bu komutu gir.
# (Sanki biz terminale yazmışız gibi)
CMD ["python", "monitor.py"]
