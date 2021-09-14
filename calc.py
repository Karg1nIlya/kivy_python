from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

class Calculator(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if(self.formula == "0"):
            self.formula = ""
        
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if self.formula[-1] != "*" and self.formula[-1] != "+" and self.formula[-1] != "-" and self.formula[-1] != "/":
            if(str(instance.text).lower() == "x"):
                self.formula += "*"
            elif(str(instance.text).lower() == ","):
                self.formula += "."
            else:
                self.formula += str(instance.text)
        else:
            newformula = ""
            n = len(self.formula)
            for i in range(n-1):
                newformula += self.formula[i]
            if(str(instance.text).lower() == "x"):
                self.formula = newformula + "*"
            elif(str(instance.text).lower() == ","):
                self.formula += "." 
            else: 
                self.formula = newformula + str(instance.text).lower()
        self.update_label()

    def calc_result(self, instance):
        try:
            self.lbl.text = str(eval(self.lbl.text))
            self.formula = str(eval(self.lbl.text))
        except Exception:
            self.formula = "Error"
            self.update_label()
            self.formula = "0"

    def clear(self, instance):
        self.formula = "0"
        self.update_label()

    def percent(self, instance):
        self.formula = str(eval(self.lbl.text)*0.01)
        self.update_label()

    def sign(self, instance):
        self.formula = str(eval(self.formula)*(-1))
        self.update_label()

    def double(self, instance):
        self.formula = str(eval(self.formula)**2)
        self.update_label()

    def build(self):
        self.formula = "0"
        bl = BoxLayout(orientation = 'vertical', padding=25)
        gl = GridLayout(cols = 4, spacing=3, size_hint = (1, .6))

        self.lbl = Label(text="0", font_size = 40, halign = "right", valign="center", size_hint=(1, .6), text_size=(400-50, 500*.4-50))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text="AС", on_press = self.clear))
        gl.add_widget(Button(text="+/-", on_press = self.sign))
        gl.add_widget(Button(text="%", on_press = self.percent))
        gl.add_widget(Button(text="X^2", on_press = self.double))

        gl.add_widget(Button(text="7", on_press = self.add_number))
        gl.add_widget(Button(text="8", on_press = self.add_number))
        gl.add_widget(Button(text="9", on_press = self.add_number))
        gl.add_widget(Button(text="/", on_press = self.add_operation))

        gl.add_widget(Button(text="4", on_press = self.add_number))
        gl.add_widget(Button(text="5", on_press = self.add_number))
        gl.add_widget(Button(text="6", on_press = self.add_number))
        gl.add_widget(Button(text="X", on_press = self.add_operation))

        gl.add_widget(Button(text="1", on_press = self.add_number))
        gl.add_widget(Button(text="2", on_press = self.add_number))
        gl.add_widget(Button(text="3", on_press = self.add_number))
        gl.add_widget(Button(text="-", on_press = self.add_operation))

        gl.add_widget(Button(text="0", on_press = self.add_number))
        gl.add_widget(Button(text=",", on_press = self.add_operation))
        gl.add_widget(Button(text="=", on_press = self.calc_result))
        gl.add_widget(Button(text="+", on_press = self.add_operation))       

        bl.add_widget(gl)
        return bl

Calculator().run()
