
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

| Title  | Text                        |
|--------|-----------------------------|
| Title1 | This is a prompt with {var1} |
| Title2 | Another prompt with {var2}   |

- **Title**: A brief description or title of the prompt.
- **Text**: The actual prompt content, which can contain placeholders for variables, enclosed in curly braces (`{}`).

Note: The 'Number' column is no longer required in the CSV file. The script will automatically assign numbers to the prompts when displaying the menu.

## Usage

1. **Run the Script**:
   ```bash
   python start_prompt_manager.py
   ```

2. **Select a Prompt**: The script will display a list of available prompts, and you can select one by entering its number.

3. **Input Variables**: If the selected prompt contains placeholders, the script will ask for input values to replace them.

4. **View and Copy the Final Prompt**: The completed prompt will be displayed in the terminal, and a clean version (without terminal color codes) will be copied to your clipboard automatically.

## Example

If your `prompts.csv` file contains:

```csv
Title,Text
Learn any new skill,"I want to learn {desired skill}. Create a 30-day learning plan to help a beginner like me learn and improve this skill."
```

When you select this prompt, the script will ask:

```
Enter content for 'desired skill': How to work with LLMs
```

The final prompt would look like:

```
"I want to learn How to work with LLMs. Create a 30-day learning plan to help a beginner like me learn and improve this skill."
```

And this final version will be copied to your clipboard.

## Notes

- The script provides user-friendly error handling, ensuring invalid inputs (such as non-numeric values when selecting a prompt) are managed gracefully.
- The terminal output includes color-coding to enhance readability, but this is automatically removed from the version copied to the clipboard.

## Customizing Prompts

Feel free to use the prompts already contained in `prompts.csv` as a starting point, but don't hesitate to add, edit, and customize them as you see fit. The provided prompts are just examples, and you can tailor them to your specific needs or create entirely new ones. 


## Additional Prompts Storage

The `additional_prompts.csv` file is not directly linked to the script. This file serves as a repository for prompts that you may not need at the moment but would like to store for future use. It's a great place to keep a collection of prompts that you find interesting or potentially useful, without cluttering the main `prompts.csv` file.

Feel free to add new prompts to `additional_prompts.csv` as you come across them. This can include:

- Prompts you've created but aren't ready to use yet
- Prompts you've found from other sources
- Variations of existing prompts
- Specialized prompts for specific tasks or projects

When you decide you want to use a prompt from `additional_prompts.csv`, you can simply copy it to the `prompts.csv` file, and it will become available in the prompt manager.

## Contributing

If you have any suggestions or improvements for this script, please feel free to contribute to the project. You can fork the repository, make your changes, and submit a pull request.

Enjoy!


