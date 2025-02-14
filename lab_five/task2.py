from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class WordCountApp(App):
    def build(self):
        layout = GridLayout(cols=1, padding=10, spacing=10)

        # Label for instructions
        self.label = Label(text="Enter a sentence:", font_size=25)
        layout.add_widget(self.label)

        # Text input for the sentence
        self.text_input = TextInput(multiline=False, font_size=25)
        layout.add_widget(self.text_input)

        # Button to count words
        self.button = Button(text="Count Words", font_size=25)
        self.button.bind(on_press=self.count_words)
        layout.add_widget(self.button)

        # Label to display word count
        self.result_label = Label(text="", font_size=25)
        layout.add_widget(self.result_label)

        return layout

    def count_words(self, instance):
        sentence = self.text_input.text
        word_count = len(sentence.split())
        self.result_label.text = f"Word count: {word_count}"

if __name__ == "__main__":
    WordCountApp().run()