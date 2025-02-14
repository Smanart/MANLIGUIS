from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class ToDoApp(App):
    def build(self):
        self.tasks = []

        # Main layout
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        # Text input for adding tasks
        self.task_input = TextInput(hint_text="Enter a task", size_hint_y=None, height=50)
        layout.add_widget(self.task_input)

        # Button to add tasks
        add_button = Button(text="Add Task", size_hint_y=None, height=50)
        add_button.bind(on_press=self.add_task)
        layout.add_widget(add_button)

        # Scrollable area for tasks
        self.scroll_view = ScrollView(size_hint=(1, None), size=(layout.width, 300))
        self.task_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.task_layout.bind(minimum_height=self.task_layout.setter('height'))
        self.scroll_view.add_widget(self.task_layout)
        layout.add_widget(self.scroll_view)

        # Button to remove selected task
        remove_button = Button(text="Remove Task", size_hint_y=None, height=50)
        remove_button.bind(on_press=self.remove_task)
        layout.add_widget(remove_button)

        # Button to mark task as completed
        complete_button = Button(text="Mark as Completed", size_hint_y=None, height=50)
        complete_button.bind(on_press=self.mark_completed)
        layout.add_widget(complete_button)

        return layout

    def add_task(self, instance):
        task = self.task_input.text.strip()
        if task:
            task_label = Label(text=f"[ ] {task}", size_hint_y=None, height=40)
            self.task_layout.add_widget(task_label)
            self.tasks.append({"text": task, "completed": False, "label": task_label})
            self.task_input.text = ""

    def remove_task(self, instance):
        if self.tasks:
            task = self.tasks.pop()
            self.task_layout.remove_widget(task["label"])

    def mark_completed(self, instance):
        if self.tasks:
            task = self.tasks[-1]  # Mark the last task as completed
            task["completed"] = not task["completed"]
            task["label"].text = f"{'[X]' if task['completed'] else '[ ]'} {task['text']}"

if __name__ == "__main__":
    ToDoApp().run()