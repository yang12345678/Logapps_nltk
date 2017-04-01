from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button




class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text='Hello')
        btn2 = Button(text='World')
        layout.add_widget(btn1)
        layout.add_widget(btn2)

if __name__=="__main__":
    MyApp().run()
