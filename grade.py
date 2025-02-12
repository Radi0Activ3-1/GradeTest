# Function to determine the letter grade based on numeric input
def get_letter_grade(grade):
    if 90 <= grade <= 100:
        return "A"
    elif 80 <= grade < 90:
        return "B"
    elif 70 <= grade < 80:
        return "C"
    elif 60 <= grade < 70:
        return "D"
    else:
        return "F"

# Main program execution
try:
    # Accept numeric grade input
    grade = int(input("Enter the numeric grade (0-100): "))

    # Validate input range
    if 0 <= grade <= 100:
        print(f"The letter grade is: {get_letter_grade(grade)}")
    else:
        print("Error: Please enter a number between 0 and 100.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
