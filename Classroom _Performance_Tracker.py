class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):

        return sum(self.marks) / len(self.marks)


class Classroom:
    def __init__(self):
        self.students = {}

    def add_student(self, name, marks):

        self.students[name] = Student(name, marks)

    def calculate_averages(self):

        averages = {}
        for name, student in self.students.items():
            averages[name] = round(student.calculate_average(), 2)
        return averages

    def find_top_performer(self):

        top_student = None
        highest_average = float('-inf')

        for name, student in self.students.items():
            average = student.calculate_average()
            if average > highest_average:
                highest_average = average
                top_student = name

        return top_student



students_data = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}


classroom = Classroom()
for name, marks in students_data.items():
    classroom.add_student(name, marks)


average_marks = classroom.calculate_averages()
top_performer = classroom.find_top_performer()


print("Average Marks:", average_marks)
print("Top Performer:", top_performer)
