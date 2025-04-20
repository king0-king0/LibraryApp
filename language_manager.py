# language_manager.py
import json
import arabic_reshaper
from bidi.algorithm import get_display


class LanguageManager:
    def __init__(self):
        try:
            with open("./languages.json", "r", encoding="utf-8") as f:
                self.language = json.load(f)
        except:
            print("there aren't a language file")

    def lang(self, text, lang="en"):
        try:
            if "ar" == lang:
                return get_display(arabic_reshaper.reshape(self.language[lang][text]))
            if "en" == lang:
                return text
        except KeyError:
            return "Missing translation"
