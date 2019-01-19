from kivy.app import App
from kivy.uix.floatlayout import FloatLayout



class FloatLayoutApp(App):
    def build(self):
        return FloatLayout()


fl = FloatLayoutApp()
fl.run()