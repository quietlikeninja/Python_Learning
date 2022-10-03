#https://www.codecademy.com/courses/learn-intermediate-python-3/projects/python-school-catalogue
class School:
    def __init__(self, name: str, level: str, numberofStudents: int) -> None:
        self.name = name
        self.level = level
        self.numberOfStudents = numberofStudents

    def get_name(self) -> str:
        return self.name

    def get_level(self) -> str:
        return self.level

    @property
    def students(self) -> int:
        """Docstring for the 'numberOfStudents' property"""
        return self.numberOfStudents

    @students.setter
    def students(self, numberOfStudents: int) -> None:
        self.numberOfStudents = numberOfStudents

    def __repr__(self) -> str:
        return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"
    

class PrimarySchool(School):
    def __init__(self, name: str, numberOfStudents: int, pickupPolicy: str) -> None:
        super().__init__(name, "Primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickupPolicy(self) -> str:
        return self.pickupPolicy

    def __repr__(self) -> str:
        return f"{super().__repr__()}.\nStudents can be picked up {self.pickupPolicy}"

class HighSchool(School):
    def __init__(self, name: str, numberOfStudents: int, sportsTeams: list) -> None:
        super().__init__(name, "High", numberOfStudents)
        self.sportsTeams = sportsTeams
    
    def get_sportsTeams(self) -> list:
        return self.sportsTeams
    
    def __repr__(self) -> str:
        return f"{super().__repr__()}.\nHas these sports teams: {self.sportsTeams}"

def main():
    h1 = HighSchool("Gympie State", 100, ["Hockey", "Cricket"])
    #print(s1.get_name())
    #print(s1.get_level())
    #print(s1.get_numberOfStudents())
    h1.students = 1398
    print(h1)

    p1 = PrimarySchool("One Mile State", 450, pickupPolicy="After 3:30pm")
    #print(p1.get_level())
    print(p1)

if __name__ == '__main__':
    main()