import sys

def process_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_text = file.read().lower()
    except IndexError:
        sys.exit("Error: No file name provided")
    except FileNotFoundError:
        sys.exit(f"Error: File '{file_name}' not found")
    except IOError:
        sys.exit(f"Error: Unable to open or read file '{file_name}'")
    return file_text.strip().split(';')

def unary_to_string(unary):
    return len(unary)

def convert_numbers_to_ascii_letters(s):
    def digit_to_ascii_letter(digit):
        return chr(ord('A') + int(digit) - 1)
    result = ''.join(digit_to_ascii_letter(char) if char.isdigit() else char for char in s)
    return result

def main():
    file_name = sys.argv[1]
    file_lines = process_file(file_name)
    program_counter = 0
    while program_counter < len(file_lines):
        program_counter += 1
        file_line = file_lines.pop(0)
        line_words = file_line.split('-')
        word = ""
        for line_word in line_words:
            if '.' not in line_word:
                raise("Error: Code must contain only . and -.")
            else:
                word_unary = unary_to_string(line_word)
                word_letter = convert_numbers_to_ascii_letters(word_unary)
                word = word + word_letter
        exec(word)