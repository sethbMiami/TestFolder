# this will be used to create and define classes for practice

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.last + self.first + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def salary(self):
        return '{} current salary is {}'.format(self.first, self.pay)


emp_1 = Employee('Seth', 'Bruner', 61000)
emp_2 = Employee('Emily', 'Mendez', 65000)
emp_3 = Employee('Test', 'User', 50000)
emp_4 = Employee('Kris', 'Acevedo', 45000)
emp_5 = Employee('Chris', 'Leyva', 80000)


# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)
print(emp_5.email)

print(emp_1.fullname())
print(emp_2.fullname())
print(emp_5.fullname())


print(emp_1.salary())
print(emp_2.salary())
print(emp_5.salary())


