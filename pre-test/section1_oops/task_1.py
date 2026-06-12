# -----------CLASS 'EMPLOYEE'------------
class Employee:
    # starting salary
    def __init__(self):
        self.salary = 50000

    # add 10000 to salary
    def increment(self):
        self.salary = self.salary + 10000

    # take 5000 away
    def deduct(self):
        self.salary = self.salary - 5000

    # show salary on the screem
    def get_salary(self):
        print(self.salary)


# FIRST EMPLOYEE
emp1 = Employee()
emp1.get_salary()  # Prints 50000
emp1.increment()
emp1.deduct()
emp1.get_salary()  # Prints 55000

# SECOND EMPLOYEE
emp2 = Employee()
emp2.get_salary()  # Prints 50000
emp2.increment()
emp2.deduct()
emp2.get_salary()  # Prints 55000
