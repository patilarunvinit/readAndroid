from kivy.app import App
from kivy.core.text import Label
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.popup import Popup
import requests
import json



#data from api
response_API = requests.get('http://aamras.com/dummy/EmployeeDetails.json')
data1=response_API.text
parse_json = json.loads(data1)
t=parse_json['employees']






class MessageBox(Popup):
    message = StringProperty()

class RecycleViewRow(BoxLayout):
    text = StringProperty()




class MainScreen(RecycleView):


    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.data = [{'text':f"{str(t[x]['name'])}\n{str(t[x]['age'])}\n{str(t[x]['salary'])}"} for x in range(len(t))]


    def message_box(self, message):
        p = MessageBox()
        p.message = message
        p.open()



kv = Builder.load_file('apps.kv')

class TestApp(App):
    label = Label(text='Hello from Kivy',
                  size_hint=(.5, .5),
                  pos_hint={'center_x': .5, 'center_y': .5})

    def build(self):
        return MainScreen()

if __name__ == "__main__":
    TestApp().run()