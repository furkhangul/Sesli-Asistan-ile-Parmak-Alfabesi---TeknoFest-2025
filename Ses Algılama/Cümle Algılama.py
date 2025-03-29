import speech_recognition as sp  # Sesin text formatına çevirmek için kullanacağız.

def ses_tanima():
    tanimlayici = sp.Recognizer()  # Seslerin yazıya dönüştürülmesi için tanımlamasını sağlar.
    with sp.Microphone() as mic:
        print("Sesli Komut Bekleniyor. (Bir cümle söyleyin)")
        ses = tanimlayici.listen(mic)  # Mikrofonu dinlemeye başlar.
        try:
            # Google API'si ile sesli komutları tanıyacağız ve dil parametresi olarak Türkçe'yi belirtiyoruz.
            komut = tanimlayici.recognize_google(ses, language="tr")
            print(f"Ses: {komut}")
        except sp.UnknownValueError:
            print("Anlaşılamayan Ses!")
        except sp.RequestError:
            print("API ile bağlantı sağlanamadı!")

if __name__ == "__main__":
    ses_tanima()  # Sesli komutları tanımaya başlıyoruz.
