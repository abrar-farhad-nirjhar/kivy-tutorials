from kivy.app import App
from kivy.uix.stacklayout import StackLayout

class StackLayoutApp(App):
    def build(self):
        return StackLayout()


sl = StackLayoutApp()
sl.run()