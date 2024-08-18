import random
import pymongo

class SpaceDetected(Exception):
    """
    Custom exception raised when a space or non-alphabetic character is detected in a name.
    """
    def __init__(self, msg):
        self.error_message = msg

    def __str__(self):
        return self.error_message

def validate_name(name):
    """
    Validates that the name contains only letters and no spaces.
    
    Args:
        name (str): The name to validate.

    Raises:
        SpaceDetected: If the name contains non-alphabetic characters or spaces.
    """
    if not name.isalpha():
        raise SpaceDetected(f"Name '{name}' should only contain letters without spaces.")
 

class Course:
    def __init__(self):
        # Connect to MongoDB
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["student_management"]  # Create/use a database
        self.collection = self.db["courses"]  # Create/use a collection
        # Predefined data
        self.data = {
            "courses": ["AI", "AIML", "CO", "CI"],
            "subjects": {
                "AI": ["Math", "Artificial Intelligence", "Python", "Machine Learning", "Deep Learning", "Data Structure"],
                "AIML": ["Python", "Deep Learning", "Data Structure", "Object-Oriented Programming", "Database Management Systems", "Problem Solving", "Robotics"],
                "CO": ["Data Structure", "Object-Oriented Programming", "Database Management Systems", "Python"],
                "CI": ["Transportation Engineering", "Environmental Engineering", "Physics", "Math", "Engineering Drawing", "Fluid Mechanics", "Foundation", "Construction Management"],
            }
        }

        # Insert predefined data into MongoDB
        self.insert_predefined_data()
    
    def insert_predefined_data(self):
            """
            Inserts the predefined courses and subjects data into the MongoDB collection if not already present.
            """
            for course_name in self.data["courses"]:
                if not self.collection.find_one({"course_name": course_name}):
                    # Insert the course and its subjects into the collection
                    self.collection.insert_one({
                        "course_name": course_name,
                        "subjects": self.data["subjects"].get(course_name, [])
                    })
                    print(f"Inserted course: {course_name} with subjects: {self.data['subjects'][course_name]}")
                else:
                    print(f"Course '{course_name}' already exists in the database.")

    def generate_course_id(self):
        """
        Generates a unique course ID by finding the highest existing course ID in the collection
        and incrementing it by 1. If no courses are found, it starts at 101.
        
        Returns:
            int: A new unique course ID.
        """
        last_course = self.collection.find_one(sort=[("_id", pymongo.DESCENDING)])
        
        if last_course:
            last_id = last_course["_id"]
            new_id = last_id + 1
        else:
            new_id = 101  # Starting course ID

        return new_id

    def add_course(self):
        """
        Adds a new course to the MongoDB database if it doesn't already exist.
        
        Prompts the user for a course name, validates it, generates a unique course ID, and then adds it to the course collection in MongoDB.
        """
        try:
            course_name = input("Enter course name: ").upper()
            validate_name(course_name)
            
            # Check if the course already exists in the MongoDB collection
            if self.collection.find_one({"course_name": course_name}) is None:
                # Generate a unique course ID
                course_id = self.generate_course_id()
                
                # Insert the new course into the MongoDB collection
                self.collection.insert_one({
                    "_id": course_id,
                    "course_name": course_name,
                    "subjects": []
                })
                print(f"{course_name} has been added successfully with Course ID: {course_id}.")
            else:
                print(f"{course_name} is already present in the database.")
        except SpaceDetected as e:
            print(e)
        except ValueError:
            print("You cannot enter a non-string type.")
        except Exception as e:
            print(e)

    def add_subject(self):
        """
        Adds a new subject to an existing course in the MongoDB database.
        
        Prompts the user for a course and subject name, validates them, and adds the subject to the specified course in the MongoDB collection.
        """
        try:
            course_name = input("Enter course name: ").upper()
            subject_name = input("Enter subject name: ").title()  # Title case for consistent formatting
            validate_name(course_name)
            validate_name(subject_name)

            # Check if the course exists in the MongoDB collection
            course = self.collection.find_one({"course_name": course_name})

            if course is None:
                print(f"Course '{course_name}' does not exist.")
                return

            # Check if the subject already exists in the course
            if subject_name in course["subjects"]:
                print(f"{subject_name} is already present in {course_name}.")
            else:
                # Add the new subject to the course's subjects list
                self.collection.update_one(
                    {"course_name": course_name},
                    {"$push": {"subjects": subject_name}}
                )
                print(f"{subject_name} added to {course_name} successfully.")

        except SpaceDetected as e:
            print(e)
        except ValueError:
            print("You cannot enter a non-string type.")
        except Exception as e:
            print(e)

    def delete_course(self):
        """
        Deletes an existing course from the MongoDB database.
        
        Prompts the user for a course name, validates it, and then removes the course and its subjects.
        """
        try:
            course_name = input("Enter course name: ").upper()
            validate_name(course_name)

            result = self.collection.delete_one({"course_name": course_name})

            if result.deleted_count > 0:
                print(f"{course_name} has been removed successfully.")
            else:
                print(f"{course_name} is not in the database.")
        except SpaceDetected as e:
            print(e)
        except ValueError:
            print("You cannot enter a non-string type.")
        except Exception as e:
            print(e)

    def delete_subject(self):
        """
        Deletes an existing subject from a specified course in the MongoDB database.
        
        Prompts the user for a course and subject name, validates them, and removes the subject from the course.
        """
        try:
            course_name = input("Enter course name: ").upper()
            subject_name = input("Enter subject name: ").title()
            validate_name(course_name)
            validate_name(subject_name)

            # Check if the course exists in the MongoDB collection
            course = self.collection.find_one({"course_name": course_name})

            if course is None:
                print(f"Course '{course_name}' does not exist.")
                return

            if subject_name not in course["subjects"]:
                print(f"{subject_name} is not present in {course_name}.")
            else:
                # Remove the subject from the course's subjects list
                self.collection.update_one(
                    {"course_name": course_name},
                    {"$pull": {"subjects": subject_name}}
                )
                print(f"{subject_name} has been removed successfully.")
        except SpaceDetected as e:
            print(e)
        except ValueError:
            print("You cannot enter a non-string type.")
        except Exception as e:
            print(e)

    def all_courses(self):
        """
        Displays a list of all available courses in the MongoDB database.
        """
        print("All courses:")
        courses = self.collection.find()
        for course in courses:
            print(f"{course['_id']}. {course['course_name']}")

    def all_subjects(self):
        """
        Displays all subjects for each course in the MongoDB database.
        """
        print("All subjects:")
        courses = self.collection.find()
        for course in courses:
            print(f"{course['course_name']}: {', '.join(course['subjects'])}")

    def search_courses(self):
        """
        Checks if a specific course is available in the MongoDB database.
        
        Prompts the user for a course name, validates it, and checks its availability.
        """
        try:
            course_name = input("Enter course name: ").upper()
            validate_name(course_name)
            course = self.collection.find_one({"course_name": course_name})
            if course:
                print(f"Course '{course_name}' is available.")
            else:
                print(f"Course '{course_name}' is not available.")
        except SpaceDetected as e:
            print(e)
        except ValueError:
            print("You cannot enter a non-string type.")
        except Exception as e:
            print(e)

    def search_subject(self):
        """
        Checks if a specific subject is available in a course in the MongoDB database.
        
        Prompts the user for a course and subject name, validates them, and checks the subject's availability in the course.
        """
        try:
            course_name = input("Enter course name: ").upper()
            subject_name = input("Enter subject name: ").title()
            validate_name(course_name)
            validate_name(subject_name)

            course = self.collection.find_one({"course_name": course_name})

            if course is None:
                print(f"Course '{course_name}' is not available.")
            else:
                if subject_name in course["subjects"]:
                    print(f"Subject '{subject_name}' is available in the course '{course_name}'.")
                else:
                    print(f"Subject '{subject_name}' is not available in the course '{course_name}'.")
        except SpaceDetected as e:
            print(e)
        except ValueError:
            print("You cannot enter a non-string type.")
        except Exception as e:
            print(e)

    def get_course_subject(self):
        """
        Displays the subjects of a specific course from the MongoDB database.
        
        Prompts the user for a course name, validates it, and lists the subjects under that course.
        """
        try:
            course_name = input("Enter a course name: ").upper()
            validate_name(course_name)

            course = self.collection.find_one({"course_name": course_name})

            if course:
                print(course.get("subjects", []))
            else:
                print(f"{course_name} is not present.")
        except SpaceDetected as e:
            print(e)

    def update_course_name(self):
        """
        Updates the name of an existing course in the MongoDB database.
        
        Prompts the user for the old and new course names, validates them, and updates the course name.
        """
        try:
            old_course_name = input("Enter the old course name: ").upper()
            new_course_name = input("Enter the new course name: ").upper()

            validate_name(old_course_name)
            validate_name(new_course_name)

            course = self.collection.find_one({"course_name": old_course_name})

            if course is None:
                print(f"{old_course_name} is not present in the database.")
            elif self.collection.find_one({"course_name": new_course_name}):
                print(f"{new_course_name} is already present.")
            else:
                self.collection.update_one(
                    {"course_name": old_course_name},
                    {"$set": {"course_name": new_course_name}}
                )
                print(f"Course name updated from {old_course_name} to {new_course_name}.")
        except SpaceDetected as e:
            print(e)
        except Exception as e:
            print(e)
    def display_menu(self):
        """
        Displays the Course Management System menu and processes user input.
        
        The menu allows the user to manage courses and subjects by selecting options.
        """
        print("\nCourse Management System")
        print("1. Add Course")
        print("2. Add Subject")
        print("3. Delete Course")
        print("4. Delete Subject")
        print("5. View All Courses")
        print("6. View All Subjects")
        print("7. Search Course")
        print("8. Search Subject")
        print("9. Find Course Subjects")
        print("10. Update Course Name")
        print("11. Exit")

        try:
            while True:
                user_choice = input("Enter your choice: ")
                if not user_choice.isdigit():
                    print("Invalid input! Please enter a number.")
                    continue

                user_choice = int(user_choice)

                if user_choice == 1:
                    self.add_course()
                elif user_choice == 2:
                    self.add_subject()
                elif user_choice == 3:
                    self.delete_course()
                elif user_choice == 4:
                    self.delete_subject()
                elif user_choice == 5:
                    self.all_courses()
                elif user_choice == 6:
                    self.all_subjects()
                elif user_choice == 7:
                    self.search_courses()
                elif user_choice == 8:
                    self.search_subject()
                elif user_choice == 9:
                    self.get_course_subject()
                elif user_choice == 10:
                    self.update_course_name()
                elif user_choice == 11:
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("You cannot enter a non-integer value.")
        except Exception as e:
            print(e)
class Student:
    def __init__(self):
        self.students = {}  # Dictionary to store student information with ID as key
    
    def generate_id(self):
        """Generates a unique 10-digit student ID."""
        minimum = pow(10, 10-1)
        maximum = pow(10, 10) - 1
        return random.randint(minimum, maximum)

    def enroll_course(self, course_obj):
        """Enrolls a student in a course."""
        student_name = input("Enter student name: ").title()
        course_name = input("Enter course name: ").upper()

        try:
            validate_name(student_name)
            validate_name(course_name)
            if course_name in course_obj.courses:
                student_id = self.generate_id()
                self.students[student_id] = {'Name': student_name, 'Course': course_name}
                print(f"Student {student_name} enrolled in {course_name} with ID: {student_id}")
            else:
                print(f"Course '{course_name}' does not exist.")
        except SpaceDetected as e:
            print(e)
        except ValueError:
            print("You cannot enter a non-string type.")
        except Exception as e:
            print(e)

    def view_students(self):
        """Displays the list of enrolled students."""
        print("Enrolled Students:")
        for student_id, student_info in self.students.items():
            print(f"ID: {student_id}, Name: {student_info['Name']}, Course: {student_info['Course']}")

    def get_student_id(self):
        name = input("Enter name of student: ").title()
        if name in [student_info['Name'] for student_info in self.students.values()]:
            student_id = list(self.students.keys())[list(student_info['Name'] for student_info in self.students.values()).index(name)]
            print("One line Code Key value:", student_id)
            return student_id
        else:
            print("Student not found.")
            return None
    def add_student(self):
        student_id = self.generate_id()
        student_name = input("Enter student name: ").title()
        self.students[student_id] = {'Name': student_name, 'Courses': []}
        print(f"Student {student_name} added with ID: {student_id}.")

    def remove_student(self):
        student_id = int(input("Enter student ID to remove: "))
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with ID {student_id} removed.")
        else:
            print("Student ID not found.")

    def get_student_name(self):
        student_id = int(input("Enter a student id: "))
        if student_id in self.students:
            return self.students[student_id]['Name']
        else:
            print("Student ID not found.")
            return None
    
    def list_all_students(self):
        if self.students:
            for student_id, info in self.students.items():
                print(f"ID: {student_id}, Name: {info['Name']}")
        else:
            print("No students available.")
    def enroll_in_multiple_courses(self):
        student_id = int(input("Enter student ID: "))
        if student_id not in self.students:
            print("Student ID not found.")
            return

        courses = input("Enter course names separated by commas: ").upper().split(',')
        enrolled_courses = self.students[student_id].get('Courses', [])
        for course in courses:
            course = course.strip()
            if course not in enrolled_courses:
                enrolled_courses.append(course)
        
        self.students[student_id]['Courses'] = enrolled_courses
        print(f"Student ID {student_id} enrolled in courses: {', '.join(courses)}.")

    def list_enrolled_courses(self):
        student_id = int(input("Enter student ID: "))
        if student_id in self.students:
            courses = self.students[student_id].get('Courses', [])
            if courses:
                print(f"Courses for student ID {student_id}: {', '.join(courses)}")
            else:
                print("No courses enrolled.")
        else:
            print("Student ID not found.")

    def update_enrolled_courses(self):
        student_id = int(input("Enter student ID: "))
        if student_id not in self.students:
            print("Student ID not found.")
            return

        action = input("Do you want to 'add' or 'remove' courses? ").lower()
        if action not in ['add', 'remove']:
            print("Invalid action.")
            return

        courses = input("Enter course names separated by commas: ").upper().split(',')
        enrolled_courses = self.students[student_id].get('Courses', [])

        if action == 'add':
            for course in courses:
                course = course.strip()
                if course not in enrolled_courses:
                    enrolled_courses.append(course)
        elif action == 'remove':
            for course in courses:
                course = course.strip()
                if course in enrolled_courses:
                    enrolled_courses.remove(course)
        
        self.students[student_id]['Courses'] = enrolled_courses
        print(f"Student ID {student_id} courses updated.")

    def search_students_by_course(self):
        course_name = input("Enter course name to search: ").upper()
        found_students = [id for id, info in self.students.items() if course_name in info['Courses']]
        
        if found_students:
            for student_id in found_students:
                print(f"ID: {student_id}, Name: {self.students[student_id]['Name']}")
        else:
            print(f"No students enrolled in {course_name}.")
    def update_student_info(self):
        student_id = int(input("Enter student ID to update: "))
        if student_id not in self.students:
            print("Student ID not found.")
            return

        new_name = input("Enter new name (leave empty to keep current): ").title()
        if new_name:
            validate_name(new_name)
            self.students[student_id]['Name'] = new_name
            print(f"Student ID {student_id} name updated to {new_name}.")
        else:
            print("No changes made to name.")

    def get_student_count(self):
        count = len(self.students)
        print(f"Total number of students: {count}")
        return count

    def search_student_by_name(self):
        name = input("Enter student name to search: ").title()
        found_students = {id: info for id, info in self.students.items() if info['Name'] == name}
        
        if found_students:
            for student_id, info in found_students.items():
                print(f"ID: {student_id}, Name: {info['Name']}, Courses: {', '.join(info.get('Courses', []))}")
        else:
            print("No student found with that name.")

    def update_student_name(self):
        student_id = int(input("Enter student ID to update name: "))
        if student_id in self.students:
            new_name = input("Enter new name: ").title()
            validate_name(new_name)
            self.students[student_id]['Name'] = new_name
            print(f"Student ID {student_id} name updated to {new_name}.")
        else:
            print("Student ID not found.")

    def is_enrolled_in_course(self):
        student_id = int(input("Enter student ID: "))
        course_name = input("Enter course name: ").upper()
        
        if student_id in self.students:
            courses = self.students[student_id].get('Courses', [])
            if course_name in courses:
                print(f"Student ID {student_id} is enrolled in {course_name}.")
            else:
                print(f"Student ID {student_id} is not enrolled in {course_name}.")
        else:
            print("Student ID not found.")
    def remove_student_from_course(self):
        student_id = int(input("Enter student ID: "))
        course_name = input("Enter course name to remove: ").upper()

        if student_id in self.students:
            courses = self.students[student_id].get('Courses', [])
            if course_name in courses:
                courses.remove(course_name)
                self.students[student_id]['Courses'] = courses
                print(f"Student ID {student_id} removed from {course_name}.")
            else:
                print(f"Student ID {student_id} is not enrolled in {course_name}.")
        else:
            print("Student ID not found.")

    def display_menu(self, course_obj):
        """Displays the CLI menu for student management and processes user input."""
        try:
            while True:
                print("\nStudent Management System")
                print("1. Enroll Student")
                print("2. View Enrolled Students")
                print("3. Find ID by Name")
                print("4. Find Name by ID")
                print("5. Search Student by Name")
                print("6. Update Student Name")
                print("7. Check Enrollment in a Course")
                print("8. Remove Student from a Course")
                print("9. Exit")
                
                user_choice = input("Enter your choice: ")
                if not user_choice.isdigit():
                    print("Invalid input! Please enter a number.")
                    continue

                user_choice = int(user_choice)

                if user_choice == 1:
                    self.enroll_course(course_obj)
                elif user_choice == 2:
                    self.view_students()
                elif user_choice == 3:
                    self.get_student_id()
                elif user_choice == 4:
                    print(self.get_student_name())
                elif user_choice == 5:
                    self.search_student_by_name()
                elif user_choice == 6:
                    self.update_student_name()
                elif user_choice == 7:
                    self.is_enrolled_in_course()
                elif user_choice == 8:
                    self.remove_student_from_course()
                elif user_choice == 9:
                    print("Exiting the system.")
                    break
                else:
                    print("Invalid choice! Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example of running both Course and Student management systems together
if __name__ == "__main__":

    course_obj = Course()
    student_obj = Student()

    while True:
        print("\nMain Menu")
        print("1. Manage Courses")
        print("2. Manage Students")
        print("3. Exit")

        main_choice = input("Enter your choice: ")

        if main_choice == '1':
            course_obj.display_menu()
        elif main_choice == '2':
            student_obj.display_menu(course_obj)
        elif main_choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 3.")