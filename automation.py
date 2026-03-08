import os
import webbrowser

def open_calculator():
    os.system("calc")

def open_notepad():
    os.system("notepad")

def open_youtube():
    webbrowser.open("https://youtube.com")

def search_youtube(query):

    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)