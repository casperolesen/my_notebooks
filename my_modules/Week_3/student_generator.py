from my_modules.Week_3.Student import Student
from my_modules.Week_3.DataSheet import DataSheet
from my_modules.Week_3.Course import Course

import random
import csv
import platform

course_names = ['English', 'French', 'German', 'Spanish', 'Mathematics', 'Biology', 'Chemistry', 'Geography', 'Economics', 'History']
grades = [-3, 0, 2, 4, 7, 10, 12]
genders = ['Male', 'Female']

def generate_courses():
    courses_available = course_names.copy()
    courses = []
    for ic in range(1, 6):
        index = random.randint(0, len(courses_available)-1)
        course_name = courses_available.pop(random.randint(0, len(courses_available)-1)) 
        classroom = "{}{}{}".format(str(random.randint(1,5)), '0', str(random.randint(1, 9)))
        etcs = 0
        grade = grades[random.randint(0, len(grades)-1 )]
        if (grade >= 2):
            etcs = 30

        courses.append(Course(course_name, classroom, 'Teacher {}'.format(str(ic)), etcs, grade))
    
    return courses

def generate_random_students(n):
    students = []
    for i in range(1, n+1):
        # courses
        courses = generate_courses()
        
        # datasheet
        data_sheet = DataSheet(courses)

        # student
        student_name = 'Student {}'.format(str(i))
        gender = genders[random.randint(0,1)]
        image_url = 'http://myprofile.com/myimage{}.jpg'.format(str(i))
        students.append(Student(student_name, gender, data_sheet, image_url))

    print("{} students created!".format(len(students)))
    return students

def save_students_csv(students):
    #stud_name, course_name, teacher, ects, classroom, grade, img_url
    
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None

    with open('./files/students.csv', 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(["stud_name", "gender", "course_name", "teacher", "ects", "classroom", "grade", "img_url"])
        for s in students:
            for c in s.data_sheet.courses:
                output_writer.writerow([s.name, s.gender, c.name, c.teacher, c.ETCS, c.classroom, c.grade, s.image_url])
    
    return print("Saved to file!")

def get_students_from_csv():
    students = []
    with open('./files/students.csv') as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            student = Student(row[0], row[1], DataSheet([Course(row[2], row[5], row[3], int(row[4]), int(row[6]) )]), row[7])
            if student not in students: 
                students.append(student)
            else:
                index = students.index(student)
                temp = students[index]
                temp.data_sheet.courses.append(Course(row[2], row[5], row[3], int(row[4]), int(row[6]) ))
                students[index] = temp

    return students

if __name__ == "__main__":
    students = generate_random_students(100)
    print("{} students created!".format(len(students)))
    save_students_csv(students)
    print("Saved to file!")