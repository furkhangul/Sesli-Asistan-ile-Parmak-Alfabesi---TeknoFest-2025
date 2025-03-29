import speech_recognition as sp 

def ses_tanima():
    tanimlayici = sp.Recognizer()

    with sp.Microphone() as mic:
        print("Sesli Komut Bekleniyor... (Durdurmak için Ctrl+C tuşlayın)")

        while True:
            try:
                ses = tanimlayici.listen(mic) 
                komut = tanimlayici.recognize_google(ses, language="tr")
                print(f"KOMUT : {komut}")

            except sp.UnknownValueError:
                print("Anlaşılamayan Ses!") 
            except sp.RequestError:
                print("API ile bağlantı sağlanamadı!") 


if __name__ == "__main__":
    try:
        ses_tanima() 
    except KeyboardInterrupt:
        print("\nProgram durduruldu.") 
