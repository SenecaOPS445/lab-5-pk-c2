#!/usr/bin/env python3
# Author ID: [seneca_id]

def add(number1, number2):
    """
    Adds two numbers together.
    If either argument is a string that represents a number, it converts the string to an integer.
    Returns the result if successful, else returns an error message.
    """
    try:
        # Try to convert both numbers to integers if they are strings
        number1 = int(number1) if isinstance(number1, str) else number1
        number2 = int(number2) if isinstance(number2, str) else number2
        
        # Add the numbers
        return number1 + number2
    except (ValueError, TypeError):
        # If conversion fails, return error message
        return 'error: could not add numbers'


def read_file(filename):
    """
    Reads a file and returns its contents as a list of lines.
    If an error occurs, returns a string indicating the error.
    """
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except (FileNotFoundError, IOError):
        return 'error: could not read file'


if __name__ == '__main__':
    # Testing the add function with different inputs
    print(add(10, 5))                        # Should return 15
    print(add('10', 5))                      # Should return 15 (string '10' should be converted)
    print(add('abc', 5))                     # Should return error: could not add numbers
    print(add('10', '5'))                    # Should return 15 (string '10' and '5' should be converted)
    print(add('abc', '5'))                   # Should return error: could not add numbers

    # Testing the read_file function with existing and non-existing files
    print(read_file('seneca2.txt'))         # Should return the lines in the file (if it exists)
    print(read_file('file10000.txt'))       # Should return error: could not read file (file doesn't exist)
