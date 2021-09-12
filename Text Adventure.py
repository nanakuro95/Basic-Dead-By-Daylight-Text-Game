survivor_names = {
    "Big Booty" : "Jane Romero",
    "Blendette" : "Claudette Morell",
    "I'm a cap!" : "Detective Tap",
    "Hippie" : "Kate",
    "Anime" : "Rin Kimura",
    "Locker bitch" : "Dwight",
    "Sandwich" : "Jill Valentine",
    "Hair flip" : "Leon Kennedy",
    }
killers = {
    "Bam Bam" : "Oni",
    "UwU Scary" : "Spirit",
    "Flat!!" : "Pyramid Head",
    "Cutest boy" : "Demogorgon",
    "The Lag!" : "Nemesis",
    "Stalker" : "Ghostface",
    "Ping Pong" : "Blight",
    "Bing Bong" : "Wraith",
}

def game_over():
    if "2":
        print("I don't blame you for giving up to be honest. Unless you're on PC, this game is broken.")
    if "1":
        print("Why the fuck did you DC? You've got it easy compared to the killer! Look! They're in the corner crying!")
def pallet_slam():
    if "1":
        print("You slam a pallet down on the killer chasing you and run off to hide.")
    if "2":
        print("You are stunned by the pallet. Absolutely tragic.")
        game_over()
def hooked():
    hook_count = ""
    hook_limit = 3
    if "1" and hook_count == 0:
        print("This is the first time you've been hooked. Hang on in there!")
        hook_count += 1
        hook_count == 1
    elif "1" and hook_count == 1 and not(hook_limit):
        print("Oof. Where are those friends of yours I wonder.")
        hook_count += 1
    elif "1" and hook_count == 2 and not(hook_limit):
        print("Uhoh. Looks like death is imminent!")
        hook_count += 1
    else:
        if "1" and hook_count == 3:
            game_over()

    if "2" and hook_count == 1:
        print("Nice one!")
    elif "2" and hook_count == 2:
        print("Ooh! Another one under the belt!")
    else:
        if "2" and hook_count == 3:
            print("You got one!!")

def chase_ends():
    if "1":
        print("You get downed by the killer and placed on the hook. Hope you've got competent team mates.")
        hooked()

    if "2":
        print("You down the survivor and hook them on the closest hook. Nice job!")

def chest():
    print("You unlock the chest and manage to find a toolbox. This will help you fix the generators faster!")
    generator_fix()

def generator_fix():
    print("You begin fixing the generatory at an impossible speed. That killer will never stand a chance.")
    print("\nYou hear a heartbeat from close by! It's Shia Labeof! Just kidding, but it is a killer so ya'd better start running!")
    chase_begins()

def generator_break():
    if "2":
        print("You destroy the generator and any progress that's been made on it. Nicely done. Now go get em!")
        chase_begins()

def chase_begins():
    if "1":
        print("Run...")
        print("After a bit of looping - you toxic bitch - the killer downs you.")
        chase_ends()
    if "2":
        print("You find a couple　annoying survivors trying to repair the gen. One runs off to the right and fucks up skill check, the other to the left.")
        print("\nWhich one will you chase? (l or r)")
        print("(l) You chase the survivor to the left, managing to down them. That was a lucky hit. Go hook that annoyance!")
        print("(r) You chase the bitch on the right but lag hits you right in the soul and you freeze up, allowing them the slam a pallet down on your head.")

        answer = input(">")

        if "l" in answer:
            generator_break()
            chase_ends()
        if "r" in answer:
            pallet_slam()
            chase_ends()

def start_game():
    print("You select a survivor or killer. Which will you pick? (1 or 2)?")
    print("(1) You pick a shitty survivor who has an automatic advantage.")
    print("(2) You pick a killer. You poor bastard.")

    answer = input("Choose from the list above: ")

    if answer == "1":
        print("You load into an area you are unfamiliar with and see a generator off to the left and a chest to the right. What do you do? (A or B)?")
        print("(A) You run to the generator and start repairing it.")
        print("(B) Fuck the gen. Grab the goodies in the chest!")

        answer = input(">")

        if "a" in answer:
            generator_fix()

        if "b" in answer:
            chest()

    if answer == "2":
        print("You've chosen the role of killer and sadly, this isn't going to be fun. You spawn in an unfamiliar area.")
        print("\nThere is a noise coming from in front a few meters off and a noise to your right. Which way do you go? (f or r)")
        print("(f) You trudge forward towards the noise.")
        print("(r) You follow the noise on your right")

        answer = input(">")

        if "f" in answer:
            generator_break()

        if "r" in answer:
            chase_begins()

start_game()
