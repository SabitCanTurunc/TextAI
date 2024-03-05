import logging
import string
from collections import Counter
from zemberek import TurkishMorphology, TurkishTokenizer, TurkishSentenceNormalizer
from nltk.corpus import stopwords as nltk_stopwords

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
    
    # En çok tekrar eden kelime grupları
    en_cok_tekrar_edilenler = kelime_sayilari.most_common(3)  # En çok tekrar eden 3 grubu al
    
    # En çok tekrar eden kelimenin grubunu ana konu olarak belirle
    ana_konu_kelimesi, ana_konu_sayisi = en_cok_tekrar_edilenler[0]
    
    # Yardımcı konuları belirleme
    yardimci_konular = en_cok_tekrar_edilenler[1:]  # İlk grubu ana konu olarak aldığımız için geri kalanları yardımcı konu yap
    
    return ana_konu_kelimesi, ana_konu_sayisi, yardimci_konular

# def test_anahtar_kelimeleri_bul():
#     # TurkishMorphology nesnesini oluştur
#     morphology = TurkishMorphology.create_with_defaults()

#     # Test metni oluştur
#     metin = """Kuantum bilgisayarlar, geleneksel bilgisayarlar gibi veriyi sıfırlar ve birler olarak saklamazlar.Bunun yerine, kuantum bit veya kubit adı verilen özel birimleri kullanırlar. Kuantum bilgisayarlar,kuantum mekaniği ilkelerine dayalı olarak çalışır ve bu nedenle bazı özel özelliklere sahiptir.Bir kubit aynı anda hem 0 hem de 1 olabilir, bu da klasik bilgisayarların yapamayacağıparalel hesaplamaları mümkün kılar. Bu özelliği, belirli türdeki hesaplamaları geleneksel bilgisayarlardançok daha hızlı yapmalarını sağlar. Kuantum bilgisayarlar, özellikle şifreleme ve veritabanı arama gibibelirli görevlerde potansiyel olarak büyük bir avantaj sağlayabilirler. Ancak, şu anda pratik uygulamalardakullanıma hazır değiller ve karmaşık teknik zorluklarla karşı karşıyadırlar.Bu nedenle, kuantum bilgisayarların gelecekteki etkileri hala belirsizdir."""    
#     # TurkishSentenceNormalizer nesnesini başlat ve metni normalize et
#     normalized_metin = TurkishSentenceNormalizer(morphology).normalize(metin)

#     # Anahtar kelimeleri bul
#     ana_konu_kelimesi, ana_konu_sayisi, yardimci_konular = anahtar_kelimeleri_bul(normalized_metin)

#     # Ana konu ve tekrar sayısı
#     print("Ana Konu ve Tekrar Sayısı:")
#     print(f"{ana_konu_kelimesi}: {ana_konu_sayisi}")

#     # Yardımcı konular ve tekrar sayıları
#     print("\nYardımcı Konular ve Tekrar Sayıları:")
#     for kelime, sayi in yardimci_konular:
#         print(f"{kelime}: {sayi}")

# # Testi çalıştır
# test_anahtar_kelimeleri_bul()
