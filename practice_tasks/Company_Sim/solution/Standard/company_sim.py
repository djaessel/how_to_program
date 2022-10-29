import sys


class Employee:
    def __init__(self, data):
        self.id = int(data[0])
        self.username = data[1].strip('"')
        self.password = data[2].strip('"')
        self.salary = int(data[3])
        self.area = data[4].strip('"')
        self.is_manager = (data[5] == "True")

    def show_salary(self):
        print(self.salary)

    def show_area(self):
        print(self.area)


def load_employee():
    employee = []
    with open("employee.csv", "r") as f:
        data_len = 1
        f.readline() # skip header line
        while data_len > 0:
            line = f.readline().rstrip("\n")
            data_len = len(line)
            if data_len > 0:
                e = Employee(line.split(";"))
                employee.append(e)
    return employee


def find_user(emp, username):
    for e in emp:
        if e.username == username:
            return e
    return 0


def handle_command(current_user, all_users, command):
    # Salary command
    if command.startswith("salary"):
        command_data = command.split()
        l = len(command_data)
        if l == 1:
            current_user.show_salary()
        elif l == 2:
            username = command_data[1]
            if current_user.is_manager or current_user.username == username:
                user = find_user(all_users, username)
                if user != 0:
                    user.show_salary()
                else:
                    print("User not found!")
            else:
                print("Access denied!")
        else:
            print("Invalid arguments!")
    # Area command
    elif command.startswith("area"):
        command_data = command.split()
        l = len(command_data)
        if l == 1:
            current_user.show_area()
        elif l == 2:
            username = command_data[1]
            user = find_user(all_users, username)
            if user != 0:
                user.show_area()
            else:
                print("User not found!")
        else:
            print("Invalid arguments!")
    # Exit command
    elif command == "exit":
        sys.exit()
    # All else
    else:
        print("Invalid command!")


def main_program():
    emp = load_employee()

    print("##############")
    print("# Company OS #")
    print("##############")
    print()
    
    current_user = 0
    access = False
    while not access:
        username = input("Username: ")
        if username == "exit":
            sys.exit()

        password = input("Password: ")
        if password == "exit":
            sys.exit()

        for e in emp:
            if e.username == username and e.password == password:
                access = True
                current_user = e
                # break

        if not access:
            print("Wrong credentials!")

    
    last_command = ""
    while last_command != "exit":
        last_command = input("Enter command: ")
        handle_command(current_user, emp, last_command)


main_program()

