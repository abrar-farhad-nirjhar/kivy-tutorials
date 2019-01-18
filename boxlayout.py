from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutApp(App):
    def build(self):
        return BoxLayout()


bl = BoxLayoutApp()
bl.run()