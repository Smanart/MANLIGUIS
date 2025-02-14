from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CalculatorApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')

        self.display = TextInput(font_size=32, halign='right', size_hint=(1, 0.2), readonly=True)
        main_layout.add_widget(self.display)

        buttons = [
            ['%', 'CE', 'C', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-', '0', '.', '=']
        ]

        button_grid = GridLayout(cols=4, size_hint=(1, 0.8))

        for row in buttons:
            for label in row:
                button = Button(text=label, font_size=24)
                button.bind(on_press=self.on_button_press)
                button_grid.add_widget(button)

        main_layout.add_widget(button_grid)
        return main_layout

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.display.text = ""
        elif text == "CE":
            self.display.text = self.display.text[:-1]
        elif text == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except Exception:
                self.display.text = "Error"
        elif text == "+/-":
            if self.display.text and self.display.text[0] == "-":
                self.display.text = self.display.text[1:]
            else:
                self.display.text = "-" + self.display.text
        else:
            self.display.text += text

if __name__ == "__main__":
    CalculatorApp().run()
