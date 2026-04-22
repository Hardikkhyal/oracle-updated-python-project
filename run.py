from core.employee import add_employee, list_employees, update_status
from core.attendance import mark_attendance
from core.payroll import generate_payroll
from core.reports import monthly_report, salary_slip

def menu():
    print("\n1. Add Employee")
    print("2. List Employees")
    print("3. Update Status")
    print("4. Mark Attendance")
    print("5. Generate Payroll")
    print("6. Monthly Report")
    print("7. Salary Slip")
    print("0. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = int(input("Emp ID: "))
        name = input("Name: ")
        dept = input("Dept: ")
        desig = input("Designation: ")
        join_date = input("Join Date (YYYY-MM-DD): ")
        salary = float(input("Base Salary: "))
        status = input("Status: ")
        add_employee(emp_id, name, dept, desig, join_date, salary, status)

    elif choice == "2":
        list_employees()

    elif choice == "3":
        emp_id = int(input("Emp ID: "))
        status = input("New Status: ")
        update_status(emp_id, status)

    elif choice == "4":
        emp_id = int(input("Emp ID: "))
        date = input("Date (YYYY-MM-DD): ")
        status = input("PRESENT/ABSENT: ")
        mark_attendance(emp_id, date, status)

    elif choice == "5":
        emp_id = int(input("Emp ID: "))
        month = int(input("Month: "))
        year = int(input("Year: "))
        generate_payroll(emp_id, month, year)

    elif choice == "6":
        month = int(input("Month: "))
        year = int(input("Year: "))
        monthly_report(month, year)

    elif choice == "7":
        emp_id = int(input("Emp ID: "))
        month = int(input("Month: "))
        year = int(input("Year: "))
        salary_slip(emp_id, month, year)

    elif choice == "0":
        break
