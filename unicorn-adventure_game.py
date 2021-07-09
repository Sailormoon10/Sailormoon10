
import time #imports a module to add a pause.
MY_NAME = input("Tell me your name:  ")
answer_A = ["A","a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y","y","yes"]
no = ["no","N", "n"]


required = ("\nUse only, A, B, or C\n") #cuts down on duplication


#The story is broken into sections, starting with "intro"

def intro():
    print ("Your car veered off the road and barely misses the oak tree, "
    "falling into a ditch. You awaken the "
    "next morning in a thick, eerie forest. Head spinning and "
    "fighting the urge to vomit, you stand and marvel at your new, "
    "unfamiliar setting. The peace quickly fades when you hear a "
    "grotesque sound emitting behind you. A mystical unicorn is "
    "running towards you. You will: (Choose one)")
    time.sleep(1)
    print ("""\n
     A. Grab a rock and throw it at the unicorn
     B. Pick up some leaves to try and show a peace offering by giving it food to eat
     C. Run!""")
    choice = input(">>> ")
    if choice in answer_A:
        option_rock()
    elif choice in answer_B:
        option_food()
    elif choice in answer_C:
        print("\nThe jolt of energy required to run leaves you sluggish, you faint from "
        "the blunt force from your car accident and get eaten by a wolf... Game over!")
        time.sleep(2)
        print("\nYou died!")
        print("Wanna play again? Y/N: ")
        play = input(">>> ")
        if play in yes:
            intro()
        elif play in no:
            print("\nThanks for playing!")
            print("Program terminated.")
        else:
            print("Invalid input. Program terminated")
    else:
        print(required)
        intro()
        
def option_rock():
    print ("\nThe unicorn bellows out in anger, and starts to run faster towards you,  "
    "this time, with a menacing stare. What do you do next?:")
    time.sleep(1)
    print("""
    A. Run
    B. Try and find food to gain it's trust
    C. Run to a nearby rotted hollow log, the unicorn will never be able to crawl in """)
    choice = input(">>> ")
    if choice in answer_A:
        option_run()
    elif choice in answer_B:
        option_food()
    elif choice in answer_C:
        option_log()
    else:
        print(required)
        option_rock()
               
def option_food():
    print("\nThat is all the unicorn wanted, you were standing in their pile of food  "
    "and it hadn't eaten all day. The unicorn eats its' food quietly while staring at you.  "
    "It raises its' head and holds out his hoof for you to shake it. It sees the wound  "
    "on your head and gestures you to climb up on its' back. Will you:")
    time.sleep(1)
    print("""
    A. Step back in terror
    B. Shake its' hoof, and reluctantly climb on
    C. Go back to your car and look for help, I mean you did just suffer a concussion!""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nYou trip on a rock that you swear wasn't there and hit you head on a tree trunk... "
        "this has GOT to be your worst day ever, and now your last... you died!")
        print()
        print("Wanna play again? Y/N: ")
        play = input(">>> ")
        if play in yes:
            intro()
        elif play in no:
            print("\nThanks for playing!")
            print("Program terminated.")
        else:
            print("Invalid input. Program terminated")
    elif choice in answer_B:
        option_fly()
    elif choice in answer_C:
        option_emt()
    else:
        print(required)
        option_food()
        
def option_log():
    print("\nYou hide out in the log and let out a sigh of relief as you finally get to catch your breath.  "
   "You lay your head down but feel something bumpy. As you look down, you uncover something so vile, "
    "a 3 eyed snake staring right at you! You barf and quickly try to climb out. As you dust off the moss "
   "you see:")
    time.sleep(1)
    print("""
    A. Two state troopers staring at you with guns drawn
    B. An EMT officer and two cops
    C. The unicorn""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nCOP: Put your arms up where we can see them! You are under arrest for the possession of drugs  "
        "you have the right to remain silent... ")
        print("\nOh no, it looks like your doppelganger has committed a crime, you are going to jail from mistaken identity,  "
        "better call Saul!")
        time.sleep(2)
        print("\nThe end")
        print()
        print("Wanna play again? Y/N: ")
        play = input(">>> ")
        if play in yes:
            intro()
        elif play in no:
            print("\nThanks for playing!")
            print("Program terminated.")
        else:
            print("Invalid input. Program terminated")        
    elif choice in answer_B:
        option_emt()
    elif choice in answer_C:
        option_mad_unicorn()
        
def option_emt():
    print("\nThere you see a cop and an EMT rushing to help you.")
    time.sleep(1)
    print("\nEMT: Are you okay? Is this your car? The EMT man says as him and his partner lay out a stretcher for you.")
    time.sleep(6)
    print()
    print(MY_NAME,":....uh yea I think so,")
    time.sleep(1)
    print("...what happened?")
    time.sleep(2)
    print("\nEMT:You got into a car crash and you may have a concussion, we'll help you onto the stretcher, "
    "we got to get you to a hospital, quick!")
    time.sleep(6)
    print()
    print(MY_NAME,":I'm fine, but I just saw a unicorn in those trees, it was chasing after me!")
    time.sleep(4)
    print("""\nThe EMTs look at each other in confusion.""")
    time.sleep(3)
    print("\nCOP: Yeah kid, I know it might seem real "
    "but that's just the concussion talking, we're taking you to the hospital right now.")
    time.sleep(7)
    print()
    print(MY_NAME,":I swear! You guys think I'm making this up? Go look, I'm not crazy, wait... no, let me out of here!")
    time.sleep(7)
    print("\nThe EMTs are now struggling to hold you down to sedate you. You slowly feel your eyes getting heavy.")
    time.sleep(6)
    print("""You think to yourself, "yeah this might have just been a dream" then slowly fall into a slumber.""")
    time.sleep(6)
    print("\nThe End.")
    print()
    print("Wanna play again? Y/N: ")
    play = input(">>> ")
    if play in yes:
        intro()
    elif play in no:
        print("\nThanks for playing!")
        print("Program terminated.")
    else:
        print("Invalid input. Program terminated")
     
        
def option_adventure():
    print("\nThe smell repels the unicorn and it runs away... whew! That was close, you slowly walk back to your car.")
    time.sleep(1)
    option_emt()
    
def option_mad_unicorn():
    print("\nThe unicorn is now fiery with rage, it jumps up to pounce on you."
    "As you cover your face and cower in fear, the unicorn stops and "
    "notices your wrist. Close call, but what exactly was on your wrist?")
    time.sleep(1)
    print("""
    A. Your new shiny watch, gifted for your birthday.
    B. BBQ sauce, from the meal that you ate a few hours ago.
    C. Pink wristband from the club that you were at""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nThe glare from your watch blinds the unicorn, it runs away leaving you in disbelief... wooh close call! Now get back to your car and get help!")
    if choice in answer_B:
        option_adventure()
    if choice in answer_C:
        print("\nThe unicorn mistakes your pink wristband for a rare delicacy and takes a big bite...out of your hand! You bleed out, and now you are dead!")
        print()
        print("Wanna play again? Y/N: ")
        play = input(">>> ")
        if play in yes:
            intro()
        elif play in no:
            print("\nThanks for playing!")
            print("Program terminated.")
        

def option_fly():
    print("\nThis feels unreal! You climb on its' back and the unicorn flies into the sky, you can see the whole city from here, but can they see us? "
    "You are flying over the lush trees and cool lakes, you think to yourself, What is going on, am I dreaming? As you turn back you can see your car wreck has caused  "
    " a bottleneck, oh well you say to yourself,after a near-death experience it's time to live my life! Riding on this unicorn sure is it! The unicorn slowly glides down "
    "and lands right in front of this marble cave. You climb off and step into a pile of: ")
    time.sleep(1)
    print("""
    A. Glowing marbles
    B. Unicorn rainbow doo doo
    C. Purple leaves """)
    choice = input(">>> ")
    if choice in answer_A:
        option_marble()
    if choice in answer_B:
        option_doo_doo()
    if choice in answer_C:
        option_leaves()
        
def option_marble():
    print("""Whoa WTF?" You carefully pick up the 5 marbles and take a good look at them,
    The marbles emit a beautiful glow of green, pink, and blue. You don't know what it is but you  
    suddenly feel your once throbbing head feel like normal again. You touch your head,
    Wait I'm no more bleeding? These must be some type of healing marbles!" You put them in your  
    pocket and catch up to the unicorn walking into the cave. As you peer inside, you see:  """)
    time.sleep(1)
    print("""
    A. A family of unicorns looking at you
    B. A unicorn with a crown on it's  throne
    C. A table of food """)
    choice = input(">>> ")
    if choice in answer_A:
        option_medicine()
    if choice in answer_B:
        print("There's a unicorn king at the throne! The king says something to the one who brought you over, and he does not sound happy. He finally says in English")
        time.sleep(5)
        print("\nYou are not welcomed here, human, go back to where you came from and never show your face in this marble cave again!")
        time.sleep(5)
        print("\nYou cower in fear and the unicorn gestures you to get back on it's back. You climb on and the unicorn quickly takes you back to the spot it found you in\n")
        time.sleep(5)
        print("""\nUnicorn: "Sorry bud, I thought he'd help you. Here take this." He takes some gold grass that was at the cave and applies it to your forehead, the throbbing "
        "you felt is now gone!\n As he flies back, you turn around and """)
        option_emt()
    if choice in answer_C:
        print("You hurry over to the table grab a spoon, and take a big bite of some type of acai bowl,  it tastes sweet, it tastes savory, it tastes.... \n")
        time.sleep(1)
        print("Wait, you start to that throbbing headache come back, but this time it's worse. Didn't your parents teach you not to take what's not yours? Who said unicorn food is "
        "good for humans... smh you were so close...\n")
        time.sleep(1)
        print("You died!")
        print()
        print("Wanna play again? Y/N: ")
        play = input(">>> ")
        if play in yes:
            intro()
        elif play in no:
            print("\nThanks for playing!")
            print("Program terminated.")
        else:
            print("Invalid input. Program terminated")

        
    
def option_medicine():
    print(""" "You think, "Am I dead, because what am I looking at?" There are about 6 unicorns in different hues of pastel colors.
    The pink unicorn walks slowly to you and peers cautiously at this new creature. It walks back behind a black marble room and
    brings out shiny gold grass in its' mouth. The pink unicorn sprinkles it gently on your forehead, and in an instant
    "you are healed!""")
    time.sleep(7)
    print("\nUnicorn: What happened?\n")
    time.sleep(2)
    print(MY_NAME,":Wait you guys can talk?\n")
    time.sleep(2)
    print("They laugh... a little bit too much")
    time.sleep(3)
    print("""\nBlue Unicorn: "Noooo, we bark." The younger blue unicorn shouts from across the cave.
    Now the room erupts in laughter while you looked annoyed.""")
    time.sleep(5)
    print("""\nYou let out a sigh and shrug. "Sorry, it's not everyday you see unicorns roaming around." """)
    time.sleep(5)
    print("""\nThe purple unicorn says from the other side of the room, "\nPurple Unicorn: Yeah we stay hidden,
    we know how you humans love meat, and that's not going to be me! "
    "Y'all can have the cows and pigs, we good over here!" """)
    time.sleep(8)
    print(" \nThey laugh even more.\n")
    time.sleep(2)  
    print(MY_NAME,":Well, can I stay with you guys? I have no family, and I just crashed my last mode of transportation")
    time.sleep(5)
    print("\nThe pink unicorn gestures to a pile of leaves for you to sit.")
    time.sleep(3)
    print("\nPink Unicorn: You are welcome here, have a seat")
    time.sleep(3)
    print("\nWow! You didn't expect that did you? Enjoy your new life with the unicorns!")
    time.sleep(3)
    print("\n\nThe End!")    
    
def option_run():
    print("\nWhy are you running?! You have no energy, you faint and are found 2 days later by an EMT... but it is too late, you died!")
    print()
    print("Wanna play again? Y/N: ")
    play = input(">>> ")
    if play in yes:
        intro()
    elif play in no:
        print("\nThanks for playing!")
        print("Program terminated.")
    else:
        print("Invalid input. Program terminated")
  

def option_doo_doo():
    time.sleep(1)
    print("\nYuck! You notice your shoes are now in a pile of poop. The unicorn looks over at you and snickers.\n")
    time.sleep(4)
    print(MY_NAME,":Hey you talk?")
    time.sleep(2)
    print("\nIt stares blankly at you...\n")
    time.sleep(2)
    print(MY_NAME,":Ummm okay...")
    time.sleep(2)
    print("\nThe unicorn leads you into a cave and you can't believe what you see!")
    time.sleep(3)
    option_medicine()


        
intro()
        
