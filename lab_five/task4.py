from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math
    
class TriangleApp(App):
    def build(self):
        layout = GridLayout(cols=1, padding=10, spacing=10)

        # Label for instructions
        self.label = Label(text="Enter three sides of a triangle:", font_size=25)
        layout.add_widget(self.label)

        # Text inputs for the three sides
        self.text_input1 = TextInput(multiline=False, font_size=25)
        layout.add_widget(self.text_input1)

        self.text_input2 = TextInput(multiline=False, font_size=25)
        layout.add_widget(self.text_input2)

        self.text_input3 = TextInput(multiline=False, font_size=25)
        layout.add_widget(self.text_input3)

        # Button to calculate perimeter and area
        self.button = Button(text="Calculate", font_size=25)
        self.button.bind(on_press=self.calculate)
        layout.add_widget(self.button)

        # Label to display results
        self.result_label = Label(text="", font_size=25)
        layout.add_widget(self.result_label)

        return layout

    def calculate(self, instance):
        try:
            a = float(self.text_input1.text)
            b = float(self.text_input2.text)
            c = float(self.text_input3.text)

            # Check if the sides form a valid triangle
            if a + b > c and a + c > b and b + c > a:
                perimeter = a + b + c
                s = perimeter / 2  # Semi-perimeter
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Heron's formula
                self.result_label.text = f"Perimeter: {perimeter}, Area: {area:.2f}"
            else:
                self.result_label.text = "Invalid triangle sides."
        except ValueError:
            self.result_label.text = "Please enter valid numbers."

if __name__ == "__main__":
    TriangleApp().run()