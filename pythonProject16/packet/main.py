# packet/main.py

from packet.add import add_student
from packet.list import list_students
from packet.help import help_command
from packet.exit import exit_program


def main():
    students = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            exit_program()
        elif command == 'add':
            add_student(students)
        elif command == 'list':
            list_students(students)
        elif command == 'help':
            help_command()
        else:
            print(f"Неизвестная команда {command}")


if __name__ == '__main__':
    main()
