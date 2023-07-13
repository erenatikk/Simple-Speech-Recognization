import tkinter as tk
import speech_recognition as sr
from threading import Thread

def start_recording():
    global recording
    recording = True
    print("Kayıt başladı.")

def stop_recording():
    global recording
    recording = False
    print("Kayıt durdu.")

def process_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Konuşmaya başlayın...")
        while True:
            if recording:
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio, language="tr-TR")
                    text_output.config(state='normal')
                    text_output.delete("1.0", tk.END)
                    text_output.insert(tk.END, text)
                    text_output.config(state='disabled')
                except sr.UnknownValueError:
                    pass
                except sr.RequestError as e:
                    print("Google Konuşma Tanıma servisine erişilemedi; {0}".format(e))

def start_processing():
    thread = Thread(target=process_audio)
    thread.start()

recording = False

window = tk.Tk()
window.title("Konuşma Tanıma Arayüzü")

start_button = tk.Button(window, text="Kaydı Başlat", command=start_recording)
start_button.pack(pady=10)

stop_button = tk.Button(window, text="Kaydı Durdur", command=stop_recording)
stop_button.pack(pady=10)

text_output = tk.Text(window, height=10, width=50, state='disabled')
text_output.pack(pady=10)

start_processing()

window.mainloop()
