Player1 = input("Player one Enter Your Name: ")
counter1 = 0 
Player2 = input("Player two Enter Your Name: ")
counter2 = 0

def TheGame(C1 , C2):
    animals = ["lion" , "ant" , "elephant" , "monkey" , "tiger" , "panda"]
    for r in range(1 , 11):
        print(f"{Player1}'s Scoure is {C1}")
        print(f"{Player2}'s Scoure is {C2}")
        user = input("Enter the animal Name: ")
        if animals.count(user.lower()) == 1 :
            if (r%2 == 1):
                C1 += 1 
            elif (r%2 == 0):
                C2 +=1 
        else :
            continue

    if C1 > C2 :
        print(f"the winer is {Player1}")

    elif C1 == C2 :
        TheGame()
    else :
        print(f"the winer is {Player2}")


TheGame(counter1 , counter2)