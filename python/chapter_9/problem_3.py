class Employe:
    salary = 280
    icrement = 20

    # def userSalary(self):
    #     print(f"the employ Salary is {self.salary}")
    @property
    def salaryAfterIcrement(self):
        return (self.salary + self.salary + (self.icrement/100))
    @salaryAfterIcrement.setter
    def salaryAfterIcrement(self ,salary):
       self.icrement = ((salary/self.salary)-1)*100


e = Employe()
# e.userSalary()
e.salaryAfterIcrement = 300
print(round(e.icrement))