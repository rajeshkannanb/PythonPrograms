# Aggregation of classes - Combine two or more classes together.
# Aggregate classes have "has-a" relationship.

class Salary:
    __pay = None
    __bonus = None

    def __init__(self, pay, bonus):
        self.__pay = pay
        self.__bonus = bonus

    def get_salary(self):
        return (self.__pay + self.__bonus)

class Employee:
    __name = None
    __age = None
    __salary_obj = None

    def __init__(self, name, age, salary_obj):
        self.__name = name
        self.__age = age
        self.__salary_obj = salary_obj

    def calculate_salary(self):
        return self.__salary_obj.get_salary()

#object creation
salary_emp1 = Salary(10000, 5000)
employee1 = Employee('john', 28, salary_emp1)
print(employee1.calculate_salary())

