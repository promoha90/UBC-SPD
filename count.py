import PyPDF2
import re

# Function to extract the numbers that appear before "min"
def extract_numbers_before_min(pdf_path):
    # Open the PDF file in binary read mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # List to store the extracted numbers
        numbers = []
        
        # Iterate through all the pages of the PDF
        for page in pdf_reader.pages:
            # Extract the text from the page
            text = page.extract_text()
            
            # Find all occurrences of numbers followed by exactly one space and then "min"
            matches = re.findall(r'(\d+)\smin', text)
            
            # Convert the numbers from strings to integers and add them to the list
            numbers.extend(int(num) for num in matches)
        
    return numbers

# Function to sum the extracted numbers
def sum_numbers_before_min(numbers):
    return sum(numbers)

# Usage of the functions
pdf_path = r'Problem Bank.pdf'
numbers_before_min = extract_numbers_before_min(pdf_path)
total_sum = sum_numbers_before_min(numbers_before_min)

# Display the total sum of the numbers found
print("Total:", total_sum, "minutes")
