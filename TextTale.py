import pickle
import os
import sys
import time
import random
import winsound


totallove = 1
totalhp = 20
agsorelife = 1
sanslife = 1
papyruslife = 1
undynelife = 1
toriellife = 1
mettatonlife = 1
mettatonexlife = 1
butterscotchpie = 0
totalfun = random.randint(0, 100)
child = str(input("name the fallen child:"))
if child == "Gaster" or child == "gaster":
    exit()
if child == "Flowey" or child == "flowey":
    print("Hey! I already chose that name.")
    time.sleep(3)
    exit()
time.sleep(1)
print("this is your name "  +  str(child))
time.sleep(1)
print("You’ve fallen into the underground. Do you want to go to the next room or explore this one")
time.sleep(5)
fallen = input("Choose one: 'explore' or 'move on'")
if fallen == "explore":
    print("you look around a little. you find flowers beneath you nothing else")
    time.sleep(4)
    print("you move on because there is nothing else")
    time.sleep(2)
if fallen == "move on":
    time.sleep(2)
print("you see a smiling flower. You approach it.")
time.sleep(2)
print("The flower says: 'howdy! I'm flowey, flowey the flower.'")
time.sleep(3)
print("Hmm...")
time.sleep(4)
print("You're new to the UNDERGROUND, aren’tcha")
time.sleep(4)
print("Golly you must be so confused.")
time.sleep(4)
print("Someone ought to teach you how things work around here!")
time.sleep(3)
print("I guess little old me will have to do.")
time.sleep(2)
print("Ready? Here we go!")
time.sleep(2)
print("See that heart? That is your SOUL, the very culmination of your being!")
time.sleep(4)
print("Your soul starts off weak but can grow strong if you gain a lot of LV.")
time.sleep(4)
print("What’s LV stand for? Why, LOVE of course!")
time.sleep(3)
print("You want some LOVE, don’t you?")
time.sleep(2)
print("Don’t worry, I’ll share some with you!")
time.sleep(3)
print("Down here, LOVE is shared through...")
time.sleep(3)
print("Little white… ‘friendliness pellets.’")
time.sleep(3)
print("Are you ready?")
time.sleep(2)
print("Get as many as you can!")
pellet = input("'collect' or 'move out of way'")
if pellet == "move out of way":
    print("Hey buddy, you missed them")
    print("Let’s try again, okay?")
pellet = input("dodge or collect")
if pellet == "dodge":
    print("Is this a joke? Are you braindead? RUN. INTO. THE. BULLETS!!!")
    time.sleep(4)
    print("You know what’s going on here, don’t you?")
    print("You just wanted to see me suffer")
if pellet == "collect":
    time.sleep(3)
print("You idiot in this world it is kill or be killed.")
time.sleep(2)
print("You are surrounded by the flower’s bullets")
time.sleep(3)
print("Suddenly the flower is hit with a fireball")
time.sleep(1)
print("A goat appears?")
time.sleep(1)
print("The goat: What a terrible creature, torturing such a poor, innocent youth... Ah, do not be afraid, my child. I am Toriel, caretaker of the Ruins... I pass through this place every day to see if anyone has fallen down.")
time.sleep(4)
print("Toriel: You must have fallen down... do not worry I will take care of you.")
time.sleep(1)
print("Toriel: Please follow me this way")
time.sleep(1)
print("You follow Toriel into the next room")
time.sleep(1)
print("Toriel: Allow me to educate you on the workings of the ruins... \n The ruins are full of puzles and you must solve them to advance to the next room")
time.sleep(2)
print("Toriel walks across a series of buttons")
time.sleep(1)
print("After completing the process a door opens...")
time.sleep(1)
print("You follow Toriel to the next room")
time.sleep(1)
print("Toriel: Listen child... I am going to ask you to do something very challenging... \n I need you to walk to the end of this room... by yourself.")
time.sleep(1)
print("Toriel runs down the hall")
time.sleep(1)
print("You follow her")
time.sleep(3)
print("You continue to follow her")
time.sleep(5)
print("...")
time.sleep(5)
print("You are almost to the end of the hallway")
time.sleep(1)
print("You see a pillar... look behind it? (yes or no)")
lookbehindpillar = input(":")
if lookbehindpillar == "yes":
    time.sleep(1)
    print("You look behind the pillar and see Toriel")
    time.sleep(1)
    print("Toriel: ...")
    time.sleep(2)
if lookbehindpillar == "no":
    time.sleep(1)
print("You reach the end of the hallway")
time.sleep(1)
print("Toriel comes out from behind the pillar")
time.sleep(1)
print("Toriel: It is okay child do not worry I did not leave you I am sorry if I frightend you...")
time.sleep(1)
print("Toriel: I have to run an erand. \n Please remain in this room until I get back... it is dangerous to continue.")
time.sleep(1)
time.sleep(1)
print("Toriel: on second thought how about I give you a cell phone.")
time.sleep(2)
print("You can make calls with it")
time.sleep(2)
print("Goodbye!")
obeytorielandleaveroom = input("continue or do not")
if obeytorielandleaveroom == "do not":
    print("You wait for around 10 minutes...")
    time.sleep(5)
    print("You get bored and continue")
if obeytorielandleaveroom == "continue":
    time.sleep(1)
print("You leave the room and encounter a froggit")
time.sleep(2)
print("compliment or fight...")
firstfroggitcomporfight = input("")
if firstfroggitcomporfight == "fight":
    time.sleep(1)
    print("You killed the froggit...")
    time.sleep(2)
    print("You gained LOVE!")
    totallove = totallove + 1
    print(f"Your love is now at {totallove}")
    time.sleep(1)
if firstfroggitcomporfight == "compliment":
    time.sleep(1)
    print("The froggit does not understand but is flattered anyway... \n You spare the froggit")
    time.sleep(1)
print("You move on")
time.sleep(1)
print("You are now in a room with two doors. Go up or down")
firstroomupordownmostercandy = input("(up or down):")
if firstroomupordownmostercandy == "up":
    print("You go up and see a dish. It is labeled Free Candy Take One")
    takethecandyyorn = input("Take a peice of candy?(yes or no)")
    if takethecandyyorn == "yes":
        print("You take a peice of candy... it tastes like a gym sock...")
        time.sleep(1)
print("You go back to the main room and head down the hall")
time.sleep(2)
print("In the next room there is a rock and a big waited button and the exit is covered with spikes")
time.sleep(2)
print("Do you want to push the rock on to the pad")
pushsinglerockontopad = input("(yes or no)")
time.sleep(2)
if pushsinglerockontopad == "no":
    print("You do not push the rock on to the pad however you cannot progress past the spikes")
    time.sleep(2)
    print("You realize you have to push the rock")
time.sleep(2)
print("You push the rock onto the pad... \n The spikes drop into the floor")
time.sleep(2)
print("You progress to the next room")
time.sleep(2)
print("You see three rocks with three similar pads and more spikes")
time.sleep(2)
print("You move the rocks onto the pads")
time.sleep(1)
print("The spikes fall into the ground")
time.sleep(1)
print("There are a pile of leaves on the floor")
time.sleep(2)
print("There is a ghost laying on top of them")
time.sleep(2)
print('The ghost is saying "z" outload repeatedly')
time.sleep(2)
print("Move it with force?")
movenabstablookwithforceyesorno = input("yes or no")
if movenabstablookwithforceyesorno == "no":
    print("The ghost keeps saying 'z' outloud repeatedly... \n You have no choice but to move it with force")
    time.sleep(1)
time.sleep(1)
print("Here comes Nabstablook")
time.sleep(1)
whattodonabfirst = input("Attack or Cheer")
time.sleep(1)
if whattodonabfirst == "Cheer":
    print("Nabstablook: heh...")
    time.sleep(1)
    print("Nabstablook attacks!")
    time.sleep(1)
    print("You take 1 damage!")
    time.sleep(1)
    print("You tell nabstablook a joke...")
    time.sleep(1)
    print("Nabstablook: heh heh...")
    time.sleep(2)
    print("Nabstablook wants to show you something...")
    print("Let me try...")
    time.sleep(2)
    print("Nabstablook makes itself a hat")
    time.sleep(2)
    print("Nabstablook: Do you like it? I call it dapperblook.")
    time.sleep(2)
    print("You say you like it")
    time.sleep(2)
    print("Nabstablook: Gee. I usually come to the ruins because no one is around but today I met someone nice!")
    time.sleep(2)
    print("I will get out of your way now...")
    time.sleep(2)
if whattodonabfirst == "Attack":
    print("Nabstablook:... You know you can't kill me right? I'm like... A ghost and all.")
    time.sleep(2)
    print("Nabstablook: This is awkward I will just get out of your way")
    time.sleep(2)
print("You walk past the leaves nabstablook was on")
time.sleep(2)
print("You encounter a whimsun!")
time.sleep(2)
print("Attack or Spare")
killorsparewhismunfirst = input(":")
if killorsparewhismunfirst == "Attack":
    print("You killed the whimsun in 1 shot!")
    time.sleep(2)
    totallove = totallove + 1
    print("Your LOVE has increased!")
    print(f"You are now at {totallove} LOVE!")
    time.sleep(1)
if killorsparewhismunfirst == "Spare":
    print("You spare the Whimsun")
    time.sleep(1)
print("You continue to progress")
time.sleep(2)
print("There is another room with two door ways")
spiderbakesaleornah = input("Go right or up: ")
if spiderbakesaleornah == "right":
    print("You go to the right... \n You see a spider web with lots of spiders")
    time.sleep(2)
    print("There is a sign that says 'Spider Bake Sale'")
    time.sleep(2)
    print("There is a spider in the web")
    time.sleep(2)
    spiderbakesaledialog = input("(What is going on here or What are the prices)")
    if spiderbakesaledialog == "what is going on here" or spiderbakesaledialog == "What is going on here" or spiderbakesaledialog == "What are the prices" or spiderbakesaledialog == "what are the prices":
        print("This is a spider bakesale, we sell spider donuts. The prices are 7 gold each")
        time.sleep(2)
        print("Do you want to buy a donut")
        buyadonutorno = input(":")
        if buyadonutorno == "yes":
            print("You purchased a donut")
            time.sleep(2)
print("You enter the 'up' room")
time.sleep(2)
print("You are outside!")
time.sleep(2)
print("You see Toriel returning")
time.sleep(2)
print("Toriel: Oh my I should not have left you alone for so long...")
time.sleep(2)
print("I am sorry that was foolish of me")
time.sleep(2)
print("Come with me")
time.sleep(2)
print("Toriel leads you into a house")
time.sleep(2)
print("This is your home now!")
time.sleep(2)
print("I suppose I cant hide it from you anymore...")
time.sleep(2)
print("SURPISE!")
time.sleep(1)
print("I baked you a butterscotch pie!")
time.sleep(2)
print("Oh my god! I think I left it in the oven!")
time.sleep(2)
print("I will be back child!")
time.sleep(2)
newhomewaitfortoriel = input("Wait here for Toriel or go explore the house? (wait or explore)")
if newhomewaitfortoriel == "wait" or newhomewaitfortoriel == "Wait":
    print("You wait for Toriel")
    time.sleep(5)
    print("Toriel seems to be taking a while.")
    time.sleep(2)
    print("You are bored")
    time.sleep(3)
    print("You explore the house")
if newhomewaitfortoriel == "explore" or newhomewaitfortoriel == "Explore":
    time.sleep(1)
print("There are two rooms...")
newhomeroom12or3 = input("Room 1 2 or 3?")
if newhomeroom12or3 == "3":
    print("You see a sign")
    time.sleep(2)
    print("It reads: Room under renovations")
    time.sleep(1)
    print("You look at room 2")
    time.sleep(3)
    print("Oh no it seems this is Toriel's room.")
    time.sleep(2)
    print("You are a decent human so you do not go in")
    time.sleep(2)
if newhomeroom12or3 == "2":
    print("You look at room 2")
    time.sleep(3)
    print("Oh no it seems this is Toriel's room.")
    time.sleep(2)
    print("You are a decent human so you do not go in")
    time.sleep(2)
if newhomeroom12or3 == "1":
    time.sleep(1)
print("You go inside room 1")
time.sleep(2)
print("It is a bedroom!")
time.sleep(2)
print("There is a box of toys...")
time.sleep(1)
print("None of them interest you")
time.sleep(2)
print("There is a closet")
time.sleep(2)
print("It is filled with... Nothing")
time.sleep(2)
print("There is a cozy bed.")
time.sleep(2)
print("You lay in it for a while...")
time.sleep(4)
print("You wake up on the bed \n it is light outside")
time.sleep(3)
print("There is a slice of butterscotch pie on the floor")
time.sleep(2)
print("would you like to pick it up?")
takebutterscotchpieyesorno = input("(yes or no)")
if takebutterscotchpieyesorno == "yes" or takebutterscotchpieyesorno == "Yes":
    print("You take the Butterscotch pie")
    butterscotchpie = butterscotchpie + 1
    print("(The Butterscotch pie... \n This item will heal you in battle)")
    time.sleep(2)
if takebutterscotchpieyesorno == "no" or takebutterscotchpieyesorno == "No":
    print("You leave the Butterscotch pie behind")
    time.sleep(2)
print("You leave the room")
time.sleep(2)
print("Toriel is in the living room reading a book titled 72 Uses for Snails")
time.sleep(2)
print("You approach her...")
time.sleep(2)
print("Toriel: Is there something you need?")
time.sleep(2)
print("How to exit the ruins | When can I go home?")
torielquestion = input("how to exit or home")
time.sleep(1)
if torielquestion == "home" or torielquestion == "Home":
    print("Oh... I don't think you understand this is your home now.")
    time.sleep(2)
if torielquestion == "how to exit" or torielquestion == "How to exit":
    print("Uhh... \n How about a fun snail fact instead?")
    time.sleep(2)
torielquestion2 = input("how to exit or snail fact")
if torielquestion2 == "snail fact" or torielquestion2 == "Snail fact":
    print("I am glad you are interested")
    time.sleep(1)
    print("How about this one")
    time.sleep(2)
    print('"While slow snails are actually incredibly active especially when they are at a 66 fun level."')
    time.sleep(2)
    print("Would you like to know how much fun you are at?")
    time.sleep(1)
    howmuchfun = input(":")
    if howmuchfun == "yes" or howmuchfun == "Yes":
        print("Okay, it seems you are at...")
        time.sleep(2)
        print(f"{howmuchfun} fun!")
if torielquestion2 == "how to exit" or torielquestion2 == "How to exit":
    time.sleep(2)
print("Wait here...")
time.sleep(2)
print("There is something I must take care of.")
time.sleep(2)
print("Toriel walks down the hall and into the basement")
time.sleep(2)
print("Would you like to follow her?")
time.sleep(2)
print('(yes or no)')
time.sleep(1)
followtoriel = input(": ")
if followtoriel == "no" or followtoriel == "No":
    print("You wait for Toriel to come back...")
    time.sleep(10)
    print("Nothing is happening")
    time.sleep(5)
    print("wait or follow")
    followtoriel2 = input(": ")
    if followtoriel2 == "wait" or followtoriel2 == "Wait":
        print("You wait a little longer")
        time.sleep(10)
        print("Toriel still is not coming back")
        time.sleep(5)
        print("You are done waiting")
        time.sleep(2)
if followtoriel == "Yes" or followtoriel == "yes":
    time.sleep(1)
print("You follow Toriel")
time.sleep(2)
print("You are in the basement...")
time.sleep(2)
print("You go a little further")
time.sleep(1)
print("You see Toriel!")
time.sleep(2)
print("She has a weird expression")
time.sleep(2)
print("Please do not follow me child")
time.sleep(2)
print("She walks further down the hallway")
time.sleep(1)
print("You catch up to her")
time.sleep(2)
print("You cannot follow me child, they will kill you \n ASGORE will kill you")
time.sleep(2)
print("She walks further down the hall and goes around a corner")
time.sleep(2)
print("You catch up to her again")
time.sleep(1)
print("She is standing by a big door")
time.sleep(2)
print("This is the only exit to the ruins and I am going to destroy it so that you do not get killed")
time.sleep(2)
print("You really want to leave so bad?")
time.sleep(2)
print("Fight me then prove to me you are ready")
time.sleep(2)
print("Your SOUL appears infront of you...")
time.sleep(2)
print("Toriel is preparing an attack")
time.sleep(1)
print("What will you do")
fighttoriel1 = input("attack or mercy")
if fighttoriel1 == "mercy" or fighttoriel1 == "Mercy":
    print("You tell Toriel you do not want to fight")
    time.sleep(2)
    print("If you aren't going to fight how can I expect you to get past Asgore and survive???")
    time.sleep(2)
    print("Toriel attacks")
    gethitbytorielorno1 = random.randint(1, 10)
    if gethitbytorielorno1 >= 6:
        print("Toriel's attack hits -2 hp")
        totalhp = totalhp -2
        time.sleep(1)
    if gethitbytorielorno1 <= 5:
        print("Toriel's attack missed")
        time.sleep(2)
    print("You tell Toriel you still do not want to fight.")
    time.sleep(2)
    print("Something seems to change about her expression")
    time.sleep(2)
    print("Toriel attacks again but all of her attacks are missing")
    time.sleep(2)
    print('You tell Toriel that neither of you need to fight')
    time.sleep(2)
    print("Toriel seems defeated")
    time.sleep(2)
    print("Pathetic isn't it")
    time.sleep(1)
    print("I can not even save 1 child")
    time.sleep(2)
    print("Toriel hugs you and walks away")
    time.sleep(2)
    print("You go through the door")
if fighttoriel1 == "attack" or fighttoriel1 == "Attack":
    print("You attack Toriel")
    time.sleep(2)
    print("Toriel has 20 hp left")
    time.sleep(2)
    print("Toriel attacks back!")
    time.sleep(2)
    gethitbytorielmurder1 = random.randint(1, 10)
    if gethitbytorielmurder1 >= 6:
        print("Toriel's attack hits you lose 3 hp")
        totalhp = totalhp - 1
        time.sleep(2)
    print("You hit Toriel again")
    toriellife = toriellife - 1
    print("You...")
    time.sleep(1)
    print("Really hate me that much?")
    time.sleep(2)
    print("Toriel turns into dust")
    time.sleep(2)
    totallove = totallove + 1
    print(f"You gained LOVE! You are now at {totallove} LOVE")
    time.sleep(2)
    print("You walk through the door")
print("TEXTTALE")
time.sleep(5)
print("You walk forward...")
time.sleep(2)
print('you keep going...')
time.sleep(2)
print("The ground has snow on it?")
time.sleep(2)
print("You are in a forest!")
time.sleep(2)
print("You think you hear something behind you")
time.sleep(2)
print("You keep walking")
time.sleep(2)
print("You make it to a bridge")
time.sleep(2)
print("It has bars on it?")
time.sleep(1)
print("They are wide enough to walk through")
time.sleep(2)
print("There are foot steps approaching from behind...")
time.sleep(2)
print("H U M A N . . .")
time.sleep(2)
print("Don't you know how to greet a new pal?")
time.sleep(2)
print("Turn around and shake my hand")
time.sleep(2)
print("You turn around and shake his hand")
winsound.PlaySound('whoopee.mp3', winsound.SND_FILENAME)
time.sleep(2)
print("A whoopee cushion???")
time.sleep(2)