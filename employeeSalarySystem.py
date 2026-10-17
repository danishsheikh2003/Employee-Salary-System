#Employee Salary System

class Employee:

    def __init__(self, name, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")

        self.__name = name
        self.__salary = salary

    def display(self):
        print("Name: ",self.__name)
        print("Salary: ",self.__salary)

    def increase_salary(self, percent):
        if percent < 0:
            raise ValueError("Percentage cannot be negative")

        increase = self.__salary * percent / 100
        self.__salary += increase
        print("Salary increased successfully")

            
emp1 = Employee("Danish", 30000)

emp1.display()

emp1.increase_salary(10)

emp1.display()             