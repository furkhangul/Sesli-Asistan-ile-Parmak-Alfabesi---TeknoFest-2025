import speech_recognition as sp  # Sesin text formatına çevirmek için kullanacağız.


def ses_tanima():
    tanimlayici = sp.Recognizer()  # Seslerin yazıya dönüştürülmesi için tanımlamasını sağlar.

    # Mikrofonu sürekli dinle
    with sp.Microphone() as mic:
        print("Sesli Komut Bekleniyor... (Durdurmak için Ctrl+C tuşlayın)")

        while True:
            try:
                ses = tanimlayici.listen(mic)  # Mikrofonu dinlemeye başlar.
                komut = tanimlayici.recognize_google(ses, language="tr")  # Google API ile sesli komutları tanır.
                print(f"KOMUT : {komut}")  # Tanınan komutları yazdırır.

            except sp.UnknownValueError:
                print("Anlaşılamayan Ses!")  # Tanınamayan ses hatası.
            except sp.RequestError:
                print("API ile bağlantı sağlanamadı!")  # Google API bağlantı hatası.


if __name__ == "__main__":
    try:
        ses_tanima()  # Sesli komutları sürekli tanımaya başlıyoruz.
    except KeyboardInterrupt:
        print("\nProgram durduruldu.")  # Ctrl+C ile durdurulduğunda mesaj verilir.
