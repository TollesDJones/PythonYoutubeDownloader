from kivy import lang
from kivymd.app import MDApp
from kivymd.uix import screen
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDRectangleFlatIconButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from pytube import YouTube
import pytube
from pytube.helpers import regex_search
import Kivy_Test_Helpers as kh

# This code can be moved to a module file within the same drectory 
# and imported. 

# youtube_link_layout = """
# MDTextField:
#     hint_text: 'Paste Your Link Here'
#     helper_text: 'Copy video link form youtube'
#     helper_text_mode: 'on_focus'
#     icon_right: 'youtube'
#     icon_right_color: app.theme_cls.primary_color
#     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#     size_hint_x: None
#     width: 300

# """

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'
        
        screen = Screen()
        self.txt_ent_youtube_link = Builder.load_string(kh.youtube_link_layout)
        btn_Go = MDRectangleFlatButton(text='GO', pos_hint= {'center_x':0.5, 'center_y':0.4}, on_press= self.show_data)
        screen.add_widget(self.txt_ent_youtube_link)
        screen.add_widget(btn_Go)
        return screen

    def show_data(self, obj):
        print(self.txt_ent_youtube_link.text)
        link = self.txt_ent_youtube_link.text
        yt= YouTube(link)
        run = True
        while run:
            try:
                yt.streams.get_highest_resolution().download(output_path='./downloads')
                run = False
                break
            except:
                print('Invalid link, Please try again.')
              
        self.txt_ent_youtube_link.text = ''


DemoApp().run()



 # def build(self):
    #     self.theme_cls.primary_palette = 'Red'
    #     self.theme_cls.primary_hue = 'A700'
    #     self.theme_cls.theme_style = 'Dark'

    #     screen = Screen()
    #     youtube_link = MDTextField(text='Enter video link', 
    #                                 pos_hint={'center_x':0.5, 'center_y':0.5}, 
    #                                 size_hint_x= None, width=300)

    #     btn_flat = MDRectangleFlatButton(text='Hello World!', 
    #                             pos_hint={'center_x':0.5, 'center_y':0.6})
    #     screen.add_widget(btn_flat)
    #     screen.add_widget(youtube_link)
    #     return screen


 # label = MDLabel(text="Hello World", 
        #                 halign="center",
        #                 theme_text_color="Error", 
        #                 font_style="Caption")

        # icon_label = MDIcon(icon="apple", halign="center")
        # return icon_label