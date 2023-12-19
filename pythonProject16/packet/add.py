# packet/add.py

def add_student(students):
    full_name = input("Фамилия и инициалы? ")
    group_number = input("Номер группы? ")
    grades_str = input("Успеваемость (через пробел)? ")

    grades = [float(grade) for grade in grades_str.split()]

    student = {
        'full_name': full_name,
        'group_number': group_number,
        'grades': grades,
    }

    students.append(student)
    students.sort(key=lambda item: item.get('group_number', ''))
