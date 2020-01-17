# My attempt at a Python text based adventure for #100DaysOfCode.
#
import os
import sys

class Player:
    def __init__(self, name, health, gold):
        self.name = name
        self.health = health
        self.gold = gold

class Limbs:
    def __init__(self, head, larm, rarm, lhand, rhand, lleg, rleg, lfoot, rfoot):
        self.head = head
        self.larm = larm
        self.rarm = rarm
        self.lhand = lhand
        self.rhand = rhand
        self.lleg = lleg
        self.rleg = rleg
        self.lfoot = lfoot
        self.rfoot = rfoot

player = Player("Player", 25, 15)
limbs = Limbs(True, True, True, True, True, True, True, True, True)

appname = "GLORP"
vers = "v0.0.1"

loop = 0
while loop == 0:
    # Create a 'fresh slate' for GLORP
    os.system('clear')
    # Title Screen and Welcome
    print("\n--------------------------------------------------\n")
    print("                   ", appname, vers)
    print("\n            What would you like to do?             \n")
    print("                     ::PLAY::")
    print("                     ::ABOUT::")
    print("                     ::EXIT::\n")
    action = input(">> ")

    if action == 'play':
        loop = 1
    elif action == 'about':
        os.system('clear')
        print("\n-----------------------------------------------------\n")
        print("      ", appname, vers, "by Ron Becker\n")
        print("When entering a command be sure to type in lower-case")
        print("so that there aren't any issues. You can use commands")
        print("like `go` or `move`, and `inspect` or `examine.`")
        print("\nFor a full list type `help` in the input.\n")
        print("Source: https://github.com/ronbecker/100DaysOfPython\n")
        input("Enter to continue...\n")
    elif action == 'exit':
        print("\n-----------------------------------------------------\n")
        print(" Thank you for playing GLORP! I hope you enjoyed it! \n")
        sys.exit()
    elif action == 'help':
        os.system('clear')
        print("-----------------------------------------------------")
        print("             help - shows this message.              ")
        print("          go <direction> | move <direction>          ")
        print(" inspect | examine - the also accept <item> arguments")
        print("              take <item> | get <item>               ")
        print("                      use <item>                     ")
        print("                      eat <item>                     \n")
        input("Enter to continue...\n")
    else :
        print("\n-----------------------------------------------------\n")
        print("    I don't know how to do that. Let's try agian!    \n")

while loop == 1:
    print("\n-----------------------------------------------------\n")
    print(" Seriously, another adventurer? What is it with you  ")
    print(" guys? Do you just like to suffer? Is that is? Well,  ")
    print(" it doesn't really matter. You're gonna die soon just ")
    print(" like all the others anyways. I may as well get a name ")
    print(" to put on your tombstone. So what is it?\n")
    player.name = input(">> ")
    print("\n-----------------------------------------------------\n")
    print("\n Seriously,", player.name, "is actually what you go by? Wow.. ")
    print(" OK then... I have one more question for you. It's a")
    print(" yes or yes question. Is Ron just the greatest thing ")
    print(" ever??\n")
    yesoryes = input(">> ")
    if yesoryes == 'yes':
        print("\n-----------------------------------------------------\n")
        print(" I knew it! You're going to be a great adventurer! I ")
        print(" can't wait to tell all the guys at the pub that I ")
        print(" got to meet you! Alright, let's get started!")
        print("\n You find yourself on the side of an old trade road as ")
        print(" far as you can tell you're the only person out here.  ")
        print(" To the north the road continues to the capital, to    ")
        print(" south is the forest, to the west is a small village,  ")
        print(" and to the east is a rather run down farm house.\n")
        print(" What would you like to do?")
        choice = input(">> ")
        if choice == "go" or "move":
            pass
        elif choice == "inspect" or "examine":
            pass
        elif choice == "take":
            pass
        elif choice == "use":
            pass
        elif choice == 'eat':
            loop = "eatlimb"
            while loop == "eatlimb":
                print("-----------------------------------------------------\n")
                print(" OK, I'm not gonna lie. This is a really odd choice. ")
                print(" I guess since you don't have any food you're going  ")
                print(" print to have to pick something else to eat...\n")
                print("1. I eat my own head!    |    2. I eat my left hand! ")
                print("3. I eat my right hand!  |    4. The left arm baby! ")
                print("5. The right arm!!       |    6. I have a left foot. ")
                print("7. Or a right foot...    |    8. Maybe my left leg?")
                print("9. I've never like my right leg anyways!")
                eatlimb = input(">> ")
                if eatlimb == '1':
                    pass
                elif eatlimb == '2':
                    pass
                elif eatlimb == '3':
                    pass
                elif eatlimb == '4':
                    pass
                elif eatlimb == '5':
                    pass
                elif eatlimb == '6':
                    pass
                elif eatlimb == '7':
                    pass
                elif eatlimb == '8':
                    pass
                elif eatlimb == '9':
                    pass
                else :
                    print("-----------------------------------------------------\n")
                    print(" Nope. You can't get out of it now. You wanted to    ")
                    print(" eat. So now you have to eat!\n")
                    input("Enter to begin the feast...")


    else :
        print("\n-----------------------------------------------------\n")
        print(" That was the wrong answer and as a result you died. ")
        print(" Better luck next time", name + "!\n")
        sys.exit()
