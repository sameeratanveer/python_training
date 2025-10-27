from abc import ABC, abstractmethod
from reports import ProgressReport
from courses import Course, Lesson

class BaseUser(ABC):
    """
    Base class for all users in the platform.
    """
    def __init__(self, id, name, email, password='1234', role='user', is_logged_in=False):
        self.id = id
        self.name = name
        self.email = email
        self.__password = password
        self.role = role
        self.is_logged_in = is_logged_in

    def login(self, email, password):
        """Login user if email/password match."""
        if email == self.email and password == self.__password:
            self.is_logged_in = True
            print(f"{self.name} logged in successfully!")
            return True
        print("Login failed: email/password mismatch.")
        return False

    def logout(self):
        """Logout user."""
        if self.is_logged_in:
            self.is_logged_in = False
            print(f"{self.name} logged out.")
        else:
            print("You are not logged in.")
        return not self.is_logged_in

    @abstractmethod
    def view_dashboard(self):
        pass


class Admin(BaseUser):
    """Admin user with permissions to manage the platform."""
    def view_dashboard(self):
        print("Admin Dashboard — manage users and courses!")

    def create_instructor(self, platform, name, email, password='1234'):
        from users import Instructor
        instructor = Instructor(platform.user_id_counter, name, email, password)
        platform.user_id_counter += 1
        platform.add_user(instructor)
        return instructor

    def create_student(self, platform, name, email, password='1234'):
        from users import Student
        student = Student(platform.user_id_counter, name, email, password)
        platform.user_id_counter += 1
        platform.add_user(student)
        return student

    def create_course(self, platform, title, description, instructor):
        course = Course(title, description, instructor)
        platform.course_id_counter += 1
        platform.add_course(course)
        instructor.courses_taught.append(course)
        return course

    def platform_stats(self, platform):
        print(f"Total Users: {len(platform.users)} | Total Courses: {len(platform.courses)}")


class Instructor(BaseUser):
    """Instructor user with permissions to create courses, lessons, and grade students."""
    def __init__(self, id, name, email, password='1234', role='instructor', is_logged_in=False):
        super().__init__(id, name, email, password, role, is_logged_in)
        self.courses_taught = []

    def view_dashboard(self):
        print("Instructor Dashboard — manage your courses and lessons.")

    def create_course(self, platform, title, description):
        from users import Admin
        course = Course(title, description, self)
        platform.add_course(course)
        self.courses_taught.append(course)
        print(f"Course '{title}' created.")
        return course

    def add_lesson(self, course_obj, title, content):
        lesson = Lesson(title, content)
        course_obj.add_lesson(lesson)
        print(f"Lesson '{title}' added to course '{course_obj.title}'.")
        return lesson

    def view_enrolled_lessons(self, course_obj):
        print(f"\nLessons for {course_obj.title}:")
        for lesson in course_obj.lessons:
            status = "Published" if lesson.is_published else "Unpublished"
            print(f"- {lesson.title} [{status}]")

    def grade_student(self, course_obj, student_obj, assessment_name, score):
        if course_obj not in self.courses_taught:
            print("Error: Not instructor for this course.")
            return
        course_obj.record_grade(student_obj, assessment_name, score)


class Student(BaseUser):
    """Student user with permissions to enroll, view lessons, and track progress."""
    def __init__(self, id, name, email, password='1234', role='student', is_logged_in=False):
        super().__init__(id, name, email, password, role, is_logged_in)
        self.enrolled_courses = []

    def view_dashboard(self):
        print("Student Dashboard — browse and track your courses.")

    def browse_courses(self, platform):
        print("\nAvailable Courses:")
        for course in platform.courses:
            print(f"- {course.title} by {course.instructor.name}")

    def enroll(self, course_obj):
        if course_obj not in self.enrolled_courses:
            self.enrolled_courses.append(course_obj)
            course_obj.enrolled_students.append(self)
            print(f"{self.name} enrolled in {course_obj.title}.")
        else:
            print(f"Already enrolled in {course_obj.title}.")

    def view_lessons(self, course_obj):
        print(f"\nLessons in {course_obj.title}:")
        for lesson in course_obj.lessons:
            status = "Published" if lesson.is_published else "Unpublished"
            print(f"- {lesson.title} [{status}]")

    def submit_assignments(self, course_obj, assessment_name, score):
        if course_obj in self.enrolled_courses:
            course_obj.record_grade(self, assessment_name, score)
        else:
            print("You are not enrolled in this course.")

    def view_progress(self):
        for course in self.enrolled_courses:
            report = ProgressReport(self, course)
            report.print_report()
