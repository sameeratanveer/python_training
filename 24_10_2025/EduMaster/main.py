from platform import EduPlatform
from users import Admin, Instructor, Student
from courses import Lesson

# Setup platform
platform = EduPlatform()

# Create a default admin
default_admin = Admin(platform.user_id_counter, "Admin", "admin@edu.com", "admin123")
platform.user_id_counter += 1
platform.add_user(default_admin)


def admin_menu(admin):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Create Instructor")
        print("2. Create Student")
        print("3. Create Course")
        print("4. View Platform Stats")
        print("5. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Instructor Name: ")
            email = input("Instructor Email: ")
            password = input("Password: ")
            admin.create_instructor(platform, name, email, password)
        elif choice == "2":
            name = input("Student Name: ")
            email = input("Student Email: ")
            password = input("Password: ")
            admin.create_student(platform, name, email, password)
        elif choice == "3":
            title = input("Course Title: ")
            description = input("Course Description: ")
            email = input("Instructor Email: ")
            instructor = platform.get_user(email)
            if isinstance(instructor, Instructor):
                admin.create_course(platform, title, description, instructor)
            else:
                print("Invalid instructor email.")
        elif choice == "4":
            admin.platform_stats(platform)
        elif choice == "5":
            admin.logout()
            break
        else:
            print("Invalid choice!")


def instructor_menu(inst):
    while True:
        print("\n--- Instructor Menu ---")
        print("1. Create Course")
        print("2. Add Lesson to Course")
        print("3. View Lessons of a Course")
        print("4. Grade Student")
        print("5. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Course Title: ")
            description = input("Course Description: ")
            inst.create_course(platform, title, description)
        elif choice == "2":
            for idx, course in enumerate(inst.courses_taught, 1):
                print(f"{idx}. {course.title}")
            c_idx = int(input("Select course number: ")) - 1
            course = inst.courses_taught[c_idx]
            lesson_title = input("Lesson Title: ")
            lesson_content = input("Lesson Content: ")
            lesson = inst.add_lesson(course, lesson_title, lesson_content)
            publish = input("Publish now? (y/n): ").lower()
            if publish == "y":
                lesson.publish()
        elif choice == "3":
            for idx, course in enumerate(inst.courses_taught, 1):
                print(f"{idx}. {course.title}")
            c_idx = int(input("Select course number: ")) - 1
            course = inst.courses_taught[c_idx]
            inst.view_enrolled_lessons(course)
        elif choice == "4":
            for idx, course in enumerate(inst.courses_taught, 1):
                print(f"{idx}. {course.title}")
            c_idx = int(input("Select course number: ")) - 1
            course = inst.courses_taught[c_idx]
            for idx, student in enumerate(course.enrolled_students, 1):
                print(f"{idx}. {student.name}")
            s_idx = int(input("Select student number: ")) - 1
            student = course.enrolled_students[s_idx]
            assessment_name = input("Assessment Name: ")
            score = float(input("Score: "))
            inst.grade_student(course, student, assessment_name, score)
        elif choice == "5":
            inst.logout()
            break
        else:
            print("Invalid choice!")


def student_menu(stud):
    while True:
        print("\n--- Student Menu ---")
        print("1. Browse Courses")
        print("2. Enroll in Course")
        print("3. View Lessons")
        print("4. Submit Assignment/Quiz")
        print("5. View Progress")
        print("6. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            stud.browse_courses(platform)
        elif choice == "2":
            title = input("Course Title to Enroll: ")
            course = platform.get_course(title)
            if course:
                stud.enroll(course)
        elif choice == "3":
            title = input("Course Title: ")
            course = platform.get_course(title)
            if course and course in stud.enrolled_courses:
                stud.view_lessons(course)
            else:
                print("You are not enrolled in this course.")
        elif choice == "4":
            title = input("Course Title: ")
            course = platform.get_course(title)
            if course and course in stud.enrolled_courses:
                assessment = input("Assessment Name: ")
                score = float(input("Score: "))
                stud.submit_assignments(course, assessment, score)
            else:
                print("You are not enrolled in this course.")
        elif choice == "5":
            stud.view_progress()
        elif choice == "6":
            stud.logout()
            break
        else:
            print("Invalid choice!")


def main():
    print("Welcome to EduPlatform CLI")
    while True:
        print("\n--- Login ---")
        email = input("Email: ")
        password = input("Password: ")
        user = platform.get_user(email)
        if user and user.login(email, password):
            if isinstance(user, Admin):
                admin_menu(user)
            elif isinstance(user, Instructor):
                instructor_menu(user)
            elif isinstance(user, Student):
                student_menu(user)
        else:
            print("Login failed. Try again.")


if __name__ == "__main__":
    main()
