import random
'''
paper = -1
rock = 0
scissor = 1
'''

computer = random.choice([-1, 0, 1])
print("Welcome to ROCK PAPER SCISSOR Game\n\n\tFor ⛰️\tEnter'r'\n\tFor 📃 Enter 'p'\n\tFor ✂️\tEnter 's'\n\n")
youstr = input("Enter your choice:-")
youDict = {"r":0, "p":-1, "s":1}
reverseDict = {0:"Rock⛰️", -1:"Paper📃", 1:"Scissor✂️"}

you = youDict[youstr]

print(f"\tYou Chose:-{reverseDict[you]}\n\tComputer Chose:-{reverseDict[computer]}")

if(computer == you):
    print("It's a Draw Match :(")
else:
    if(computer == -1 and you == 1):
        print("You Win:)")
    elif(computer == -1 and you == 0):
        print("Computer Win")


    elif(computer == 0 and you == 1):
        print("Computer Win")
    elif(computer == 0 and you == -1):
        print("You Win:)")


    elif(computer == 1 and you == -1):
        print("Computer Win")
    elif(computer == 1 and you == 0):
        print("You Win:)")
    else:
        print("Something Went Wrong")    

