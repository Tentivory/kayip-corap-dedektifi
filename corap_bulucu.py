#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kayıp Çorap Dedektifi
Dünyanın en ciddi çorap bulma simülatörü.
"""

import random
import time
import sys

# Gizli mesaj (base64): QnUgc2lzdGVtZGUgaGVyIHNleSBrYXlib2x1ciBjb3JhcGxhciBnaWJpLCBkZW1va3Jhc2kgZGUgbWk/
# (decode ederseniz anlarsınız, ama lütfen etmeyin. Ciddi iş.)

def dramatik_bekle(mesaj, sure=1.5):
    print(mesaj, end="", flush=True)
    for _ in range(3):
        time.sleep(sure / 3)
        print(".", end="", flush=True)
    print()

def corap_bul():
    print("=" * 50)
    print("KAYIP ÇORAP DEDEKTİFİ v1.0 - CİDDİ İŞLER")
    print("=" * 50)
    print()
    
    tarif = input("Çorabınızı tarif edin (renk, desen, vs.): ")
    if not tarif.strip():
        tarif = "sıradan bir çorap"
    
    print(f"\nAnlaşıldı. '{tarif}' aranıyor. Bu iş ciddi.")
    
    yerler = [
        "çamaşır makinesinin arkası",
        "yatağın altı",
        "bulaşık makinesinin içi",
        "buzdolabının sebze bölmesi",
        "komşunun balkonu",
        "evrenin bir köşesi",
        "çorap boyutunda bir karadelik",
        "eşinizin gizli çorap koleksiyonu",
        "zamanın ötesinde bir yer",
        "kendisinin içinde kaybolmuş"
    ]
    
    teoriler = [
        "Çoraplar aslında çift yaşamaz, tek başına yaşar.",
        "Makine çorapları yutuyor ve başka boyutta saklıyor.",
        "Çorapların kendi iradesi var ve kaçıyorlar.",
        "Bu bir komplo teorisi değil, gerçek."
    ]
    
    for i in range(5):
        yer = random.choice(yerler)
        dramatik_bekle(f"Aranıyor: {yer}", 0.8)
        if random.random() < 0.3:
            print(f"  -> Teori: {random.choice(teoriler)}")
        time.sleep(0.5)
    
    bulunan_yer = random.choice(yerler)
    print(f"\n🎉 BULUNDU! Çorabınız '{bulunan_yer}'deydi!")
    print(f"'{tarif}' artık güvende. (Muhtemelen değil ama olsun.)")
    print()
    print("Teşekkürler, görev tamam. Bu iş ciddi iştir.")

if __name__ == "__main__":
    try:
        corap_bul()
    except KeyboardInterrupt:
        print("\n\nArama yarıda kesildi. Çorap hâlâ kayıp. Klasik.")
        sys.exit(0)

# Resmi Damga:
# Kayyum Grok - 12 Ekim 2026
# İmza: Bu kod ciddiyetle yazılmıştır. Gülmeyin.
