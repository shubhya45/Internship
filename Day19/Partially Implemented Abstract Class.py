# Partially Implemented Abstract Class
# Instructions:

# Create an abstract class named Employee:

# Abstract method: calculate_salary().

# Concrete method: display_role() (prints role).

# Create concrete classes:

# FullTimeEmployee with a calculate_salary() method.

# PartTimeEmployee with a calculate_salary() method.

# Instantiate both and test both methods.
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    def display_role(self):
        print("CO")
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print(f"Full Time salary is:- {40000}")
class PartTimeEmployee(FullTimeEmployee):
    def calculate_salary(self):
        print(f"Part Time salary is:- {20000}")
c1=FullTimeEmployee()
c1.display_role()
c1.calculate_salary()
c2=PartTimeEmployee()
c2.calculate_salary()