class Student():
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url
    
    def __str__(self):
        return '{name}, {gender}, {datasheet} courses, {image_url}'.format(
            name=self.name, gender=self.gender, datasheet=len(self.data_sheet.courses), image_url=self.image_url)

    def __eq__(self, other):
        return self.name == other.name 

    def get_avg_grade(self):
        total = 0
        for grade in self.data_sheet.get_grades_as_list():
            total += grade

        return total / len(self.data_sheet.get_grades_as_list())

    def get_study_progression(self):
        total = 0
        for course in self.data_sheet.courses:
            total += course.ETCS
        return total / 150