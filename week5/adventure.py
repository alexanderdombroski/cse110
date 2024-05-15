import os

def cls(): #I copied this code these two lines from https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console. 
    os.system('cls' if os.name=='nt' else 'clear')

cls()

name = input("\nWhat is your hero's name? ").title()
gender = ""

valid = False
while valid == False:
    gender = input("What is your hero's gender (MALE/FEMALE)? ")
    if gender.lower() == "male":
        heshe = "he"
        himher = "him"
        hisher = "his"
        valid = True
    elif gender.lower() == "female":
        heshe = "she"
        himher = "her"
        hisher = "her"
        valid = True

cls()

gender = input("What is your hero's gender (MALE/FEMALE)? ").lower()
if gender == "male":
    heshe = "he"
    himher = "him"
    hisher = "his"
elif gender == "female":
    heshe = "she"
    himher = "her"
    hisher = "her"
else:
    print("I don't know what that gender is.. I'm refering to you as it")
    heshe = "heshe"
    himher = "it"
    hisher = "its"


# --------------- Choice 0 ---------------

print(f"""{name} is ready for an adventure! {heshe.capitalize()} gets ready to leave, but first 
{heshe} needs to grab {hisher} favorite adventure gear. {heshe.capitalize()} grabs a rope, 
map, compass, flashlight, and a snack.""")

food = ""
print("\nType one of the options in ALL CAPS\n")
while food not in('sandwich', 'trail mix'):
    food = input(f"Does {heshe} bring a SANDWICH or TRAIL MIX? ").lower()
cls()

# --------------- Choice 0 Result ---------------

print(f"{name} grabs {hisher} {food} and leaves for the forest.")
print(f"To the left {heshe} sees a nearby stream and to the right {heshe} sees a dark cave.")
direction = ""
while direction not in('left', 'right'):
    direction = input(f"Which direction will {heshe} go, LEFT or RIGHT? ").lower()
cls()

if direction == 'right':
    # --------------- Choice 1 Result ---------------

    print(f"{name} leaves the forest behind and enters a large cave. {heshe.capitalize()}\n"
          f"can hear the sound of droplets pattering on the cave floor.\n"
          f"{name} feels the warmth that comes from shelter from the\n"
          f"wind, but {heshe} feels something else too. Shining the flashlight\n"
          f"directly in front of {himher}, {name} sees a big wall of dark fur.\n")
    input("Hit ENTER")
    print("""
      /¯¯¯\___/¯¯¯\ 
     │   __   __   │
     │    ■   ■    │
     │      |      │
     │    └─┴─┘    │
      \___________/
          \n""" # Made using extended ASCII characters
          f"It's a bear!\n\n"
          f"1. RUN away\n"
          f"2. FIGHT it courageously\n"
          f"3. FEED it {hisher} {food}")
    option = ""
    while option not in("fight", "feed", "run"):
        option = input(f"What of these options will {name} do? ").lower()
    cls()
    
    if option == "fight":
        # --------------- Choice 1.1 Result ---------------
        print(f"{name} charges at the bear and strikes it in the nose. The bear\n"
              f"shakeS it's head a couple tImes and sits dowN, rubbinG it's nose\n"
              f"with it's paws. It turned out to be a black bear and it feels too\n"
              f"intimidated  and in pain to strike back. {name} leaves for home with an\n"
              f"epic tale to tell. As {heshe} arrives near home, a squirrel jumps from\n"
              f"a tree onto {hisher} face.")
        while option not in("shake","yell", "sing"):
            option = input(f"Will {heshe} SHAKE it off or YELL for help? ").lower()
        cls()

        if option == "shake":
            # --------------- Choice 1.1.1 Result ---------------
            print(f"{name} shakes the squirrel off mistified why nature keeps attacking\n"
                  f"{himher}. {heshe.capitalize()} returns home to get some rest. {heshe.capitalize()} survives never\n"
                  f"wanting to go on an adventure in the woods again.")
        elif option == "yell":
            # --------------- Choice 1.1.2 Result ---------------
            print(f"Nobody comes. More squirrels jump and they steal {name}'s {food}. You lose.")
        else: # option == sing
            # --------------- Choice 1.1.2 Result ---------------
            print(f"The squirell jumps off and starts dancing. {name} dances\n"
                  f"with it. You found the secret ending. You win.")

    elif option == "feed":
        # --------------- Choice 1.2 Result ---------------
        print(f"{name} offers the bear {hisher} {food}. It sniffs at it, opening its jaws wide.")
        option = ""
        while option not in("hold", "throw"):
            option = input(f"Will {name} coninue to HOLD the food or THROW it at the bear? ").lower()
        cls()
        if option == "hold" :
            # --------------- Choice 1.2.1 Result ---------------
            print(f"The bear eats the {food} and then eats {name}. You lose.")     
        else: # option == throw
            # --------------- Choice 1.2.2 Result ---------------
            print(f"{name} throws the {food} at the bear and barely makes it home alive.")

    else: # option == run
        # --------------- Choice 1.3 Result ---------------
        print(f"{name} trips {hisher} way back out the cave. The bear does not pursue.")
        while option not in("home", "river"):
            option = input(f"Would {name} rather head HOME or spend the rest of the day at the RIVER? ").lower()
        cls()

        if option == "home":
            # --------------- Choice 1.3.1 Result ---------------
            print(f"{name} heads home hoping never to see that cave or the bear again. {heshe.capitalize()}\n"
                  f"survived. Well done.")
            
        else:
            # --------------- Choice 1.3.2 Result ---------------
            print(f"{name} heads for the river but gets stopped by some other bears who are fishing. Panicked,\n"
                  f"{heshe} trips and falls down a hill. You lose.")

else: # River
    # --------------- Choice 2 Result ---------------
    print(f"{name} walks for a while and approaches a river. {heshe.capitalize()} sees\n"
          f"a object shimmering in the river. Would {name} like to CROSS the river or\n"
          f"WALK upstream?\n")
    option = ""
    while option not in("walk", "cross"):
        option = input(f"What of these options will {name} do? ")
    cls()

    if option == "cross":
        # --------------- Choice 2.1 Result ---------------
        cls()
        print(f"{name} stumbles accross the stones exposed in the river and makes it half\n"
              f"way, but then {heshe} falls in. {hisher.capitalize()} {food} is now all wet. {heshe} can\n"
              f"see a glimmer in the stream.\n")
        while option not in("home", "search"):
            option = input(f"Would {name} like to go HOME or SEARCH the waters\n"
                           f"to find out what the shimmer is? ").lower()
        cls()

        if option == "home":
            # --------------- Choice 2.1.1 Result ---------------
            print(f"{name} makes {hisher} way home and calls it a day. {heshe.capitalize()} dries\n"
                  f"off and makes lunch after throwing away {hisher} {food}.")
            
        else: # option == "search"
            # --------------- Choice 2.1.2 Result ---------------
            print(f"{name} found what appears to be gold flecks. {heshe.capitalize()} took note of\n"
                  f"the location and went home to get panning supplies.")

    else: # Walk upstream
        # --------------- Choice 2.2 Result ---------------
        print(f"As {name} walks upstream, {heshe} notices an abandondoned watermill.")
        while option not in("in", "out"):
            option = input(f"Would {name} like to investigate IN the mill or OUT around back? ").lower()
        cls()

        if option == "in":
            # --------------- Choice 2.2.1 Result ---------------
            print(f"An old prospector used to run this mill, and he hunted for gold in his\n"
                  f"free time. {name} found a few containers of gold flecks. You win!")
            
        else: # option == "out"
            # --------------- Choice 2.2.2 Result ---------------
            print(f"{name} walks out back and notices a ton of spider webs. Turning\n"
                  f"around, {heshe} sees a giant spider that attacks and captures {himher}.\n"
                  f"{name} is trapped in web with no way of escape. ")

print("\nTHE END\n")