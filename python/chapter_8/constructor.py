class Employe :
    language = "Python"
    salary = 100000000

    def __init__(self,lunguage,salary):
        self.language = lunguage
        self.salary = salary
        # print("Hello")

    def getinfo(self):
        print(f"the laguage is {self.language}.\nthe salary is {self.salary}")
    


    # @staticmethod
    # def greet():
    #     print("Good Morning")

   

user = Employe("FastAPI",1200000000)

print(f"the laguage is {user.language}.\nthe salary is {user.salary}")

user.getinfo()

# user.greet()