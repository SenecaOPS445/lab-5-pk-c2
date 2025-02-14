#!/usr/bin/env python3
# Author ID: [seneca_id]

def read_file_string(file_name):
    """
    Takes file_name as a string for a file name,
    returns its entire contents as a string.
    """
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: {file_name} not found."

def read_file_list(file_name):
    """
    Takes a file_name as a string for a file name,
    returns its entire contents as a list of lines without new-line characters.
    """
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return [f"Error: {file_name} not found."]

def append_file_string(file_name, string_of_lines):
    """
    Takes a file name and a string of lines,
    appends the string of lines to the file.
    """
    try:
        with open(file_name, 'a') as file:
            file.write(string_of_lines)
            print(f"Data successfully appended to {file_name}")
    except IOError as e:
        print(f"An error occurred while appending to {file_name}: {e}")

def write_file_list(file_name, list_of_lines):
    """
    Takes a file name and a list of lines,
    writes each item of the list to the file, each on a new line.
    """
    try:
        with open(file_name, 'w') as file:
            for line in list_of_lines:
                file.write(line + '\n')
            print(f"Data successfully written to {file_name}")
    except IOError as e:
        print(f"An error occurred while writing to {file_name}: {e}")

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """
    Takes two file names, reads data from the first file,
    writes data to the second file, and adds line numbers to the start of each line.
    """
    try:
        with open(file_name_read, 'r') as infile, open(file_name_write, 'w') as outfile:
            line_number = 1
            for line in infile:
                outfile.write(f"{line_number}:{line}")
                line_number += 1
            print(f"Data with line numbers copied from {file_name_read} to {file_name_write}")
    except IOError as e:
        print(f"An error occurred while reading/writing files: {e}")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    
    # Append string to file1
    append_file_string(file1, string1)
    print(read_file_string(file1))
    
    # Write list to file2
    write_file_list(file2, list1)
    print(read_file_string(file2))
    
    # Copy data with line numbers from file2 to file3
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))

