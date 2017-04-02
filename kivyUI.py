# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.uix.button import Button
#
#
#
#
# class MyApp(App):
#     def build(self):
#         layout = BoxLayout(orientation='vertical')
#         btn1 = Button(text='Hello')
#         btn2 = Button(text='World')
#         layout.add_widget(btn1)
#         layout.add_widget(btn2)
#
# if __name__=="__main__":
#     MyApp().run()

import os
from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = '/path/to/standford/jars'os.environ['STANFORD_MODELS'] = '/path/to/standford/jars'
parser = stanford.StanfordParser(model_path="/location/of/the/englishPCFG.ser.gz")
sentences = parser.raw_parse_sents(("Hello, My name is Melroy.", "What is your name?"))
print sentences
# GUI
for line in sentences:
    for sentence in line:
        sentence.draw()
