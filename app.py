import mysql.connector
from dataPreprocessing import *
from collections import Counter
from zemberek import TurkishMorphology, TurkishTokenizer, TurkishSentenceNormalizer
from nltk.corpus import stopwords as nltk_stopwords
from summerize import *
from wiki_search import *
from dataBase import *

# SENTENCE NORMALIZATION
morphology = TurkishMorphology.create_with_defaults()
normalizer = TurkishSentenceNormalizer(morphology)

metinler = []
while True:
    metin = input("Lütfen bir metin girin veya çıkmak için 'q' tuşuna basın: ")
    if metin.lower() == 'q':
        break
    metinler.append(metin)

for index, metin in enumerate(metinler):
    normalized_metin = normalizer.normalize(metin)
    ana_konu_kelimesi, ana_konu_sayisi, yardimci_konular = anahtar_kelimeleri_bul(normalized_metin)

    print(f"\nMetin {index + 1} Analizi:")
    print(f"Metin {index + 1} özeti")
    print(summarize_article(metin))
    print("\nAna Konu ve Tekrar Sayısı:")
    print(f"{ana_konu_kelimesi}: {ana_konu_sayisi}")
    print("\nYardımcı Konular ve Tekrar Sayıları:")
    for kelime, sayi in yardimci_konular:
        print(f"{kelime}: {sayi}")

    keyword = ana_konu_kelimesi
    print("\nBenzer konular: ")
    article_text = search_wikipedia(keyword[0:])
    if article_text != "Arama sonuçları bulunamadı.":
        summary = summarize_article(article_text)
        print(summary)
    else:
        print(article_text)

    # Veritabanına kaydetme
    save_to_database(metin, ana_konu_kelimesi, ana_konu_sayisi, yardimci_konular, summary)