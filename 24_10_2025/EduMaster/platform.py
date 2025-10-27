class EduPlatform:
    """
    EduPlatform is the main platform managing users and courses.
    """
    def __init__(self):
        self.users = []
        self.courses = []
        self.user_id_counter = 1
        self.course_id_counter = 1

    def add_user(self, user_obj):
        """Add a user to the platform."""
        self.users.append(user_obj)
        print(f"User '{user_obj.name}' added to platform.")

    def add_course(self, course_obj):
        """Add a course to the platform."""
        self.courses.append(course_obj)
        print(f"Course '{course_obj.title}' added to platform.")

    def get_user(self, email):
        """Retrieve a user by email."""
        for user in self.users:
            if user.email == email:
                return user
        print("User not found.")
        return None

    def get_course(self, title):
        """Retrieve a course by title."""
        for course in self.courses:
            if course.title == title:
                return course
        print("Course not found.")
        return None
