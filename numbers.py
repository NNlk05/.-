def process_numbers(input_string):
    numbers = input_string.split()
    result = ""
    
    while numbers:
        first_number = int(numbers.pop(0))
        result += '.' * first_number + '-'
        
    # Remove the trailing dash
    if result.endswith('-'):
        result = result[:-1]
        
    return result

def main():
    input_string = input("Enter a string of numbers separated by spaces: ")
    output = process_numbers(input_string)
    print(f"Processed output: {output}")

if __name__ == "__main__":
    main()