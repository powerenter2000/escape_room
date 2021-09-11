import time

def main():
    print("You have just woken up and noticed you're in a room by yourself.")
    time.sleep(2)
    print("You look around and notice it appears to be a bedroom")
    time.sleep(2)
    y = input("You hear a voice and it asks 'What is your name?' ")
    print("Welcome",y,"Stand up and begin your journey")
    time.sleep(2)
    print("You are standing up and notice items in the room")
    time.sleep(2)
    options()

def main_2():
    options()

def letter():
    x = input("Do you pick up the letter? y or n: ")
    if x == "y":
        print("You read the letter, 'The color of the sky will set you free'")
        time.sleep(4)
        print("You now focus your attention on the other items")
        time.sleep(2)
        options()
    else:
        print("You chose to not pick up the letter, The room now starts to fill up with a poisonous gas")
        time.sleep(2)
        print("You did not escape")

def clown():
    x = input("Have you selected the other options? Are you ready to touch the clown? y or n: ")
    if x == "y":
        print("The clowns eyes are always so colorful, which eyeball shall set you free? ")
        time.sleep(4)
    options = "Blue Eye", "Red Eye", "Green Eye", "Orange Eye"
    for index, value in enumerate(options, 1):
        print("{}. {}".format(index, value))
        selection = int(input("Which eyeball do you choose "))
        options_2 = "1", "3", "6", "10"
    for index, value in enumerate(options_2, 1):
        print("{}. {}".format(index, value))
        selection_2 = int(input("HOw many turns do you turn the eyeball "))
        if selection == 1 and selection_2 == 3:
            time.sleep(2)
            print("Thinking")
            time.sleep(2)
            print("You see a door magicaly open in front of you and you escape")
        else:
            time.sleep(2)
            print("You chose incorrectly")
            time.sleep(2)
            print("The room now starts to fill up with a poisonous gas because of your wrong selections")
            time.sleep(2)
            print("You did not escape!")
    else:
        main_2()
        time.sleep(2)

def options():
    options = "Under the Bed","The Letter", "The clown"
    for index, value in enumerate(options,1):
        print("{}. {}".format(index, value))
        selection = int(input("Which item do you want to investigate? "))
    if selection == 2:
        letter()
    elif selection == 1:
        bed()
    else:
        clown()

def bed():
    x = input("You notice there are books under the bed, do you reach for the books? y or n: ")
    if x == "y":
        print("You reach your arm under the bed and pull out 6 books numbered 1 through 7, you notice a book is missing, the 6th one")
        time.sleep(5)
        print("You now focus your attention on the other items")
        options()
    else:
        print("You chose to not reach your arm under the bed, The room now starts to fill up with a poisonous gas")
        time.sleep(2)
        print("You did not escape")

main()