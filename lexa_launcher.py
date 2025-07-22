from voice_control import speak, listen
from folder_lock import lock_folder, unlock_folder
from code_assistant import compile_and_debug
from gui import run_gui
import subprocess
import os

def main():
    speak("Hello, I am Lexa. Your intelligent assistant.")
    while True:
        command = listen()
        if "open notepad" in command:
            subprocess.Popen("notepad.exe")
            speak("Opening Notepad.")
        elif "lock folder" in command:
            speak("Please say the folder path.")
            folder = listen()
            result = lock_folder(folder)
            speak(result)
        elif "unlock folder" in command:
            speak("Please say the folder path.")
            folder = listen()
            result = unlock_folder(folder)
            speak(result)
        elif "compile code" in command:
            speak("Please paste the code in terminal.")
            code = input("Paste your code here:\n")
            result = compile_and_debug(code)
            print(result)
            speak("Code analysis complete. Check terminal.")
        elif "launch gui" in command:
            run_gui()
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I don't understand that.")

if __name__ == "__main__":
    main()