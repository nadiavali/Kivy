from kivy.app import App

from kivy.uix.scatter import Scatter  # Bigger and smaller and rotate
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout  # Resolution
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout # place it child widget all in a row either vertically or horizontally
# from kivy.uix.button import Button

"""first lesson:
- the name of app can not be kivy.py
"""


class TutorialApp(App):
    def build(self):
        # One of these should be root widget and the others should be child widgets
        b = BoxLayout(orientation='vertical') # top and the bottom by adding vertical
        t = TextInput(font_size=150,
                        size_hint_y=None, # if you want to have specific height you need to set this to none, otherwise it will be by default half of the screen height
                        # and also it takes 1 or 0 which 1 is the default
                        height=200,
                        text='default')
        # FloatLayout allows you to specify the exact position of each widget within the layout
        f = FloatLayout() 
        s = Scatter()
        l = Label(text='default', font_size=150) # does't matter what you write here it always takes the text from the text input value
        # in general set them to the same values otherwise it can be buggy

        # let you to modify the texts changes and that binds two widgets together
        t.bind(text=l.setter('text')) # it should be text otherwise you can't modify the textinput and label and also if it is not 'text' if the label and text input have different values you will see that in box layout
        f.add_widget(s)
        s.add_widget(l)

        # Order of displaying is important to which comes first
        # In this case text input t will be at the top
        # Question: why it doesn't show the default text of label when t and f children's order get changed 
        b.add_widget(t)
        b.add_widget(f)
        return b
        # return Button(text='Hello Kivy!',
        #                 background_color=(0, 0, 1, 1),
        #                 font_size=150
        #             )

#def some_function(*args):
    print('text changed')

if __name__ == "__main__":
    TutorialApp().run()
