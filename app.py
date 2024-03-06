from dataPreprocessing import *
from collections import Counter
from zemberek import TurkishMorphology, TurkishTokenizer, TurkishSentenceNormalizer
from nltk.corpus import stopwords as nltk_stopwords
from summerize import *
from wiki_search import *

# SENTENCE NORMALIZATION
# Cümle normalizasyonu için nesne oluşturuluyor
morphology = TurkishMorphology.create_with_defaults()
normalizer = TurkishSentenceNormalizer(morphology)

# Kullanıcı tarafından metinlerin alınması
metinler = []
while True:
    metin = input("Lütfen bir metin girin veya çıkmak için 'q' tuşuna basın: ")
    if metin.lower() == 'q':
        break
    metinler.append(metin)

# Metinlerin analizi ve özetlenmesi
for index, metin in enumerate(metinler):
    print(f"\nMetin {index + 1} Analizi:")
    # Normalizasyon
    normalized_metin = normalizer.normalize(metin)
    # Anahtar kelimeleri bulma
    ana_konu_kelimesi, ana_konu_sayisi, yardimci_konular = anahtar_kelimeleri_bul(normalized_metin)
    # Metin Özeti
    print(f"Metin {index + 1} özeti")
    print(summarize_article(metin))
    # Ana konu ve tekrar sayısı
    print("\nAna Konu ve Tekrar Sayısı:")
    print(f"{ana_konu_kelimesi}: {ana_konu_sayisi}")
    # Yardımcı konular ve tekrar sayıları
    print("\nYardımcı Konular ve Tekrar Sayıları:")
    for kelime, sayi in yardimci_konular:
        print(f"{kelime}: {sayi}")

    # Anahtar kelimeyi kullanıcıdan al
    keyword = ana_konu_kelimesi
    print("\nBenzer konular: ")
    article_text = search_wikipedia(keyword[0:])
    if article_text != "Arama sonuçları bulunamadı.":
        summary = summarize_article(article_text)
        print(summary)
    else:
        print(article_text)
