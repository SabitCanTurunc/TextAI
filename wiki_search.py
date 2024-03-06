import wikipedia


def search_wikipedia(keyword):
    try:
        # Wikipedia API'sini kullanarak makaleyi çekme
        wikipedia.set_lang("tr")  # Türkçe Wikipedia için dil ayarı
        article = wikipedia.page(keyword)
        return article.content

    except wikipedia.exceptions.PageError:
        return "Arama sonuçları bulunamadı."

    except wikipedia.exceptions.DisambiguationError:
        return "Arama sonuçları bulunamadı."
