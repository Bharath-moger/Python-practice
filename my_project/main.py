import argparse
from my_project.student_manager import read_students, add_student

def main():
    parser = argparse.ArgumentParser(description="Student Manager CLI")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Read command
    subparsers.add_parser("read", help="Read all students from CSV")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new student")
    add_parser.add_argument("--no", required=True, help="Student ID")
    add_parser.add_argument("--name", required=True, help="Student name")
    add_parser.add_argument("--age", required=True, type=int, help="Student age")
    add_parser.add_argument("--grade", required=True, help="Student grade")

    args = parser.parse_args()

    if args.command == "read":
        read_students()
    elif args.command == "add":
        add_student(args.no, args.name, args.age, args.grade)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


# from my_project.student_manager import  read_students , add_student
# # from my_project.demo import calc , add

# if __name__ == "__main__":
#     # Add a new student
#     # add_student(5, "sharath", 21, "A+")

#     # Read all students
#     read_students()

#     #Prcaticing
#     # calc(200,100)
#     # add(1,2,3,4,5,6,7,8,9)