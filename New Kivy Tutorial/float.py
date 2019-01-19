from kivy.app import App

from kivy.uix.floatlayout import FloatLayout








class SimpleKivy6(App):
    def build(self):
        return FloatLayout()



sk = SimpleKivy6()

sk.run()