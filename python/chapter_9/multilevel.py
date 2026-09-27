class employe:
    a = 1

class programmer(employe):
    b = 2

class Manager(programmer):
    c = 3

e = employe()
print(e.a)
e = programmer()
print(e.a, e.b )
e =  Manager()
print(e.a , e.b , e.c)