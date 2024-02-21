# ------------------------------------------------------------------------------------------ #
# Title: Assignment06DusanS
# Desc: This assignment demonstrates using classes and separations of concerns
# Change Log: (Who, When, What)
#   DusanS,2/19/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import json


# Define the Data Constants

MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""

FILE_NAME: str = "Enrollments.json"

# End of Constants

# Define the Data Variables

students: list = []
menu_choice: str = ""

# End of Variables

# Create Classes


class FileProcessor:
    """
    This class contains functions designed to work with JSON files, reading data and writing it to file.
    DusanS,2/19/2024,Created class File Processor

    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads the json file and stores the data into a list of dictionaries.
        DusanS,2/19/2024,Created function read_data_from_file

        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes the data from a list of dictionaries to a json file.
        DusanS,2/19/2024,Created function write_data_to_file

        """
        try:
            file = open(file_name, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!\n")
            for student in student_data:
                print(f'{student["FirstName"]},{student["LastName"]} was registered for {student["CourseName"]}')
        except Exception as e:
            if not file.closed:
                file.close()
            IO.output_error_messages("There was a problem saving data to file.", e)


class IO:
    """
    This class contains functions designed to manage user input and output.
    DusanS,2/19/2024,Created class IO

    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays a custom error message to the user.
        DusanS,2/19/2024,Created function output_error_messages

        """
        print(message, end="\n")
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays a menu of choices to the user.
        DusanS,2/19/2024,Created function output_menu

        """
        print(menu, end="\n")

    @staticmethod
    def input_menu_choice():
        """
        This function gets the user input from the menu of choices.
        DusanS,2/19/2024,Created function input_menu_choice

        """

        choice = input("What would you like to do: ")
        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function gets the user input for the student's first name, last name and course name.
        DusanS,2/19/2024,Created function input_student_data

        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("User input can only contain alphabetical characters.", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return students

    @staticmethod
    def output_student_course(student_data: list):
        """
        This function displays the course information to the user.
        DusanS,2/19/2024,Created function output_student_course

        """
        print("-" * 50)
        for student in student_data:
            print(f'{student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

# End of function definitions

# Main body of this script


students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":
        IO.output_student_course(student_data=students)
        continue

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":
        break  # out of the loop

    else:
        print ("Invalid option, please only choose one of the following: 1,2,3 or 4.")

print ("Program ended.")