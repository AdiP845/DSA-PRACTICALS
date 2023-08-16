# Department maintains a student information. The txt file contains roll number, name, division and address. Allow user 
# to add, delete information of student. Display information of particular employee. If record of student does not exist 
# an appropriate message is displayed. If it is, then the system displays the student details. Use sequential file to main
# the data. in python

def add_student_info(file_name):
    roll_number = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    division = input("Enter Division: ")
    address = input("Enter Address: ")

    with open(file_name, 'a') as file:
        file.write(f"{roll_number},{name},{division},{address}\n")

    print("Student information added successfully!")

def delete_student_info(file_name):
    roll_number = input("Enter Roll Number of the student to delete: ")

    with open(file_name, 'r') as file:
        lines = file.readlines()

    with open(file_name, 'w') as file:
        deleted = False

        for line in lines:
            student_info = line.strip().split(',')
            if student_info[0] != roll_number:
                file.write(line)
            else:
                deleted = True

        if deleted:
            print("Student information deleted successfully!")
        else:
            print("Student not found!")

def display_student_info(file_name):
    roll_number = input("Enter Roll Number of the student to display: ")

    with open(file_name, 'r') as file:
        found = False

        for line in file:
            student_info = line.strip().split(',')
            if student_info[0] == roll_number:
                print("Roll Number:", student_info[0])
                print("Name:", student_info[1])
                print("Division:", student_info[2])
                print("Address:", student_info[3])
                found = True
                break

        if not found:
            print("Student not found!")

def main():
    file_name = "student_info.txt"

    while True:
        print("\n***** Student Information System *****")
        print("1. Add Student Information")
        print("2. Delete Student Information")
        print("3. Display Student Information")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student_info(file_name)
        elif choice == '2':
            delete_student_info(file_name)
        elif choice == '3':
            display_student_info(file_name)
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")

    print("Exiting the program.")

if __name__ == '__main__':
    main()