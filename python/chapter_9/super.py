class employe:
    print("this is employe")
    a = 1

class programmer(employe):
    print("this is program")
    b = 2

class Manager(programmer):
    print("this is manager")
    c = 3

e = employe()
print(e.a)
e = programmer()
print(e.a, e.b  )
e =  Manager()
print(e.a , e.b , e.c)