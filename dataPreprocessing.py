
import logging
import string
from collections import Counter
from zemberek import TurkishMorphology, TurkishTokenizer
from nltk.corpus import stopwords as nltk_stopwords
from zemberek import TurkishSentenceNormalizer

logger = logging.getLogger(__name__)


def anahtar_kelimeleri_bul(normalized_metin):
    tokenizer = TurkishTokenizer.DEFAULT
    morphology = TurkishMorphology.create_with_defaults()
    
    # Stop words listesi (NLTK kullanarak)
    stop_words = set(nltk_stopwords.words('turkish'))
    
    # Metni kelimelere ayırma
    tokens = tokenizer.tokenize(normalized_metin)
    
    # Kelimeleri çıkarma ve noktalama işaretlerini filtreleme
    kelimeler = []
    for i in range(len(tokens) - 2):  # Üçlü kelimeleri al
        token1 = tokens[i].content
        token2 = tokens[i + 1].content
        token3 = tokens[i + 2].content
        # Noktalama işaretlerini ve gereksiz boşlukları filtrele
        content_cleaned = ''.join(char for char in (token1 + ' ' + token2 + ' ' + token3) if char not in string.punctuation)
        content_cleaned = content_cleaned.strip()
        # Stop words listesinde olmayan kelimeleri ekle
        if content_cleaned.lower() not in stop_words and content_cleaned != '':
            kelimeler.append(content_cleaned)
    
    # Kelimeleri say
    kelime_sayilari = Counter(kelimeler)
    
    # En çok tekrar eden kelime grubu
    ana_konu_kelimesi, ana_konu_sayisi = kelime_sayilari.most_common(1)[0]
    del kelime_sayilari[ana_konu_kelimesi]  # Ana konu kelimesini kelime sayılarından çıkar
    
    # Yardımcı konuları belirleme
    yardimci_konular = [(kelime, sayi) for kelime, sayi in kelime_sayilari.items() if sayi >= 2]  # Tekrar sayısı 2'den fazla olanları al
    
    return ana_konu_kelimesi, ana_konu_sayisi, yardimci_konular


def kelimeleri_koklere_ayir_zemberek(kelimeler):
    morphology = TurkishMorphology.create_with_defaults()
    kokler = []  # Kökleri saklamak için bir liste oluşturuyoruz
    for kelime in kelimeler:
        analysis = morphology.analyze(kelime)
        if analysis:
            for result in analysis:
                kok = result.get_stem()
                kokler.append(kok)
    kokler = list(set(kokler))  # Tekrar eden kökleri temizleme
    kokler.sort()  # Kökleri sıralıyoruz
    return kokler

