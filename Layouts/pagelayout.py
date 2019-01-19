from kivy.app import App
from kivy.uix.pagelayout import PageLayout

class PageLayoutApp(App):
    def build(self):
        return PageLayout()


pl = PageLayoutApp()
pl.run()