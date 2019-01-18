from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class GridLayoutApp(App):
    def build(self):
        return GridLayout()


gl = GridLayoutApp()
gl.run()