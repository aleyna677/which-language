"""
mini-vocab v1 — Geliştirilmiş Sürüm
Öğrenci: Aleyna Akın 251478072

V1 GÖREV LİSTESİ (TASKS):
1.Arama özelliği (search) için temel altyapının kurulması.
2.Hata mesajlarının kullanıcı dostu hale getirilmesi (Türkçeleştirme).
3. 'list' komutunun 'henüz eklenmedi' mesajı yerine dosya kontrolü yapacak şekilde güncellenmesi.
"""

import sys
import os

def initialize():
    """Sözlük dizinini ve veri dosyasını oluşturur."""
    if os.path.exists(".minivocab"):
        return "Sistem zaten başlatılmış (Already initialized)."
    os.mkdir(".minivocab")
    f = open(".minivocab/words.dat", "w")
    f.close()
    return "Mini-vocab başarıyla başlatıldı (.minivocab/ dizini oluşturuldu)."

def add_word(word, translation):
    """Yeni bir kelime çiftini dosyaya ekler."""
    if not os.path.exists(".minivocab"):
        return "Hata: Sistem başlatılmamış. Önce şunu çalıştırın: python minivocab.py init"
    
    f = open(".minivocab/words.dat", "a")
    entry = word + "|" + translation + "|LEARNING|2026-03-30\n"
    f.write(entry)
    f.close()
    return "Eklendi: " + word + " -> " + translation

def search_word(word):
    """[V1 YENİLİĞİ] Dosya içinde kelime araması yapar."""
    if not os.path.exists(".minivocab/words.dat"):
        return "Sözlük dosyası bulunamadı!"
    
    # Not: Döngü ve liste kullanmadan basit içerik kontrolü
    f = open(".minivocab/words.dat", "r")
    content = f.read()
    f.close()
    
    if word in content:
        return "[BULUNDU] " + word + " kelimesi sözlüğünüzde mevcut."
    else:
        return "[HATA] '" + word + "' kelimesi bulunamadı."

def list_words():
    """Sözlükteki kelimeleri listeler."""
    if not os.path.exists(".minivocab/words.dat"):
        return "Sözlük boş."
    
    f = open(".minivocab/words.dat", "r")
    content = f.read()
    f.close()
    
    if content == "":
        return "Henüz kelime eklenmemiş."
    return "Sözlük İçeriği:\n" + content

def show_not_implemented(command_name):
    """Henüz eklenmemiş komutlar için (Örn: done, remove)."""
    return "'" + command_name + "' komutu ilerleyen haftalarda eklenecektir."

# --- Ana Program Akışı ---
if len(sys.argv) < 2:
    print("Kullanım: python minivocab.py <komut> [argümanlar]")
elif sys.argv[1] == "init":
    print(initialize())
elif sys.argv[1] == "add":
    if len(sys.argv) < 4:
        print("Hatalı kullanım! Örnek: python minivocab.py add elma apple")
    else:
        print(add_word(sys.argv[2], sys.argv[3]))
elif sys.argv[1] == "search":
    if len(sys.argv) < 3:
        print("Lütfen aranacak kelimeyi yazın.")
    else:
        print(search_word(sys.argv[2]))
elif sys.argv[1] == "list":
    print(list_words())
elif sys.argv[1] == "done" or sys.argv[1] == "remove":
    print(show_not_implemented(sys.argv[1]))
else:
    print("Bilinmeyen komut: " + sys.argv[1])
