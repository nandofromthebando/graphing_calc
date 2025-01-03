import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import math

kivy.require('2.1.0')

class Calculator(App):
    def build(self):
        self.operators = ["/", "*", "-", "+", "^"]
        self.last_was_operator = None
        self.last_button = None
        self.history = []

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Solution and History Display
        self.solution = TextInput(font_size=75, readonly=True, halign="right", multiline=False, size_hint=(1, 0.1))
        self.history_label = Label(text="", font_size=16, size_hint_y=None, height=40, halign="left", valign="top")
        self.history_label.bind(size=self.history_label.setter('text_size'))
        main_layout.add_widget(self.history_label)
        main_layout.add_widget(self.solution)

        # Buttons Layout
        buttons_layout = GridLayout(cols=4, padding=10, spacing=10)
        buttons = [
            'C', '+', '-', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '(', ')', '^', '=', '.',
            'sin', 'cos', 'tan', 'log',
            '%', 'sqrt', 'DEL'
        ]
        for button in buttons:
            buttons_layout.add_widget(self.create_button(button))
        main_layout.add_widget(buttons_layout)

        Window.bind(on_key_down=self.on_key_down)

        return main_layout

    def create_button(self, text):
        button = Button(
            text=text,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            font_size=50,
            background_color=(0.3, 0.3, 0.3, 1),
            on_press=self.on_button_press
        )
        return button

    def on_button_press(self, instance):
        self.process_input(instance.text)

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        print(f"Key down event: keycode={keycode}, text={text}, modifiers={modifiers}")
        if text is not None:  # Check if text is not None
            if text.isdigit() or text in self.operators or text in "()^.":
                self.process_input(text)
        elif keycode == 40:  # Enter key
            self.process_input('=')
        elif keycode == 42:  # Backspace key
            self.process_input('DEL')
        elif keycode == 6:  # C key for clearing input
            self.process_input('C')
        else:
            numpad_keys = {
                89: '1', 90: '2', 91: '3',
                92: '4', 93: '5', 94: '6',
                95: '7', 96: '8', 97: '9',
                98: '0', 99: '.', 85: '*', 86: '-', 87: '+', 84: '/'
            }
            if keycode in numpad_keys:
                self.process_input(numpad_keys[keycode])

    def process_input(self, input_text):
        current = self.solution.text

        if input_text == 'C':
            self.solution.text = ''
        elif input_text == 'DEL':
            self.backspace()
        elif input_text == '=':
            try:
                # Replace custom symbols with Python equivalents
                expression = current.replace('^', '**')
                expression = expression.replace('sqrt', 'math.sqrt')
                for func in ['sin', 'cos', 'tan']:
                    expression = expression.replace(func, f'math.{func}')
                
                # Evaluate the expression
                result = str(eval(expression))
                self.history.append(f"{current} = {result}")
                self.update_history()
                self.solution.text = result
            except ZeroDivisionError:
                self.solution.text = 'Error: Division by zero'
            except Exception as e:
                self.solution.text = 'Error: Invalid input'
        else:
            if current == '' and input_text in self.operators:
                return
            elif current and self.last_was_operator and input_text in self.operators:
                return
            else:
                new_text = current + input_text
                self.solution.text = new_text

        self.last_button = input_text
        self.last_was_operator = input_text in self.operators
    def backspace(self):
        # Remove the last character from the TextInput
        if self.solution.text:
            self.solution.text = self.solution.text[:-1]
if __name__ == '__main__':
    Calculator().run()
