def Game_Six():
    # The players's Counters 
    Counter_player_One = 0
    Counter_player_Two = 0

    # To Make Loop Input If The Numbers Small Than 100
    while(Counter_player_One <= 10 or Counter_player_Two <= 10):

        # The Number's Input Of player One
        # To Return The Integer Value 
        Number_Of_Player_One = int(input(f"{Name_Of_Player_One} Enter Number between 0 & 10 Please: "))
        # To Check The Validation OF The Input Number 
        if (Number_Of_Player_One < 10 and Number_Of_Player_One > 0):
            # To Increace The Counter 
            Counter_player_One += Number_Of_Player_One
            print(f"{Name_Of_Player_One} Your Score Is {Counter_player_One}")
        else:
            print(f"Sorry {Name_Of_Player_One} This number Invailed")



        # The Number's Input Of player Two
        # To Return The Integer Value 
        Number_Of_Player_Two = int(input(f"{Name_Of_Player_Two} Enter Number between  0 & 10 Please: "))
        # To Check The Validation OF The Input Number 
        if (Number_Of_Player_Two < 10 and Number_Of_Player_Two > 0):
            # To Increace The Counter 
            Counter_player_Two += Number_Of_Player_Two
            print(f"{Name_Of_Player_Two} Your Score Is {Counter_player_Two}")
        else:
            print(f"Sorry {Name_Of_Player_Two} This number Invailed") 




        # To Stoping The Game
        if(Counter_player_One >= 10 or Counter_player_Two >= 10):
            if(Counter_player_One == Counter_player_Two ):
                print("Sorry play Agin , No One Are Winner")
                pass
            else :
                # To known the Winner Of The Game 
                if(Counter_player_One > Counter_player_Two ):
                    print(f"{Name_Of_Player_One}  IS The Winner By {Counter_player_One} Points")
                else:
                    print(f"{Name_Of_Player_Two} IS The Winner By {Counter_player_Two} Points")
                pass

        # To Start The Gaame Agin
        if (Counter_player_One >= 10 or Counter_player_Two >= 10):
            Agin = input("If You Need Too Play Agin Choose (Agin , A , a) OORR (E , Exit , e) Tto End Game: ")
            if(Agin == "Agin" or Agin ==  "A" or Agin == "a"):
                Game_Six()
            elif (Agin == "E" or Agin == "Exit" or Agin == "e"):
                print("The Game is Finshed")
                break


# To Get The Names OF the Players 
Name_Of_Player_One = input("Player_One Enter Your Name Please: ")

# To Check If The Name is From Characters
if(Name_Of_Player_One.isalnum != True):
    print(f"Welcome {Name_Of_Player_One}")
else:
    print(f"{Name_Of_Player_One} , This Name Is UnValide")
    print("Your Nname Must Be Char From Aa-Zz")
    Name_Of_Player_One = input("Player_One Enter Your Name, Agin Please: ")
    print(f"Welcome {Name_Of_Player_One}")


# To Check If The Name is From Characters
Name_Of_Player_Two = (input("Player_Two Enter Your Name Please: "))

if(Name_Of_Player_Two.isalpha != True):
    print(f"Welcome {Name_Of_Player_Two}")
else:
    print(f"{Name_Of_Player_Two} , This Name Is UnValide")
    print("Your Nname Must Be Char From Aa-Zz")
    Name_Of_Player_One = input("Player_Two Enter Your Name, Agin Please: ")
    print(f"Welcome {Name_Of_Player_Two}")

# The description Of Game
print("Welcome Our Players, this Game Is A Counter All Player  Set Number This Counter Increases the Player Who Gget 100 Or More First Win The Game")

Game_Six()