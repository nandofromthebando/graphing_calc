import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

kivy.require('2.1.0')


class Calculator(App):
    def build(self):
        self.operators = ["/", "*", "-", "+", "^"]
        self.last_was_operator = None
        self.last_button = None

        self.solution = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        main_layout = GridLayout(cols=4, padding=10, spacing=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', 'C', '+',
            '(', ')', '^', '=',
        ]

        main_layout.add_widget(self.solution)
        for button in buttons:
            main_layout.add_widget(self.create_button(button))

        Window.bind(on_key_down=self.on_key_down)

        return main_layout

    def create_button(self, text):
        button = Button(
            text=text,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            font_size=24,
            on_press=self.on_button_press
        )
        return button

    def on_button_press(self, instance):
        self.process_input(instance.text)

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        print(f"Key pressed - keycode: {keycode}, text: {text}, scancode: {keyboard}")
        if text.isdigit() or text in self.operators or text in "()^.":
            self.process_input(text)
        elif keycode == 40:  # Enter key
            self.process_input('=')
        elif keycode == 42:  # Backspace key
            self.solution.text = self.solution.text[:-1]
        elif keycode in [46, 67]:  # C key for clearing input (main keyboard and numpad)
            self.solution.text = ''
        else:
            numpad_keys = {
                89: '1', 90: '2', 91: '3',
                83: '4', 84: '5', 85: '6',
                79: '7', 80: '8', 81: '9',
                82: '0', 86: '.', 75: '*', 78: '-', 69: '+', 98: '/', 96: '='
            }
            if keycode in numpad_keys:
                self.process_input(numpad_keys[keycode])

    def process_input(self, input_text):
        current = self.solution.text

        if input_text == 'C':
            self.solution.text = ''
        elif input_text == '=':
            try:
                self.solution.text = str(eval(self.solution.text.replace('^', '**')))
            except Exception as e:
                self.solution.text = 'Error'
        else:
            if current and (self.last_was_operator and input_text in self.operators):
                return
            elif current == '' and input_text in self.operators:
                return
            else:
                new_text = current + input_text
                self.solution.text = new_text

        self.last_button = input_text
        self.last_was_operator = self.last_button in self.operators


if __name__ == '__main__':
    Calculator().run()
