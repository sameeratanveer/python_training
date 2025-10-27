class Course:
    """
    Represents a course with lessons, enrolled students, and grades.
    """
    course_counter = 0

    def __init__(self, title, description, instructor, lessons=None, enrolled_students=None, grades=None, status='open'):
        Course.course_counter += 1
        self.course_id = Course.course_counter
        self.title = title
        self.description = description
        self.instructor = instructor
        self.lessons = lessons if lessons else []
        self.enrolled_students = enrolled_students if enrolled_students else []
        self.grades = grades if grades else {}
        self.status = status

    def add_lesson(self, lesson_obj):
        """Add a lesson to the course."""
        self.lessons.append(lesson_obj)
        print(f"Lesson '{lesson_obj.title}' added to course '{self.title}'.")

    def enroll_student(self, student_obj):
        """Enroll a student in the course."""
        student_obj.enroll(self)

    def get_info(self):
        """Print course information."""
        print(f"Course Id: {self.course_id} | Title: {self.title} | Instructor: {self.instructor.name}")
        print(f"Lessons: {len(self.lessons)} | Enrolled students: {len(self.enrolled_students)} | Status: {self.status}")

    def record_grade(self, student_obj, assessment_name, score):
        """Record a grade for a student."""
        if student_obj not in self.enrolled_students:
            print("Error: Student not enrolled in this course.")
            return
        student_id = student_obj.id
        if student_id not in self.grades:
            self.grades[student_id] = {}
        self.grades[student_id][assessment_name] = score
        print(f"Recorded {score} for {student_obj.name} in {self.title} ({assessment_name})")

    def calculate_average(self, student_obj):
        """Calculate average score for a student."""
        student_id = student_obj.id
        if student_id not in self.grades or not self.grades[student_id]:
            return 0
        scores = list(self.grades[student_id].values())
        return sum(scores) / len(scores)


class Lesson:
    """
    Represents a lesson in a course.
    """
    lesson_counter = 0

    def __init__(self, title, content, is_published=False):
        Lesson.lesson_counter += 1
        self.lesson_id = Lesson.lesson_counter
        self.title = title
        self.content = content
        self.is_published = is_published

    def publish(self):
        """Publish the lesson."""
        self.is_published = True

    def unpublish(self):
        """Unpublish the lesson."""
        self.is_published = False

    def get_summary(self):
        """Print a short summary of the lesson."""
        print(f"Lesson: {self.title}, Preview: {self.content[:50]}...")
