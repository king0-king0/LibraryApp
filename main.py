# main.py

from kivymd.app import MDApp
from kivy.lang import Builder
from language_manager import LanguageManager
from kivymd.uix.textfield import MDTextField
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from database import databaseManeger


class MyMDTextField(MDTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = "kv/font/NotoNaskhArabic-VariableFont_wght.ttf"
        self.font_name_hint_text = (
            "kv/font/NotoNaskhArabic-VariableFont_wght.ttf"  # Important!!
        )


class Main(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.databasemaneger = databaseManeger()

    def build(self):
        self.language_manager = LanguageManager()
        self.current_language = "ar"

        self.screen_manager = ScreenManager()

        # Create the loading screen
        self.loading_screen = MDScreen(name="loading")
        box = BoxLayout(spacing=20, padding=50)
        logo = Image(source="kv/images/logo.png")  # your logo path
        box.add_widget(logo)
        self.loading_screen.add_widget(box)

        self.screen_manager.add_widget(self.loading_screen)

        # Schedule moving to the home screen after 1 second
        Clock.schedule_once(self.show_home_screen, 1)

        return self.screen_manager

    def show_home_screen(self, dt):
        self.clear_screen()
        # Load home screen
        home_screen = Builder.load_file("./kv/home_screen.kv")
        screen = MDScreen(name="home")
        screen.add_widget(home_screen)

        self.screen_manager.add_widget(screen)
        self.screen_manager.current = "home"

    def clear_screen(self):
        # Check if "home" screen exists before clearing
        if self.screen_manager.has_screen("home"):
            home_screen = self.screen_manager.get_screen("home")
            home_screen.clear_widgets()  # Clear the existing widgets
        else:
            # If screen doesn't exist, load it from the .kv file and add it
            home_screen = Builder.load_file("./kv/home_screen.kv")
            screen = MDScreen(name="home")
            screen.add_widget(home_screen)
            self.screen_manager.add_widget(screen)

    def show_screen(self):
        self.clear_screen()
        home_screen = Builder.load_file("./kv/show_data.kv")
        screen = MDScreen(name="home")
        screen.add_widget(home_screen)
        self.screen_manager.add_widget(screen)
        self.screen_manager.current = "home"

    def get_text(self, text, lang=None):
        if lang is None:
            lang = self.current_language
        return self.language_manager.lang(text=text, lang=lang)

    def change_language(self):
        if self.current_language == "en":
            self.current_language = "ar"
        else:
            self.current_language = "en"
        self.clear_screen()

    def add(self):
        student_name = (
            self.screen_manager.get_screen("home").children[0].ids.student_name.text
        )
        book_name = (
            self.screen_manager.get_screen("home").children[0].ids.book_name.text
        )
        book_code = (
            self.screen_manager.get_screen("home").children[0].ids.book_code.text
        )

        self.databasemaneger.add_book(student_name, book_name, book_code)

        self.screen_manager.get_screen("home").children[0].ids.student_name.text = ""
        self.screen_manager.get_screen("home").children[0].ids.book_name.text = ""
        self.screen_manager.get_screen("home").children[0].ids.book_code.text = ""



if __name__ == "__main__":
    Main().run()


