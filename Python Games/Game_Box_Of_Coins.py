def Game_Eight():
    # Set The Number OF Coins
    Coins = int(input(f"Enter The Number Of Coins: "))
    if (Coins > 10 or Coins < 300):
        Coins = Coins
    else:
        print("Sorry This Number Unvaild , We Will SSett This Value")
        Coins = 50

    # The Descripton Of The Game
    print(f"Welcome Our Players, this Game Is You Have {Coins} Of Coins The Player Remove The Number Which You Write The Player Who Get The Secound Coin Is The Winner , but You Can Write Number More Than The Half Of The Remaining Coins")

    while(Coins > 0):
        # The Number's Input Of player One
        # To Return The Integer Value 
        Number_Of_Player_One = int(input(f"{Name_Of_Player_One} Enter Number between 0 & {int(Coins/2 +1)} Please: "))

        if Number_Of_Player_One  > (Coins/2+1) or Number_Of_Player_One  < 0 :
            print("This Number Is UnVailed")
            print(f"Still have {Coins}  Of Coins")
        else:

            Coins -= Number_Of_Player_One
            print(f"Still have {Coins} Of Coins")
            if(Coins == 0):
                print("Congrtoilction!")
                print(f"{Name_Of_Player_One} You Are The Winner")
                pass

        Number_Of_Player_Two = int(input(f"{Name_Of_Player_Two} Enter Number between 0 & {int(Coins/2 +1)} Please: "))

        if Number_Of_Player_Two  > (Coins/2+1) or Number_Of_Player_Two  < 0 :
            print("This Number Is UnVailed")
            print(f"Still have {Coins}  Of Coins")

        else:
            Coins -= Number_Of_Player_Two
            print(f"Still have {Coins}  Of Coins")
            if(Coins == 0):
                print("Congrtoilction!")
                print(f"{Name_Of_Player_Two} You Are The Winner")
                pass

        
         # To Start The Gaame Agin
        if (Coins == 0): 
            Agin = input("If You Need Too Play Agin Choose (Agin , A , a) OORR (E , Exit , e) Tto End Game: ")
            if(Agin == "Agin" or Agin ==  "A" or Agin == "a"):
                    Game_Eight()
            elif (Agin == "E" or Agin == "Exit" or Agin == "e"):
                print("The Game is Finshed")
                break;

# To Get The Names OF the Players 
Name_Of_Player_One = input("Player_One Enter Your Name Please: ").capitalize()
# To Check If The Name is From Characters
if(Name_Of_Player_One.isalnum != True):
    print(f"Welcome {Name_Of_Player_One}")
else:
    print(f"{Name_Of_Player_One} , This Name Is UnValide")
    print("Your Nname Must Be Char From Aa-Zz")
    Name_Of_Player_One = input("Player_One Enter Your Name, Agin Please: ").capitalize()
    print(f"Welcome {Name_Of_Player_One}")


# To Check If The Name is From Characters
Name_Of_Player_Two = input("Player_Two Enter Your Name Please: ").capitalize()
if(Name_Of_Player_Two.isalnum != True):
    print(f"Welcome {Name_Of_Player_Two}")
else:
    print(f"{Name_Of_Player_Two} , This Name Is UnValide")
    print("Your Nname Must Be Char From Aa-Zz")
    Name_Of_Player_One = input("Player_Two Enter Your Name, Agin Please: ").capitalize()
    print(f"Welcome {Name_Of_Player_Two}")

# The deescription Of Game
print(f"Welcome Our Players, this Game Is You Have Number Of Coins The Player Remove The Number Which You Write The Player Who Get The Secound Coin Is The Winner , but You Can Write Number More Than The Half Of The Remaining Coins")


Game_Eight()