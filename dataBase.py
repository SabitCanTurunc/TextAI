import mysql.connector

def save_to_database(metin, ana_konu_kelimesi, ana_konu_sayisi, yardimci_konular, benzer_konular):
    try:
        # Veritabanı bağlantısı oluşturma
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="124456",
            database="akinsoftai"
        )

        # Cursor nesnesi oluşturma
        cursor = db_connection.cursor()

        # Metni kaydet
        cursor.execute("INSERT INTO Metinler (metin) VALUES (%s)", (metin,))
        metin_id = cursor.lastrowid
        
        # Ana konuları kaydet
        cursor.execute("INSERT INTO AnaKonular (metin_id, ana_konu_kelimesi, ana_konu_sayisi) VALUES (%s, %s, %s)",
                       (metin_id, ana_konu_kelimesi, ana_konu_sayisi))

        # Yardımcı konuları kaydet
        for kelime, sayi in yardimci_konular:
            cursor.execute("INSERT INTO YardimciKonular (metin_id, kelime, sayi) VALUES (%s, %s, %s)",
                           (metin_id, kelime, sayi))

        # Benzer konuları kaydet
        benzer_konular_str = ','.join(benzer_konular)
        cursor.execute("INSERT INTO BenzerKonular (metin_id, benzer_konu) VALUES (%s, %s)",
                       (metin_id, benzer_konular_str))

        db_connection.commit()
        print("Veritabanına başarıyla kaydedildi.")
    except mysql.connector.Error as err:
        print("Veritabanına kaydedilirken hata oluştu:", err)
        db_connection.rollback()
    finally:
        # Bağlantıyı kapat
        cursor.close()
        db_connection.close()