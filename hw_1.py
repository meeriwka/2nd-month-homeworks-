
class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Full name: {self.full_name}, Age: {self.age}, Married: {self.is_married}')

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = dict(marks)

    def average_grade(self):
        print(f'Средний балл: ',sum(self.marks.values())/ len(self.marks.keys()))

class Teacher(Person):
    bonus = 0
    base_salary = 20000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        if self.experience > 3:
            bonus = 0.05 * self.base_salary * (self.experience - 3)
            return bonus + self.base_salary

    def display_info(self):
        salary = self.calculate_salary()
        print(f'Зар/плата: {salary}, ФИО: {self.full_name}, возраст: {self.age}, '
              f'семейное положение: {self.is_married}, опыт: {self.experience} лет')


def create_students():
    students_list = [Student("Жаналиев Дастан Рахатбекович", "19",
                   "not married", {'biology': 5,
            'math': 4,
            'chemistry': 5,
            'literature': 5,
            'English': 4}), Student('Сагынбеков Байэл Марсович', '15',
                   'not married', {"biology": 3,
            "math": 4,
            "chemistry": 3,
            "literature": 5,
            "English": 4}), Student("Жумадилова Айпери Айбековна", "21",
                   "не замужем", {'biology': 4,
            'math': 3,
            'chemistry': 4,
            'literature': 5,
            'English': 5})]
    return students_list


One = Person("Жаналиева Мээрим Рахатбековна", "24",
             "not married")
One.introduce_myself()



teacher = Teacher("Усупова Чолпон Сабыровна", "49","замужем", 13)
teacher.calculate_salary()
teacher.display_info()



students = create_students()
for student in students:
    student.introduce_myself()
    student.average_grade()
