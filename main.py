import random

computer = random.choice([1,0,-1])
you_dict = {
    "a" : 1,
    "s" : 0,
    "d" : -1

}

you = str(input("Enter \'a\' or \'s\'or \'d\' =>"))
you_value = you_dict[you]

if(you == 'a' or you == 's' or you == 'd' ):
    if(you_value == 1 and computer == 1):
        print("You win")
    elif(you_value == 1 and computer == 0):
        print("You lose")
    elif(you_value == 1 and computer == -1):
        print("You lose")
    elif(you_value == 0 and computer == 1):
        print("You lose")
    elif(you_value == 0 and computer == 0):
        print("You win")
    elif(you_value == 0 and computer == -1):
        print("You lose")
    elif(you_value == -1 and computer == 1):
        print("You lose")
    elif(you_value == -1 and computer == 0):
        print("You lose")
    elif(you_value == -1 and computer == -1):
        print("You win")
else:
    print("Enter valid value")