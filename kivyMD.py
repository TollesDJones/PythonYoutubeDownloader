from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window

KV = """
FloatLayout:
    canvas.before:
        Color: 
            rgba: rgba("#FF5555")
        Rectangle:
            size: self.size
            pos: self.pos
    Label:
        text: "youtube downloader".title()
        size_hint: [None, None]
        size: self.texture_size
        pos_hint: {"top:0.9, "center_x:0.5}
"""

class MyApp(App):
    def build (self):
        Window.size = [360, 600]
        return Builder.load_string(KV)


if __name__== "__main__":
    app = MyApp()
    app.run()



