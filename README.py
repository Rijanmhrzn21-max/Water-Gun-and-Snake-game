# Water-Gun-and-Snake-game
#This is  a water,paper and gun game which i made as a begginer by using python.Hope youl ike it and you can aslo tell what features i should add.

def the_whole():
    import random

    tools=["Gun","Water","Snake"]
    guessing=input("Enter eiter Water,Gun or Snake:")
    result=random.choice(tools)
    
    #Gun code
    if result=="Gun" and guessing=="Water":
        print("You win.The machine choosed Gun.\n")
    elif result=="Gun" and guessing=="Snake":
        print("You lose.The machine choosed Gun.\n")
    elif result=="Gun" and guessing=="Gun":
        print("No one wins.The machince choosed Gun.\n")

    #Snake code
    elif result=="Snake" and guessing=="Water":
        print("You lose.The machine choosed Snake.\n")
    elif result=="Snake" and guessing=="Gun":
        print("You win.The machine choosed Snake.\n")
    elif result=="Snake" and guessing=="Snake":
        print("No one wins.The machine choosed Snake.\n")

    #Water code
    elif result=="Water" and guessing=="Snake":
        print("You win.The machine choosed Water.\n")
    elif result=="Water" and guessing=="Gun":
        print("you lose.The machine choosed Water.\n")
    elif result=="Water" and guessing=="Water":
        print("No one wins.The machine choosed Water.\n")

while True:
    the_whole()
