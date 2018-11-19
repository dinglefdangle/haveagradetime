from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Screen1(GridLayout):
    def __init__(self):
        super().__init__()
        self.rows = 3
        self.add_widget()

class Main(App):

    def build(self):
        return Screen1()


Main().run()