# Calculator App

This project is a simple **Calculator App** built using the Kivy framework for Python. It provides a graphical user interface (GUI) for performing basic mathematical calculations as well as trigonometric and logarithmic operations.

## Features

- **Basic Arithmetic**: Addition, subtraction, multiplication, and division.
- **Advanced Operations**:
  - Trigonometric functions: `sin`, `cos`, `tan`.
  - Square root (`sqrt`), exponentiation (`^`), and logarithm (`log`).
- **Keyboard Support**:
  - Use the keyboard for numeric and operator input.
  - Special keys like `Enter` for equals, `Backspace` for delete, and `C` for clearing the input.
- **History Display**: Shows the last performed calculations (limited implementation).

## Requirements

- Python 3.8+
- Kivy 2.1.0+
- Math module (built into Python)

## Installation

1. Clone or download the repository.
2. Install the required dependencies:

   ```bash
   pip install kivy
   ```

3. Run the application:

   ```bash
   python calculator.py
   ```

## Usage

- Launch the application to open the calculator window.
- Use the on-screen buttons or keyboard to input calculations.
- Supported buttons:
  - `C`: Clear the current input.
  - `DEL`: Delete the last character.
  - `=`: Evaluate the current expression.
  - `sin`, `cos`, `tan`: Trigonometric functions.
  - `sqrt`: Square root.
  - `log`: Logarithm (base 10).
  - `^`: Exponentiation.
  - `%`: Percentage.

## Key Bindings

- **Numbers and Operators**: Direct input from the keyboard (e.g., `1`, `+`, `-`) (For Mac OS keyboard mapping only).
- **Special Keys**:
  - `Enter`: Evaluate the expression.
  - `Backspace`: Delete the last character.
- **Numpad Support**: Handles numpad keys for numbers and operators.

## Code Structure

- **`Calculator` Class**:
  - Handles UI creation and event processing.
  - Processes input from buttons and keyboard.
  - Performs mathematical operations and updates the display.

- **Key Methods**:
  - `process_input(input_text)`: Processes user input and updates the display.
  - `on_button_press(instance)`: Handles button press events.
  - `on_key_down(instance, keyboard, keycode, text, modifiers)`: Handles keyboard events.
  - `backspace()`: Deletes the last character from the input.

## Limitations

- **Trigonometric Functions**: Arguments for `sin`, `cos`, and `tan` must be in radians.
- **Logarithm**: Only supports base 10.

## License

This project is licensed under the MIT License.

---
