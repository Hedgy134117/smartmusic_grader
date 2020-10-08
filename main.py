from selenium import webdriver
import json

# install up to date version from https://chromedriver.chromium.org/
# Open up an automated chrome window
browser = webdriver.Chrome('chromedriver.exe')
browser.get('file:///C:/dev/Software/smartmusic_grader/smartmusic/index.html')

# Grades Dictionary (stores each student's grades)
grades = {}

# Find the grade table
table = browser.find_elements_by_class_name('grid-table')[0]

# Find all assignments
assignmentContainers = browser.find_elements_by_class_name('grid-assignment-header')

# Get all assignment names
assignments = [assignment.find_element_by_class_name('ellipsis').text for assignment in assignmentContainers]

# Find all students
studentContainers = browser.find_elements_by_class_name('grid-student-row')

# Go through each student
for studentContainer in studentContainers:
    # Get the name of the student
    studentName = studentContainer.find_element_by_class_name('grid-student-header').text
    # Put the student in the final grades dictionary
    grades[studentName] = {}
    # Go through each assignment
    for assignment in assignments:
        # Get the grade of the assignment for the student
        grade = studentContainer.find_elements_by_class_name('grid-assignment-cell')[assignments.index(assignment)].find_element_by_class_name('student-assignment').text
        # Put the grade in the grade dictionary
        grades[studentName][assignment] = grade

# Write the final grades to a json file
with open('grades.json', 'w') as jsonFile:
    json.dump(grades, jsonFile, indent=4, sort_keys=True)
