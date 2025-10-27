class ProgressReport:
    """
    Progress report for a student in a course.
    """
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grades = course.grades.get(student.id, {})
        self.average = course.calculate_average(student)
        self.completion_percent = self._compute_completion()

    def _compute_completion(self):
        """Compute completion based on graded assessments vs total lessons."""
        if len(self.course.lessons) == 0:
            return 0
        # Simple metric: each grade corresponds to a completed lesson
        return min(100, len(self.grades) / len(self.course.lessons) * 100)

    def print_report(self):
        """Print the progress report."""
        print(f"\nProgress Report for {self.student.name} in {self.course.title}")
        print(f"Grades: {self.grades}")
        print(f"Average Score: {self.average:.2f}")
        print(f"Completion: {self.completion_percent:.1f}%\n")
