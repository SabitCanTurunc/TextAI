import wikipedia
import re
import nltk
import heapq

def search_wikipedia(keyword, num_sentences=7):
    try:
        # Wikipedia API'sini kullanarak makaleyi çekme
        wikipedia.set_lang("tr")  # Türkçe Wikipedia için dil ayarı
        article = wikipedia.page(keyword)
        article_text = article.content

        ##### Ön İşleme
        # Köşeli Parantezleri ve Ekstra Boşlukları Kaldırma
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
        article_text = re.sub(r'\s+', ' ', article_text)

        # Özel Karakterleri ve Rakamları Kaldırma
        formatted_article_text = re.sub('[^a-zA-ZıİğĞüÜşŞöÖçÇ\s]', ' ', article_text)
        formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

        ##### Metni Cümlelere Ayırma
        sentence_list = nltk.sent_tokenize(article_text)

        ##### Kelime Frekanslarını Bulma
        stopwords = nltk.corpus.stopwords.words('turkish')
        word_frequencies = {}
        for word in nltk.word_tokenize(formatted_article_text):
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1

        maximum_frequncy = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word] / maximum_frequncy)

        ##### Cümlenin Skorunu Hesaplama
        sentence_scores = {}
        for sent in sentence_list:
            for word in nltk.word_tokenize(sent.lower()):
                if word in word_frequencies.keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word]
                        else:
                            sentence_scores[sent] += word_frequencies[word]

        ###### Anahtar Kelime İçeren Cümlelerden Özet Oluşturma
        summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)
        return summary

    except wikipedia.exceptions.PageError:
        return "Arama sonuçları bulunamadı."

    except wikipedia.exceptions.DisambiguationError:
        return "Arama sonuçları bulunamadı."

# Anahtar kelimeyi kullanıcıdan al
keyword = input("Anahtar kelimeyi girin: ")
summary = search_wikipedia(keyword)
print(summary)
