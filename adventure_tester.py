import adventure_class

#monster attribute list, 10 health 1 dmg
monster = [10,1]

print("What is your name?")
hero_name = raw_input()
hero = adventure_class.Hero(hero_name)
print

def play_again():
    print("Would you like to play again? y/n")
    while True:
        choice = input()
        if choice == "y":
            playing = True
            break
        elif choice == "n":
            playing = False
            break
        else:
            print("Enter a valid choice.")

def status():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("Name:" + hero.name + "    Health:" + str(hero.health))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
def battle():
    print("Let the fight begin!!")
    print("What will you do!")
    while True:
        if hero.health <= 0:
            print("You lose the battle.")
            break
        elif monster[0] <= 0:
            print("You win the battle.")
            break
        
        print("You attack the monster...")
        if hero.items["weapon"] == "sword":
            print("You deal 3 dmg.")
            monster[0] -= 3
        else:
            print("You deal 1 dmg.")
            monster[0] -= 1

        print("The monster attacks you....")
        print("You take " + str(monster[1]) + " dmg.")
        hero.health -= 1
        
def room1():
    print("You enter the first room...")
    print("In front of you, there is a key, pick it up?")
    print("yes or no?")
    while True:
        choice = raw_input()
        if choice == "yes":
            hero.items["item1"] = "key"
            print("You pick up the key")
            break
        else:
            print("You dont pick of the key")
            break
    
def room2():
    print("You enter the second room...")
    print("There is a monster!!!")
    print("What are you going to do?!")
    print("Fight or Run?")
    while True:
        choice = raw_input()
        if choice == "fight":
            battle()
            break
        elif choice == "run":
            hero.pos -= 1
            break
        else:
            print("Please choose fight or run.")
    
    
def get_room():
    pos = hero.pos
    if pos == 1:
        room1()
    elif pos == 2:
        room2()
        
def play():
    get_room()

    #main decision loop
    while True:
        print
        print("1) Move")
        print("2) Inventory")
        print("3) Status")
        print("What will you do?")
        choice = input()

        if choice not in range(1,4):
            print("Please enter a valid choice.")
            print
            
        elif choice == 1:
           print("You move to the next room.")
           hero.pos += 1
           print
           break
           
        elif choice == 2:
            print("You check your bag...")
            hero.list_items()
            print
            
        elif choice == 3:
            status()

playing = True
while playing:
    play()
