import tkinter as tk
from voice_control import speak, listen
from folder_lock import lock_folder, unlock_folder

def run_gui():
    def on_voice():
        command = listen()
        if "lock folder" in command:
            speak("Give folder path.")
            folder = listen()
            result = lock_folder(folder)
            speak(result)
        elif "unlock folder" in command:
            speak("Give folder path.")
            folder = listen()
            result = unlock_folder(folder)
            speak(result)
        else:
            speak("Command not recognized.")

    win = tk.Tk()
    win.title("Lexa GUI")
    win.geometry("300x200")
    btn = tk.Button(win, text="🎙️ Start Voice Command", command=on_voice)
    btn.pack(pady=50)
    win.mainloop()