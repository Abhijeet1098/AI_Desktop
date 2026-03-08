from automation import *
from ai_brain import ask_ai
import pyautogui
import time

def execute(command):

    if "open youtube" in command:
        open_youtube()

    elif "open calculator" in command:
        open_calculator()

    elif "open notepad" in command:
        open_notepad()

    elif "search" in command and "youtube" in command:

        query = command.replace("search","").replace("youtube","")
        search_youtube(query)

    elif "write" in command:

        topic = command.replace("write","")

        text = ask_ai(topic)

        open_notepad()
        time.sleep(2)

        pyautogui.write(text)

    else:
        answer = ask_ai(command)
        print("Zeno:", answer)