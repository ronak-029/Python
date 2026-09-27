class Employe :
    language = "Python"
    salary = 100000000

    def getinfo(self,language,salary):
        self.language = language
        self.salary = salary
        print(f"the laguage is {user.language}.\nthe salary is {user.salary}")
    

   

user = Employe("FastAPI",12000000)
user.getinfo()


# this is not work on class and object 