class Student:
    def add_exam(self,grade):
        self.grades.append(grade)

    def get_average(self):
        somme = 0
        for i in self.grades:
            somme = somme+i
        moyenne = somme/len(self.grades)
        return(moyenne)

    def __init__(self,name):
        self.name = name
        self.grades = list()

class School:
    def add_student(self,student):
        self.students.append(student)

    def get_best_student(self):
        best_student = self.students[0]
        for i in self.students:
            if i.get_average() > best_student.get_average():
                best_student = i
        return(best_student)

    def get_average(self):
        somme = 0
        for i in self.students:
            somme = somme+i.get_average()
        moyenne = somme/len(self.students)
        return(moyenne)

    def __init__(self,name):
        self.name = name
        self.students = list()

class City:
    def add_school(self,school):
        self.schools.append(school)

    def get_best_school(self):
        best_school = self.schools[0]
        for i in self.schools:
            if i.get_average() > best_school.get_average():
                best_school = i
        return(best_school)

    def get_best_student(self):
        best_school = self.get_best_school()
        best_student = best_school.get_best_student()
        return(best_student)

    def __init__(self,name):
        self.name = name
        self.schools = list()


def main():
    paris = City('paris')
    hkis = School('hkis')
    paris.add_school(hkis)
    for student_name, student_marks in (('alice', (1, 2, 3)),
                                        ('bob', (2, 3, 4)),
                                        ('catherine', (3, 4, 5)),
                                        ('daniel', (4, 5, 6))):
        student = Student(student_name)
        for mark in student_marks:
            student.add_exam(mark)
        hkis.add_student(student)
    print(paris.get_best_school().name)
    print(paris.get_best_student().name)


if __name__ == '__main__':
    main()

