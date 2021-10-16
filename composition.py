# compositions of classes - Use a class inside another class.
# Composite classes have "part-of" relationship.

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

    def __init__(self, name, age, pay, bonus):
        self.__name = name
        self.__age = age
        self.__salary_obj = Salary(pay, bonus)

    def calculate_salary(self):
        return self.__salary_obj.get_salary()


#object creation
employee1 = Employee('john', 28, 10000, 2000)
print(employee1.calculate_salary())
