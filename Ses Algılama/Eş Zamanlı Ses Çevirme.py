import speech_recognition as sp
import threading
import time


def ses_tanima(tanimlayici):
    with sp.Microphone() as mic:
        print("Sesli Komut Bekleniyor... (Durdurmak için Ctrl+C tuşlayın)")
        while True:
            try:
                ses = tanimlayici.listen(mic)
                komut = tanimlayici.recognize_google(ses, language="tr") 
                print(f"KOMUT: {komut}")
            except sp.UnknownValueError:
                pass 
            except sp.RequestError:
                print("API ile bağlantı sağlanamadı!")

def yaziyi_guncelle():
    while True:
        time.sleep(1)


if __name__ == "__main__":
    try:
        tanimlayici = sp.Recognizer()

        dinleme_thread = threading.Thread(target=ses_tanima, args=(tanimlayici,))
        yazma_thread = threading.Thread(target=yaziyi_guncelle)
        dinleme_thread.start()
        yazma_thread.start()
        dinleme_thread.join()
        yazma_thread.join()

    except KeyboardInterrupt:
        print("\nProgram durduruldu.")
