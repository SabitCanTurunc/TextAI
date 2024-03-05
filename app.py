from dataPreprocessing import *

from collections import Counter
from zemberek import TurkishMorphology, TurkishTokenizer,TurkishSentenceNormalizer
from nltk.corpus import stopwords as nltk_stopwords
from summerize import *


# SENTENCE NORMALIZATION
# Cümle normalizasyonu için nesne oluşturuluyor
morphology = TurkishMorphology.create_with_defaults()
normalizer = TurkishSentenceNormalizer(morphology)


metin="Yapay zeka, bilgisayar bilimlerinde ve yapay zeka araştırmalarında kullanılan bir terimdir. Yapay zeka, bilgisayar sistemlerine insan benzeri zeka yetenekleri kazandırmayı amaçlayan bir bilim dalıdır. Bu yetenekler arasında öğrenme, problem çözme, algılama, dil anlama ve daha pek çok şey bulunur. Yapay zeka, algoritmaların ve veri setlerinin kullanımıyla bilgisayarların karmaşık görevleri gerçekleştirebilmesini sağlar.Yapay zeka, pek çok farklı alanda kullanılmaktadır. Örneğin, otomasyon, robotik, dil işleme, görüntü işleme, oyunlar, finansal analiz, tıp alanında teşhis ve tedavi planlama gibi alanlarda yaygın olarak kullanılmaktadır.Ancak yapay zeka teknolojisinin etik ve sosyal etkileri de bulunmaktadır. Örneğin, iş gücü piyasalarında değişikliklere neden olabilir, kişisel mahremiyetin ihlal edilmesine yol açabilir veya ayrımcılığı artırabilir. Bu nedenle, yapay zeka teknolojisinin geliştirilmesi ve kullanımıyla ilgili olarak etik kurallar ve yasal düzenlemeler oldukça önemlidir."
#     
# Metni özetle
summary = summarize_article(metin)

# Özetlenmiş metni yazdır
print("özet: ",summary)

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

# Anahtar kelimeyi kullanıcıdan al
keyword = ana_konu_kelimesi
print("\nBenzer konular: ")
article_text = search_wikipedia(keyword[0:])
if article_text != "Arama sonuçları bulunamadı.":
    summary = summarize_article(article_text)
    print(summary)
else:
    print(article_text)
