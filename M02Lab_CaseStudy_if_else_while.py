""" 
Title: Dean's List and Honor Roll Qualification Test
Author: Emma Kaufman
Description: This application will accept the last name, first name,
and GPA of a given student. From there there will be a series of 
qualification tests performed on the student's entered GPA. 
From there, the program will determine if the student made either the 
Dean's List or Honor Roll.
Variable(s): LName(str) student last name, FName(str) student first name,
GPA(float) student GPA
Date Last Modified: 06/17/2025
"""

while True: #creates a loop that continues accepting student names and GPAs until the sentinel value 'ZZZ' is entered
    LName = input("Enter Last Name, or 'ZZZ' to quit: ") #prompt for student's last name, or 'ZZZ' to quit the program
    if LName.upper() == 'ZZZ': #exit the loop (and program) if the sentinel value 'ZZZ' is entered
        break
            
    FName = input("Enter First Name: ") #prompt for student's first name

    while True: #loop until a valid GPA (float) is entered
        try:
            GPA = float(input("Enter GPA in X.XX format: ")) #prompt for student's GPA and convert input to a float
            break #exit GPA input loop once a valid GPA is entered
        except ValueError: #handle invalid GPA input and prompt user again
            print("Invalid GPA format. Please enter a valid numeric value like 3.14.")
        
    if GPA >= 3.5: #check if student qualifies for Dean's List (GPA 3.5 or higher)
        print(f"{FName} {LName} made the Dean's List.")
    elif GPA >= 3.25: #check if student qualifies for Honor Roll (GPA between 3.25 and 3.49)
        print(f"{FName} {LName} made the Honor Roll.")
    else: #student did not qualify for either Dean's List or Honor Roll
        print(f"{FName} {LName} did not make the Dean's List or Honor Roll.")    
    