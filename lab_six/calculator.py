from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CalculatorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.input_field = TextInput(font_size=32, halign='center', size_hint=(1, 0.3), multiline=False)
        layout.add_widget(self.input_field)

        button_layout = BoxLayout(size_hint=(1, 0.2))

        calculate_button = Button(text="Calculate", font_size=24)
        calculate_button.bind(on_press=self.calculate_expression)
        button_layout.add_widget(calculate_button)

        clear_button = Button(text="Clear", font_size=24)
        clear_button.bind(on_press=self.clear_input)
        button_layout.add_widget(clear_button)

        layout.add_widget(button_layout)

        return layout

    def calculate_expression(self, instance):
        try:
            expression = self.input_field.text
            result = eval(expression)
            self.input_field.text = f"{expression} = {result}"
        except Exception:
            self.input_field.text = "Error"

    def clear_input(self, instance):
        self.input_field.text = ""

if __name__ == '__main__':
    CalculatorApp().run()
