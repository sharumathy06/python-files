# Grade Calculator

while True:
    # Ask for student's name
    name = input("Enter the student's name (or 'Exit' to quit): ")
    
    if name.lower() == "exit":
        print("Exiting the program.")
        break
    
    # Ask for 3 subject marks
    mark1 = float(input("Enter mark for subject 1: "))
    mark2 = float(input("Enter mark for subject 2: "))
    mark3 = float(input("Enter mark for subject 3: "))
    
    # Calculate the average
    average = (mark1 + mark2 + mark3) / 3
    
    # Determine the grade
    if average >= 75:
        result = "A"
    elif average >= 60:
        result = "B"
    elif average >= 40:
        result = "C"
    else:
        result = "F"
    
    # Print the result with formatting
    print("-----------------------")
    print(f"Name: {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {result}")
    print("-----------------------")
    print()  # Blank line for separation
