import csv

FILE = "students.csv"

def read_students():
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def add_student(student_id, name, age, grade):
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([student_id, name, age, grade])
    print(f"Student {name} added successfully!")



#practicing file handling
#Read file
# def read_students():
#     file = open('students.csv',"r");
#     content = file.read()
#     print("content is  : ",content)
#     file.close()  


#write file
#     file = open ('students.csv',"a");
# file.write('5, "Abhi", 21, "A+"')
# file.close()