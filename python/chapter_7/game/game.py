import random

def game():
    print("you are playing game guess random number ... ")

    score = random.randint(1,100)
    
    with open("hiscore.txt") as f :
        hisocer = f.read()
        if(hisocer!=""):
            hisocer = int(hisocer)
        else:
            hisocer = 0 


    print(f"you gusse number is {score}")
    if(score>hisocer):
        with open("hiscore.txt" , "w") as f :
            f.write(str(score))

    return score

game()
