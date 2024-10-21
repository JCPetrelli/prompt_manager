
# Prompt Selection and Generation Script

This script is designed to assist users in selecting and filling customizable prompts from a CSV file. It allows the user to choose a prompt, input required variables, and then copies the final prompt to the clipboard for easy use.

## Features

- **CSV-Based Prompt Loading**: Prompts are stored in a CSV file (`prompts.csv`) and loaded into the script for selection.
- **Interactive Menu**: Users can select a prompt from a menu displayed in the terminal.
- **Variable Substitution**: If a prompt contains placeholders (in the form `{variable_name}`), the script will prompt the user to input the corresponding values. If no value is provided, the variable name itself is used as the default value.
- **Clipboard Copying**: Once the prompt is customized with the user's inputs, the final version (without color codes) is automatically copied to the clipboard for convenience.
- **Color-coded Output**: The script uses color-coded text to enhance the terminal interaction using the `colorama` library.

## Prerequisites

To run this script, the following Python packages must be installed:

- `pyperclip`: For copying the final prompt to the clipboard.
- `colorama`: For colored terminal output.

You can install these dependencies using pip:

```bash
pip install pyperclip colorama
```

## CSV File Format

The script expects a CSV file named `prompts.csv` with the following format:

| Number | Title  | Text                        |
|--------|--------|-----------------------------|
| 1      | Title1 | This is a prompt with {var1} |
| 2      | Title2 | Another prompt with {var2}   |

- **Number**: A unique identifier for each prompt.
- **Title**: A brief description or title of the prompt.
- **Text**: The actual prompt content, which can contain placeholders for variables, enclosed in curly braces (`{}`).

## Usage

1. **Run the Script**:
   ```bash
   python script.py
   ```

2. **Select a Prompt**: The script will display a list of available prompts, and you can select one by entering its number.

3. **Input Variables**: If the selected prompt contains placeholders, the script will ask for input values to replace them.

4. **View and Copy the Final Prompt**: The completed prompt will be displayed in the terminal, and a clean version (without terminal color codes) will be copied to your clipboard automatically.

## Example

If your `prompts.csv` file contains:

```csv
Number,Title,Text
1, Greeting,Hello {name}, welcome to {place}!
2, Reminder,Don't forget to {task} today.
```

When you select "1", the script will ask:

```
Enter content for 'name': John
Enter content for 'place': the meeting
```

The final prompt would look like:

```
Hello John, welcome to the meeting!
```

And this final version will be copied to your clipboard.

## Notes

- The script provides user-friendly error handling, ensuring invalid inputs (such as non-numeric values when selecting a prompt) are managed gracefully.
- The terminal output includes color-coding to enhance readability, but this is automatically removed from the version copied to the clipboard.

Enjoy using this customizable prompt generator!
