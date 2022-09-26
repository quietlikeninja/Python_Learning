from tabnanny import check


def main():
    class Student:

        def __init__(self, name, year):
            self.name = name
            self.year = year
            self.grades =[]
            self.attendance = {}

        def add_grade(self, grade):
            if (isinstance(grade, Grade)):
                self.grades.append(grade)
        
        def get_average(self):
            sum = 0
            for num in self.grades:
                sum += num.score
            return sum/len(self.grades)

        def add_attendance(self, date, attended : bool):
            self.attendance.update({date: attended})

    class Grade:
        minimum_passing = 65

        def __init__(self, score):
            self.score = score

        def is_passing(self):
            return self.score >= self.minimum_passing

    roger = Student("Roger van der Weyden", 10)
    sandro = Student("Sandro Botticelli", 12)
    pieter = Student("Pieter Bruegel the Elder", 8)

    pieter.add_grade(Grade(100))
    pieter.add_grade(Grade(50))

    #for grade in pieter.grades:
    #    print(grade.is_passing())

    print(f"Pieter's average grade is: {pieter.get_average()}")

    if Grade(pieter.get_average()).is_passing():
        print(f"Pieter passed!")
    else:
        print(f"Pieter failed!")

    pieter.add_attendance("23/09/2022", False)
    pieter.add_attendance("24/09/2022", True)
    pieter.add_attendance("25/09/2022", True)

    print(f"{pieter.name}'s attendance record:")
    print("{:<15} {:<10}".format("Date", "Attended"))
    for date, attended in pieter.attendance.items():
        print("{:<15} {:<10}".format(date, str(attended)))

if __name__ == '__main__':
    main()