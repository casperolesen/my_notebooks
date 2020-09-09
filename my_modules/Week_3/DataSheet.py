class DataSheet():
    def __init__(self, courses=[]):
        self.courses = courses

    def get_grades_as_list(self):
        return [course.grade for course in self.courses]
