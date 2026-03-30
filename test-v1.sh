#!/bin/bash

echo "--- Testing mini-vocab v1 ---"

# 1. Sistemi başlat (init)
python minivocab.py init

# 2. Kelime ekle (add)
python minivocab.py add "apple" "elma"
python minivocab.py add "book" "kitap"

# 3. Listele (list)
python minivocab.py list

# 4. Öğrenildi olarak işaretle (done)
python minivocab.py done "apple"

echo "--- v1 Tests Completed ---"
