n = str(input("Enter About Your Self : "))


f = open("mywritefile.txt", "w")
f.write(n)
f.close()