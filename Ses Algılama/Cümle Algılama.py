import speech_recognition as sp

def ses_tanima():
    tanimlayici = sp.Recognizer()
    with sp.Microphone() as mic:
        print("Sesli Komut Bekleniyor. (Bir cümle söyleyin)")
        ses = tanimlayici.listen(mic)
        try:
            komut = tanimlayici.recognize_google(ses, language="tr")
            print(f"Ses: {komut}")
        except sp.UnknownValueError:
            print("Anlaşılamayan Ses!")
        except sp.RequestError:
            print("API ile bağlantı sağlanamadı!")

if __name__ == "__main__":
    ses_tanima()
