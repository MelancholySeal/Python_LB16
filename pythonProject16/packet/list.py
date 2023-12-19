# packet/list.py

def list_students(students):
    line = '+-{}-+-{}-+-{}-+'.format(
        '-' * 30,
        '-' * 15,
        '-' * 20
    )
    print(line)
    print(
        '| {:^30} | {:^15} | {:^20} |'.format(
            "Ф.И.О.",
            "Номер группы",
            "Успеваемость"
        )
    )
    print(line)

    for student in students:
        average_grade = sum(student.get('grades', 0)) / len(student.get('grades', 1))
        if average_grade > 4.0:
            print(
                '| {:<30} | {:<15} | {:<20} |'.format(
                    student.get('full_name', ''),
                    student.get('group_number', ''),
                    ', '.join(map(str, student.get('grades', [])))
                )
            )
    print(line)
