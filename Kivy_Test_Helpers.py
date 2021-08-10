youtube_link_layout = """
MDTextField:
    hint_text: 'Paste Your Link Here'
    helper_text: 'Copy video link form youtube'
    helper_text_mode: 'on_focus'
    icon_right: 'youtube'
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width: 300

"""

# btn_Go_layout = """
# MDRectangleFlatButton:
#     text: 'Go'
#     pos_hint: {'center_x': 0.5, 'center_y': 0.4}
#     on_press: self.show_data()
# """