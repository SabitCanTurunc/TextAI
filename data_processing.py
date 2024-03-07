from zemberek import TurkishMorphology, TurkishSentenceNormalizer
from summerize import *
from wiki_search import *
from dataPreprocessing import *


morphology = TurkishMorphology.create_with_defaults()
normalizer = TurkishSentenceNormalizer(morphology)

def analyze_text(text):
    normalized_text = normalizer.normalize(text)
    sum_text=summarize_article(text)
    ana_konu_kelimesi, ana_konu_sayisi, yardimci_konular = anahtar_kelimeleri_bul(normalized_text)
    keyword = ana_konu_kelimesi

    article_text = search_wikipedia(keyword[0:])
    if article_text != "Arama sonuçları bulunamadı.":
        summary = summarize_article(article_text)
    else:
        summary = article_text
    return {
        'ana_konu_kelimesi': ana_konu_kelimesi,
        'ana_konu_sayisi': ana_konu_sayisi,
        'yardimci_konular': yardimci_konular,
        'summary': summary,
        'sum_text': sum_text
    }

def save_to_database(text, analysis_result):
    # Veritabanına kaydetme işlemleri burada yapılır
    pass
