direct_access_file = {}  # Simulated direct access file (dictionary)

def insert_record():
    roll_number = input("Enter roll number: ")
    name = input("Enter name: ")
    division = input("Enter division: ")
    address = input("Enter address: ")

    record = {
        'name': name,
        'division': division,
        'address': address
    }

    direct_access_file[roll_number] = record
    print("Record inserted successfully.")

def delete_record():
    roll_number = input("Enter roll number to delete: ")

    if roll_number in direct_access_file:
        del direct_access_file[roll_number]
        print("Record deleted successfully.")
    else:
        print("Record not found.")

while True:
    print("1. Insert Record")
    print("2. Delete Record")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        insert_record()
    elif choice == '2':
        delete_record()
    elif choice == '3':
        break
