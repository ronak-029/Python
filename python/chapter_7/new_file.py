with open("old.txt") as f:
    content = f.read()

with open("newFile.txt" , "w") as f:
    f.write(content)
    