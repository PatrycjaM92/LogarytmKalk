from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math


class MyGridLay(GridLayout):
    def __init__(self,**kwargs):
        super(MyGridLay, self).__init__(**kwargs)
        self.cols=1
        self.rows = 10
        self.row_force_default = True
        self.row_default_height = 40
        self.size_hint = (0.6, 0.4)
        self.spacing=50
        self.lay2 = GridLayout()
        self.lay2.cols=2
        self.add_widget(self.lay2)
        self.lay3 = GridLayout()
        self.lay3.cols = 2
        self.lay3.row_force_default = True
        self.lay3.row_default_height = 50
        self.lay3.size_hint = (0.5, 0.2)
        self.add_widget(self.lay3)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.l = Label(text=" Log2 z : ")
        self.lay2.add_widget(self.l)
        self.t=TextInput(multiline=False,
                         size =(10,5))
        self.lay2.add_widget(self.t)

        self.btnOb=Button(text="Reset")
        self.lay3.add_widget(self.btnOb)
        self.btnOb.bind(on_press=self.reset)
        self.btnReset = Button(text= "Oblicz")
        self.lay3.add_widget(self.btnReset)
        self.btnReset.bind(on_press = self.oblicz)

    def oblicz(self,instance):

        try:
            x = int(self.t.text)
            wynik =math.log2(x)

            self.lwynik =Label(text= "wynik: "+str(wynik))
            self.add_widget(self.lwynik)
        except:
            self.lInfo=Label(text='nic nie wprowadzono ')
            self.add_widget(self.lInfo)

    def reset(self,instance):

        try:
            self.t.text = ""
            self.remove_widget(self.lwynik)
            self.remove_widget(self.lInfo)
        except: print("nothing to clear")

class SayHello(App):
    def build(self):
        return MyGridLay()








if __name__ == '__main__':
    SayHello().run()

