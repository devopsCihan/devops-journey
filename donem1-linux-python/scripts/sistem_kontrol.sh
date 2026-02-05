#!/bin/bash

# Degiskenleri tanimlayalim
SUNUCU_ADI=$(devops)
TARIH=$(date)
ACIK_KALMA_SURESI=$(uptime -p)

# Ekrana yazdiralim
echo "-------------------------"
echo "RAPOR: $SUNUCU_ADI"
echo "Tarih: $TARIH"
echo "-------------------------"
echo "Sunucu Ne Zamandır Açık?: $ACIK_KALMA_SURESI"
echo "--------------------------"
echo "Disk Durumu:"
df -h | grep "/dev/"
echo "--------------------------"

