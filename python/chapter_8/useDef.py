# class Employe :
#     language = "Python"
#     salary = 100000000


#     def getinfo():
#         print(f"the laguage is {Employe.language}.\nthe salary is {Employe.salary}")



# Employe.getinfo()

class Employe :
    language = "Python"
    salary = 100000000

    
    def getinfo(self):
        print(f"the laguage is {user.language}.\nthe salary is {user.salary}")
    @staticmethod
    def greet():
        print("Good Morning")

user = Employe()
user.salary = 20000000
user.language = "C++"

user.getinfo()

user.greet()