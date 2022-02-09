def show_employee(name, salary = 9000) :
    print(name, salary)


if int(input('Salary available? (1 for yes, 0 for no): ')) :
    show_employee(input('Give a name: '), input('Give a salary: '))
else :
    show_employee(input('Give a name: '))