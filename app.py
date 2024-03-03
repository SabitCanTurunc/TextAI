from dataPreprocessing import *
import logging
import string
from collections import Counter
from zemberek import TurkishMorphology, TurkishTokenizer,TurkishSentenceNormalizer
from nltk.corpus import stopwords as nltk_stopwords

# SENTENCE NORMALIZATION
# Cümle normalizasyonu için nesne oluşturuluyor
morphology = TurkishMorphology.create_with_defaults()
normalizer = TurkishSentenceNormalizer(morphology)


metin = input("Lütfen metni girin: ")

# Normalizasyon 
normalized_metin = normalizer.normalize(metin)

# Anahtar kelimeleri bulma
ana_konu_kelimesi, ana_konu_sayisi, yardimci_konular = anahtar_kelimeleri_bul(normalized_metin)

# Ana konu ve tekrar sayısı
print("Ana Konu ve Tekrar Sayısı:")
print(f"{ana_konu_kelimesi}: {ana_konu_sayisi}")

# Yardımcı konular ve tekrar sayıları
print("\nYardımcı Konular ve Tekrar Sayıları:")
for kelime, sayi in yardimci_konular:
    print(f"{kelime}: {sayi}")

# # Ana konunun köklerini bulma ve yazdırma
# ana_konu_kokler_zemberek = kelimeleri_koklere_ayir_zemberek([ana_konu_kelimesi])
# print("\nAna Konunun Kökleri (Zemberek):", ana_konu_kokler_zemberek)

# # Yardımcı konuların köklerini bulma ve yazdırma
# yardimci_konular_kokler_zemberek = kelimeleri_koklere_ayir_zemberek([kelime for kelime, _ in yardimci_konular])
# print("Yardımcı Konuların Kökleri (Zemberek):", yardimci_konular_kokler_zemberek)
