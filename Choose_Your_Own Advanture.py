import random

name = input("Enter your name: ")
print("Welcome {name} to the World of Fantasy!")
knight = 1
wizard = 2
theif = 3
dice = random.randint(1, 20)
role = int(input("Which role will you choose to become? \nPress 1 to become a worthy knight, \nPress 2 to become a powerful wizard, \nPress 3 to become a clever theif\n"))

if role == 1:
    print("You are a part of the kingdom in the northern region and work as an honest knight until the kingdom is attacked and destroyed by a evil wizard.  \nYou somehow manage to survive and after go out to search for the wizard to avenge your kingdom. ")
    print("As you go on your journy you find a small town and speak to its people about the evil wizard and they tell you they saw him go into a cave.  \nAs you go into that cave you find the evil wizard and attack him.  \nYou must roll a 15 or above to beat him")
    if dice >= 15:
        print("Dice roll:", dice, " You defeat the wizard and avenged your kingdom")
    else:
        print("Dice roll:", dice, " You have lost and everything was in vain")
elif role == 2:
    print("You are a wizard researching an ancient tomb until something goes horribly wrong.  \nSomething comes out of it and a ancient monster breaks free and roams the world once more.  \nYou go out to search for the monster in order to stop it from destroying everything.")
    print("As you are searching you discover local city near by and decide to take a look.  \nYou find a tarven and speak to the bar wench for information, but as soon as the conversion ends you hear screaming from outside.  \nYou go out and find that the monster you are searching for is attacking the city.  \nWhat do you do?")
    choice = int(input("Choice 1: Fight the monster \nChoice 2: Wait for backup."))
    if(choice == 1):
        print("You must roll a 18 or above to win")
        if dice >= 18:
            print("Dice roll:", dice, " You have defeated the monster and saved the day.")
        else:
            print("Dice roll:", dice, " The monster has overwhelmed you and the city was destroyed.  All hope was lost.")
    else:
        print("Backup arrives and the city guard begin to help you.  \nYou must roll a 14 or above to defeat the monster.")
        if dice >= 14:
            print("Dice roll:", dice, " You and the city guard have killed the monster and the day is saved once more.")
        else:
            print("Dice roll:", dice, " You and the city guard are killed and the city is no more.")
else:
    print("You are a theif from the southern lands and as you go back home after finishing a heist, you are suddenly attacked by a group of bandits.  \nThe bandits knock you out and steal all of your treasure.  \nNow you go out and search for these bandits in order to reclaim what was once yours.")
    print("As you go on your search you find an abanded house and decide to go check it out.  As you go inside you find some hidden loot underneath the floor.  \nDo you take it or move on.")
    Decision = int(input("Choice 1: Take the loot \nChoice 2: Move on"))
    if(Decision == 1):
        print("As you finish looting the place, you see that there are dozens of guards surrounding the place and that you must find a way out no matter what.  \nYou must roll an 16 or above to escape the guards.")
        if dice >= 16:
            print("Dice roll:", dice,"You escaped and move on and as you go on you notice that there is a hidden cave nearby and find that the bandits you are looking for are in there.  \nDo you confront them or wait till night time to do so.")
            Verdict = int(input("Choice 1: Confront now \nChoice 2: Wait till night to do so"))
            if(Verdict == 1):
                print("You must roll an 18 or higher to defeat the bandits.")
                if(dice >= 18):
                    print("Dice roll:", dice,"You defeat the bandits and reclain your stolen loot.  The day is yours.")
                else:
                    print("Dice roll:", dice,"You lost and yours days are nigh.")
            else:
                print("You wait until it is nightfall and while everyone is alseep you decide to take back what was yours without alerting everyone.  \nYou must roll and 15 or higher to get your treasure without alerting the bandits.")
                if(dice >= 15):
                    print("Dice roll:", dice,"You succedded and escape with your tresure and ride off into the night with glory on your back.  \nThe End.")
                else:
                    print("Dice roll:", dice,"You failed to not awaken the bandits and as everyone gets up you must prepare to fight them.  \nYou must roll an 19 or above to win.")
                    if dice >= 19:
                        print("Dice roll:", dice,"You defeated the bandits and reclain your stolen loot.  The day is yours.")
                    else:
                        print("Dice roll:", dice,"You lost and yours days are nigh.")
        else:
            print("Dice roll:", dice,"You are caught by the guards and are put in prison for the rest of your days.")       