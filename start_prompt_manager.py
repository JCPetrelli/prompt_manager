import csv
import sys
import pyperclip
from colorama import Fore, Style, init

init(autoreset=True)

def load_prompts(file_path):
    prompts = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for index, row in enumerate(reader, start=1):
            row['Number'] = index
            prompts.append(row)
    return prompts

def display_menu(prompts):
    print(Fore.MAGENTA + "Select a prompt by entering its number:")
    for prompt in prompts:
        print(f"{prompt['Number']}. {prompt['Title']}")

def get_user_choice(prompts):
    while True:
        try:
            choice = int(input(Fore.MAGENTA + "Enter your choice: "))
            if 1 <= choice <= len(prompts):
                return prompts[choice - 1]
            else:
                print(Fore.MAGENTA + "Invalid choice. Please try again.")
        except ValueError:
            print(Fore.MAGENTA + "Invalid input. Please enter a number.")

def get_variable_input(prompt_text):
    print(Fore.MAGENTA + "Enter values for variables (press Enter to use default):")
    variables = {}
    while '{' in prompt_text and '}' in prompt_text:
        start = prompt_text.index('{')
        end = prompt_text.index('}')
        variable = prompt_text[start+1:end]
        default_value = variable  # Use the variable name as the default value
        value = input(Fore.MAGENTA + f"Enter content for '{variable}' (default: {default_value}): " + Fore.YELLOW).strip()
        if not value:
            value = default_value
        variables[variable] = value
        prompt_text = prompt_text.replace(f"{{{variable}}}", f"{Fore.YELLOW}{value}{Fore.RESET}")
    return prompt_text, variables

def main():
    prompts = load_prompts('prompts.csv')
    display_menu(prompts)
    selected_prompt = get_user_choice(prompts)
    
    print(f"\nYou selected:" + Fore.YELLOW + f" {selected_prompt['Title']}")
    print(f"Prompt: {selected_prompt['Text']}")

    final_prompt, variables = get_variable_input(selected_prompt['Text'])

    print(Fore.MAGENTA + "\nFinal prompt:")
    print(final_prompt)

    # Remove color codes before copying to clipboard
    clean_prompt = final_prompt.replace(Fore.YELLOW, '').replace(Fore.RESET, '')
    pyperclip.copy(clean_prompt)
    print(Fore.MAGENTA + "\nThe final prompt has been copied to your clipboard.")

if __name__ == "__main__":
    main()