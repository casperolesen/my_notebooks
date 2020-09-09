class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade=None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade
    
    def __str__(self):
        return 'Name: {name}, Classroom: {classroom}, Teacher: {teacher}, ETCS: {ETCS}, Grade: {grade}'.format(
            name=self.name, classroom=self.classroom, teacher=self.teacher, ETCS=self.ETCS, grade=self.grade) 