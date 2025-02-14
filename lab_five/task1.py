from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random

class GuessNumberApp(App):
    def build(self):
        self.correct_number = random.randint(1, 10)  # Pre-defined correct number
        layout = GridLayout(cols=1, padding=10, spacing=10)

        # Label for instructions
        self.label = Label(text="Choose a number between 1 and 10:", font_size=25)
        layout.add_widget(self.label)

        # Text input for user's guess
        self.text_input = TextInput(multiline=False, font_size=25)
        layout.add_widget(self.text_input)

        # Button to check the guess
        self.button = Button(text="Check Guess", font_size=25)
        self.button.bind(on_press=self.check_guess)
        layout.add_widget(self.button)

        # Label to display result
        self.result_label = Label(text="", font_size=25)
        layout.add_widget(self.result_label)

        return layout

    def check_guess(self, instance):
        try:
            user_guess = int(self.text_input.text)
            if user_guess == self.correct_number:
                self.result_label.text = "Correct! You guessed it right."
            else:
                self.result_label.text = f"Incorrect. The correct number was {self.correct_number}."
        except ValueError:
            self.result_label.text = "Please enter a valid number."

if __name__ == "__main__":
    GuessNumberApp().run()