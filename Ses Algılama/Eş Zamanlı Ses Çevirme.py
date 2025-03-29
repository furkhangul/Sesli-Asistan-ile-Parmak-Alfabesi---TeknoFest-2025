import speech_recognition as sp
import threading
import time


# Ses tanıma fonksiyonu
def ses_tanima(tanimlayici):
    with sp.Microphone() as mic:
        print("Sesli Komut Bekleniyor... (Durdurmak için Ctrl+C tuşlayın)")
        while True:
            try:
                ses = tanimlayici.listen(mic)  # Mikrofonu dinlemeye başlar
                komut = tanimlayici.recognize_google(ses, language="tr")  # Google API ile sesli komutları tanır
                print(f"KOMUT: {komut}")  # Tanınan komutları yazdırır
            except sp.UnknownValueError:
                pass  # Tanınamayan ses hatası varsa boş bırakılır
            except sp.RequestError:
                print("API ile bağlantı sağlanamadı!")  # Google API bağlantı hatası


# Yazıya dökme işlemi (gerçek zamanlı yazmaya gerek yoksa)
def yaziyi_guncelle():
    while True:
        # Burada yazıya dökme işlemini anlık yapabiliriz veya bir dosyaya yazabiliriz
        time.sleep(1)  # Bu fonksiyon sürekli çalışıyor ama burada sadece boş bir döngü örneği


if __name__ == "__main__":
    try:
        tanimlayici = sp.Recognizer()  # Ses tanıma tanımlayıcısı

        # İki ayrı iş parçacığı başlatıyoruz:
        dinleme_thread = threading.Thread(target=ses_tanima, args=(tanimlayici,))
        yazma_thread = threading.Thread(target=yaziyi_guncelle)

        # İş parçacıklarını başlatıyoruz
        dinleme_thread.start()
        yazma_thread.start()

        # İş parçacıkları bittiğinde programı durdurmamak için
        dinleme_thread.join()
        yazma_thread.join()

    except KeyboardInterrupt:
        print("\nProgram durduruldu.")  # Ctrl+C ile durdurulduğunda mesaj verilir
