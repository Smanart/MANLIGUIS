from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SumAverageApp(App):
    def build(self):
        layout = GridLayout(cols=1, padding=10, spacing=10)

        # Label for instructions
        self.label = Label(text="Enter two numbers:", font_size=25)
        layout.add_widget(self.label)

        # Text inputs for the two numbers
        self.text_input1 = TextInput(multiline=False, font_size=25)
        layout.add_widget(self.text_input1)

        self.text_input2 = TextInput(multiline=False, font_size=25)
        layout.add_widget(self.text_input2)

        # Button to calculate sum and average
        self.button = Button(text="Calculate", font_size=25)
        self.button.bind(on_press=self.calculate)
        layout.add_widget(self.button)

        # Label to display results
        self.result_label = Label(text="", font_size=25)
        layout.add_widget(self.result_label)

        return layout

    def calculate(self, instance):
        try:
            num1 = float(self.text_input1.text)
            num2 = float(self.text_input2.text)
            total = num1 + num2
            average = total / 2
            self.result_label.text = f"Sum: {total}, Average: {average}"
        except ValueError:
            self.result_label.text = "Please enter valid numbers."

if __name__ == "__main__":
    SumAverageApp().run()