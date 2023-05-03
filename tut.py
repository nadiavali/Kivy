from kivy.app import App


from kivy.uix.scatter import Scatter  # Bigger and smaller and rotate
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout  # Resolution

# from kivy.uix.button import Button

"""first lesson:
- the name of app can not be kivy.py
"""


class TutorialApp(App):
    def build(self):
        # One of these should be root widget and the others should be child widgets
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Hello Kivy!", font_size=150)
        f.add_widget(s)
        s.add_widget(l)
        return f
        # return Button(text='Hello Kivy!',
        #                 background_color=(0, 0, 1, 1),
        #                 font_size=150
        #             )


if __name__ == "__main__":
    TutorialApp().run()
