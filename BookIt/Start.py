import kivy
import kivymd
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.graphics import Rectangle, Color
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.uix.button import MDCustomRoundIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.tab import MDTabsBase, MDTabsLabel
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.colorpicker import get_color_from_hex
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.factory import Factory

from kivymd.uix.bottomsheet import MDGridBottomSheet, MDListBottomSheet
from kivymd.uix.button import MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import (BaseListItem, ILeftBody, ILeftBodyTouch,
                         IRightBodyTouch)
from kivymd.material_resources import DEVICE_TYPE
from kivymd.uix.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivymd.uix.list import ImageLeftWidget
from kivy.core.window import Window

Window.size = (300, 550)


class Tab(FloatLayout, MDTabsBase, MDTabsLabel):
    pass


class SignInWindow(Screen, ButtonBehavior, MDLabel):
    pass


class MainWindow(Screen):
    pass


class SignUpWindow(Screen):
    pass


class AddBookToSell(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MyApp(MDApp):
    def show_sell(self, text_input):
        print(self.last_name_text_input.text)

    def new_message(self, book, city, price):
        new_message = ThreeLineAvatarIconListItem(text=book, secondary_text=city, tertiary_text=price)
        #new_message.add_widget(ImageLeftWidget(source=book_image))
        self.root.ids.listSell.add_widget(new_message)

    #def build(self):
        #return Builder.load_file("my.kv")


#if __name__ == "__main__":
MyApp().run()
