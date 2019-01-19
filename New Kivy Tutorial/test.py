from kivy.app import App

from kivy.uix.label import Label



class testApp(App):
    def build(self):
        return Label(text="Is this running?")


ta = testApp()
ta.run()