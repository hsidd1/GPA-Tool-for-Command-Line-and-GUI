#Author: Hamza Siddiqui
#Date: 2023-01-08
'''
A program to track grades and view and edit them directly in terminal instead of logging into portal and checking each term's grade and requesting a transcript.
Courses can be added directly from the txt file or from terminal using -a COURSE_NAME LETTER_GRADE CREDITS
Courses can be removed directly from the txt file or from terminal using -r COURSE_NAME
Course list can be cleared from terminal using -c
'''

import sys
# Can change file name directly (if needed) or input from terminal
filename = sys.argv[1] if len(sys.argv) > 1 else "courses.txt" # <-- CHANGE HERE

# Map letter grades to GPA values
grade_points = {
    'A+': 4.0,
    'A': 3.9,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'D-': 0.7,
    'F': 0.0
}

# List to store courses and their grades
courses = []

# Function to add a course to the list
# Use from command line with '-a "Course" "Grade" "Credits"' ... Example: -a MATH100 A- 3
def add_course(course, grade, credits):
  courses.append((course, grade, credits))

# Function to remove a course from file and list
# Use in command line with '-r "Course"' ... Example: -r MATH100
def remove_course(course):
  with open(filename, "r") as f:
    info = f.readlines()
  
  for i, line in enumerate(info):
    c, g, cr = line.strip().split()
    # Check if the course name matches the argument
    if c == course:
      info.pop(i)
      courses.remove((c,g,cr))
      break
  else:
    print(f"{course} is not in the list.")
  
  with open(filename, "w") as f:
    f.writelines(info)


# Function to calculate the GPA
def calculate_gpa(courses):
  total_grade_points = 0
  total_credits = 0
  for course in courses:
    course_name = course[0]
    course_grade = course[1]
    course_credits = float(course[2]) 
    total_grade_points += grade_points[course_grade] * course_credits
    total_credits += course_credits
  try:
    return total_grade_points / total_credits
  except ZeroDivisionError:
    print("No credits exist.")
    return 0

# Function to clear all courses from file
# Use in command line with "-c"
def clear_courses():
  response = input("Are you sure you want to clear all courses? This will also clear the courses from the courses.txt file. (y/n) ")
  if response == "y":
    courses.clear()
    with open(filename, "w") as f:
      f.write("")
  else:
    print("Courses were not cleared.")

#Function to get courses
def get_courses():
  # Read data from text file
  line_number = 0  # Counter to keep track of line number in case of ouput
  try:
    # Read data from text file
    with open(filename, "r") as f:
      for line in f:
        line_number += 1  # Increment the line number
        try:
          course, grade, credits = line.strip().split()
          add_course(course, grade, credits)
        except ValueError:
          # Incorrect format in file
          print(f"Error: Invalid course input in line {line_number} of courses.txt. Each line should contain a course name, a grade, and the number of credits, separated by a single space.\nExample: MATH1ZB3 A- 3")
          sys.exit("Fix errors and try again") # Stop reading the file
  except IOError:
    print("Error: courses.txt does not exist or cannot be opened.")

def main():
  get_courses()
  # Parse command line arguments
  for i in range(2, len(sys.argv)):
    if sys.argv[i] == '-a':
      try:
        course, grade, credits = sys.argv[i+1], sys.argv[i+2], sys.argv[i+3]
        add_course(course, grade, credits)
        # Write data to text file
        with open(filename, "w") as f:
          for course in courses:
            course_name = course[0]
            course_grade = course[1]
            course_credits = course[2]
            f.write(f"{course_name} {grade} {credits}\n")
      except ValueError:
        print("Error: Invalid input for adding a course. Please provide a course name, grade, and number of credits, separated by a single space.\nExample: -a MATH1ZB3 A- 3")
    elif sys.argv[i] == '-r':
      remove_course(sys.argv[i+1])
    elif sys.argv[i] == '-c':
      clear_courses()
  # Output courses and grades in a table-like format
  print("Course               Grade\n--------------------------")
  for course in courses:
    course_name = course[0]
    course_grade = course[1]
    print(f"{course_name:<20} {course_grade}")


  # Calculate and output GPA
  gpa = calculate_gpa(courses)
  print(f"GPA: {gpa:.2f}")

if __name__ == "__main__":
  main()
