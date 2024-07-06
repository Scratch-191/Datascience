from collections import Counter  # Import the Counter class from the collections module

# Initialize variables
filename = "dataset.txt"  # The name of the file to be read
rawdict = {str(digit): [] for digit in range(10)}  # Create a dictionary with digits as keys and empty lists as values to store line numbers

# Reading from file and counting number of each character
with open(filename, 'r') as file:  # Open the file in read mode
    content = file.read()  # Read the entire content of the file into a string

# Split the content into lines
lines = content.splitlines()  # Split content into lines

# Counting number of each character and recording line numbers
counter = Counter()  # Initialize a Counter object to count character occurrences



for line_num, line in enumerate(lines, start=1):  # Iterate over each line with its line number, starting from 1
    line = line.strip()  # Remove leading and trailing whitespace from the line
    if not line:  # Skip empty lines
        continue
    counter.update(line)  # Update the counter with characters from the current line
    for char in line:  # Iterate over each character in the line
        if char in rawdict:  # Check if the character is a digit (present in rawdict)
            rawdict[char].append(line_num)  # Append the line number to the corresponding list in rawdict

# Remove entries with empty lists

rawdict = {digit: line_numbers for digit, line_numbers in rawdict.items() if line_numbers}  # Create a new dictionary excluding entries with empty lists

# Counting number of each character using Counter
data = {str(digit): counter.get(str(digit), 0) for digit in range(10)}  # Create a dictionary with counts of each digit

# Print results

print(data)  # Print the counts of each digit
for digit, line_numbers in rawdict.items():  # Iterate over each digit and its corresponding line numbers
    print(f"{digit}: {line_numbers}")  # Print the digit and the line numbers where it appears
