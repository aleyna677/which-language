#!/bin/bash

echo "--- Testing mini-vocab v2 Updates ---"

# 1. Sistemi başlat (Zaten varsa 'Already initialized' demeli)
python minivocab.py init

# 2. Yeni kelime ekle
python minivocab.py add "computer" "bilgisayar"

# 3. [YENİ ÖZELLİK] Arama yap (search) - Mevcut kelime
echo "Testing Search (Existing):"
python minivocab.py search "computer"

# 4. [YENİ ÖZELLİK] Arama yap (search) - Olmayan kelime
echo "Testing Search (Non-existent):"
python minivocab.py search "pencil"

# 5. Hata durumu: Eksik argüman ile add komutu
echo "Testing Error Handling (Missing Args):"
python minivocab.py add "table"

echo "--- v2 Tests Completed ---"
