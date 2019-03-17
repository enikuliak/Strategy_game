# lab 12
# Strategy Game
# Yauheniya Nikulyak, Thach Doan, Ardee Magday


import sys

#global variables
hasKey = False    #initially a player doesn't have a key
countDiamonds = 0  # initially a player doesn't have diamonds
hasShovel = False   # item needed to find the secret room
secretRoomFound = False
hasSword = False
alreadyPickedDiamond1 = False
alreadyPickedDiamond2 = False
alreadyPickedDiamond3 = False
alreadyPickedDiamond4 = False
alreadyPickedDiamond5 = False


def intoAndHelp():
  print("Welcome to the Adventure House!")
  print("This is a quick description of the game.")
  print("In each room you will be told which directions you can go.")
  print("You'll may be able to go north, south, east or west by typing that direction.")
  print("In each room there is a diamond.")
  print("You can open the chest only if you have a key.")
  print("You can find a key in one of the rooms.")
  print("Once you opened a chest, you can pick up a diamond.")
  print("If you collect all 5 diamonds, you will win the game.")
  print("There is a secret room in the house.")
  print("You will need a shovel to find a secret room.")
  print("You can find a shovel in one of the rooms.")
  print("But think twice before you decide to find the secret room.")
  print("Type help to redisplay this introduction.")
  print("Type exit to quit at any time.")

def startGame():
  intoAndHelp()
  print("##################################################################################")
  print("Let's begin...You are in the Foyer.")
  actions()
  
def foyer():     # You are brought back to the Foyer
  print("###################################################################################")
  print("You are in the Foyer again.")
  actions()


def actions():
  print("You are able to go north, south, east or west by typing that direction.")
  while True:
    user_choice = requestString("What are you going to do?")
    if "help" in user_choice:
      intoAndHelp()
      continue
    elif "exit" in user_choice:
      print("Ok, goodbye.")
      sys.exit()  
    elif "north" in user_choice:
      room3()
    elif "south" in user_choice:
      print("You would be outside. Try to choose another direction.")
      continue
    elif "east" in user_choice:
      room1()
    elif "west" in user_choice:
      room4()
    # if player type anything than desired directions  
    else:
      print("Your intention is undefined. Let's try again.")
      continue

# in this room a player can open a chest if he has a key, and try to find a secret room by digging, but
# there is no secret room here, so he just tries and continue game. 
def room1():
  print("###################################################################################")
  print("Welcome to the room 1.")
  print("Unfortunately, your choice brought you to the Torture Chamber of the time of Spanish Inquisition.")
  print("It would be wise to escape from here as fast as you can")
  print("You can choose to go north, or to go west.")
  print("Look around and maybe you can find something useful to help you escape this house, just type 'check'. ")
  print("Type exit to quit at any time.")

  global hasKey
  global hasShovel
  global countDiamonds
  global secretRoomFound

  previous_choice = None
  # player can pick only one diamond at a room
  global alreadyPickedDiamond1
  while True:
    user_choice = requestString("What are you going to do?")
    if "help" in user_choice:
      intoAndHelp()
      continue
    elif "exit" in user_choice:
      print("Ok, goodbye")
      sys.exit()
    elif "check" in user_choice:
      lookAroundRoom1()
      continue  
    elif "north" in user_choice:
      room2()
    elif "west" in user_choice:
      print("You are in a Foyer again.")
      actions()
    elif "east" in user_choice:
      print("You cannot go that way. Try again.")
      continue
    elif "south" in user_choice:
      print("You cannot go that way. Try again.")
      continue
    elif hasKey == False and "open" in user_choice:
      print("It looks like you need a key to open this box.")
      continue
    elif hasKey == True and "open" in user_choice and alreadyPickedDiamond1 == False:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You've opened the box.")
      print("There is a diamond inside. You can pick up by using the 'pick up' command")
      previous_choice = user_choice
      continue
    elif hasKey == True and "open" in user_choice and alreadyPickedDiamond1 == True:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You've already picked up a diamond from this box.")
      continue
    elif hasKey == True and previous_choice == "open" and "pick up" in user_choice and alreadyPickedDiamond1 == False:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You've got your diamond.")
      alreadyPickedDiamond1 = True
      countDiamonds = countDiamonds + 1
      print("Now you have " + str(countDiamonds) + " diamonds.")
      # check win condition
      if countDiamonds == 5 and secretRoomFound == False:
        winGame()
      else:
        continue
    # try to find a secret room
    elif hasShovel == True and "dig" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("Be cautious! You are very curious.")
      print("You have been digging, but haven't found anything in this room.")
      continue
    # dig without shovel 
    elif "dig" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You need a shovel to dig. Try to find it in another room.")
      continue
    # if player type anything than desired directions  
    else:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("Your intention is undefined. Let's try again.")
      continue

def lookAroundRoom1():  
  print("###################################################################################")
  print("There is a box with a diamond here.")
  print("You can open it if you have a key by typing open.")
  print("You can pick up a diamond then by typing pick up.")
  print("If you have shovel, you can try to find a secret room.")
  print("But think twice before you decide to find it.")      

# in this room a player can find a key that open all chests in any room to collect 5 diamonds to win a game
def room2():
  print("###################################################################################")
  print("Welcome to the room 2.")
  print("You might be tired and a little scared.")
  print("Let's relax. This is a Meditation room.")
  print("You can stay here as long as you want.")
  print("After you feel better, you can continue your adventure.")
  print("But before, look around and maybe you can find something useful to help you escape this house, just type 'check'. ")
  print("You can go north, or you can go south.")
  print("Type exit to quit at any time.")

  global hasKey
  global hasShovel
  global countDiamonds
  global secretRoomFound

  previous_choice = None
  global alreadyPickedDiamond2
  while True:
    user_choice = requestString("What are you going to do?")
    if "help" in user_choice:
      intoAndHelp()
      continue
    elif "exit" in user_choice:
      print("Ok, goodbye.")
      sys.exit()  
    elif "check" in user_choice:
      lookAroundRoom2()
      continue
    elif "north" in user_choice:
      room3()
    elif "south" in user_choice:  
      room1()
    elif "west" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("There is nothing in that direction. Try again.")
      continue  
    elif "east" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You've got a key. Now you can open some chests in the house.")
      hasKey = True
      continue
    elif hasKey == True and "open" in user_choice and alreadyPickedDiamond2 == False:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You've opened the box.")
      print("There is a diamond inside. You can pick up it using the 'pick up' command")
      previous_choice = user_choice
      continue
    elif hasKey == True and "open" in user_choice and alreadyPickedDiamond2 == True:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You've already picked up a diamond from this box.")
      continue
    elif hasKey == True and previous_choice == "open" and "pick up" in user_choice and alreadyPickedDiamond2 == False:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You've got your diamond.")
      alreadyPickedDiamond2 = True
      countDiamonds = countDiamonds + 1
      print("Now you have " + str(countDiamonds) + " diamonds.")
      # check win condition
      if countDiamonds == 5 and secretRoomFound == False:
        winGame()
      else:
        continue
    #if a player has a shovel, he can try to find secret room in any room, but if there is no secret room in a place
    #he tries to dig, just continue game
    elif hasShovel == True and "dig" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("Be cautious! You are very curious.")
      print("You have been digging, but haven't found anything in this room.")
      continue
    # dig without shovel 
    elif "dig" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You need a shovel to dig. Try to find it in another room.")
      continue  
    # if player type anything than desired directions 
    else:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("Your intention is undefined. Let's try again.")
      continue

# helper function for room 2
def lookAroundRoom2():  
  print("###################################################################################")
  print("You see a key if you look east; go in that direction to pick it up.")    
  print("With the help of this key, you can open some chests in this house and collect diamonds to win.")
  print("There is a chest with a diamond in the room at your right.")
  print("You can open it if you have a key by typing 'open'.")
  print("After you open it, you can pick up a diamond by typing 'pick up'.")
  print("If you have a shovel, you can try to find a secret room.")
  print("But think twice before you decide to search for it.")


# helper function for room 3
def lookAroundRoom3():
  print("###################################################################################")
  print("The walls are made of gingerbread, but that doesn't seem too appealing.")
  print("There is a bunch of sugar-free gum everywhere, but you won't eat it because ")
  print("a group of Italian researchers suggested that high doses of Aspartame might ")
  print("raise the risk of blood - related cancers in rats.")
  print("To your left though, is a table with a blue and red skittle. It is almost as if ")
  print("you have a decision to make. Maybe you should try one.")
  print("Type blue skittle or red skittle to eat one.")
 
# the function has lose condition, a player can try to find secret room here and a diamond.  
def room3():
  print("###################################################################################")
  print("Welcome to the Dessert Room. Everything in here seems to be sweet and edible. ")
  print("You have an urge to eat something. There is candy everywhere, but what to eat?" )
  print("Take a look around and maybe you will find something that catches your eye.")
  print("Type 'check' to examine the room.")
  print("If you want to go somewhere else, you are able to go south and north.")

  global hasKey
  global hasShovel
  global countDiamonds
  global secretRoomFound
  
  global alreadyPickedDiamond3
  while True:
   user_choice = requestString("What are you going to do ?")
   if "help" in user_choice:
     intoAndHelp()
     continue
   elif "exit" in user_choice:
     print("Ok, goodbye.")
     sys.exit()
   elif "south" in user_choice:
     room4()
   elif "north" in user_choice: 
     print("~~~~~~~~~~~~~~~~~~~~~~~")
     print("That goes outside the house. A powerful force brings you back.")
     foyer()
   elif "east" in user_choice:
     print("~~~~~~~~~~~~~~~~~~~~~~~")
     print("You cannot go that way. Try again.")
     continue
   elif "west" in user_choice:
     print("~~~~~~~~~~~~~~~~~~~~~~~")
     print("You cannot go that way. Try again.")
     continue
   elif "check" in user_choice:
     lookAroundRoom3()
     continue
    # try to find a secret room, but there is no secret room here, just continue game.  
   elif hasShovel == True and "dig" in user_choice:
     print("~~~~~~~~~~~~~~~~~~~~~~~")
     print("Be cautious! You are very curious.")
     print("You have been digging, but haven't found anything in this room.")
     continue  
   # dig without shovel 
   elif "dig" in user_choice:
     print("~~~~~~~~~~~~~~~~~~~~~~~")
     print("You need a shovel to dig. Try to find it in another room.")
     continue
   elif "blue skittle" in user_choice and alreadyPickedDiamond3 == False:
     print("~~~~~~~~~~~~~~~~~~~~~~~")
     print("Magically a diamond appears in front of you. Nice choice!")
     alreadyPickedDiamond3 = True
     countDiamonds = countDiamonds + 1
     print("Now you have " + str(countDiamonds) + " diamonds.")
     #check win condition
     if countDiamonds == 5 and secretRoomFound == False:
       winGame()
     continue
   # diamond already picked
   elif "blue skittle" in user_choice and alreadyPickedDiamond3 == True:
     print("~~~~~~~~~~~~~~~~~~~~~~~")
     print("You've already got your diamond.")
   # lose condition  
   elif "red skittle" in user_choice:
     print("~~~~~~~~~~~~~~~~~~~~~~~")
     print("You have been poisoned by the red skittle. You die a slow and painful death. Please try again. ")
     sys.exit()
   # if player type anything than desired directions  
   else:
     print("~~~~~~~~~~~~~~~~~~~~~~~")
     print("Your intention is undefined. Let's try again.")
     continue  

# in this function a player can find a shovel, that would help him to find a secret room further      
def room4():
  print("###################################################################################")
  print("Welcome to the Zombie Quarantine Room. There are three people, who used to be people, in different cells.")
  print("There are cells numbered one, two and three.")
  print("There is a small chest in each of the 3 cells, behind each zombie.")
  print("In this room you can go north, west or south.")
  print("Look around and maybe you can find something useful to help you escape this house, just type 'check'. ")
  print("If you have shovel, you can try to find a secret room.")
  print("Type exit to quit at any time.")

  global hasKey
  global hasShovel
  global countDiamonds
  global secretRoomFound
  global hasSword
  zombie1Dead = false
  zombie2Dead = false
  zombie3Dead = false
  previous = None
  previous1 = None
  global alreadyPickedDiamond4
  while True:
    user_choice = requestString("What are you going to do?")
    if "help" in user_choice:
      intoAndHelp()
      continue
    elif "exit" in user_choice:
      print("Ok, goodbye.")
      sys.exit()	
    elif "north" in user_choice:
      room3()
    elif "west" in user_choice:
      foyer()
    elif "south" in user_choice:  
      room5()
    elif "east" in user_choice:
      print("You cannot go that way. Try again.")
      continue  
    elif "check" in user_choice:
      lookAroundRoom4()
      continue
    # player finds a shovel  
    elif "left" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("Now you have a shovel")
      hasShovel = True  
      continue
    # player gets a sword
    elif "right" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You got the sword. Now you have a weapon.")
      hasSword = True
      
    # player tries to find secret room, but there is no secret room here
    elif hasShovel == True and "dig" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("Be cautious! You are very curious.")
      print("You have been digging, but haven't found anything in this room.")
      continue
    # dig without shovel 
    elif "dig" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You need a shovel to dig. Try to find it in another room.")
      continue
      
    # approach FIRST without sword
    elif "first" in user_choice and hasSword == false:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You approached the zombie without a weapon and get eaten alive.")
      print("Please be prepared next time.")
      sys.exit()	
    
    # approach SECOND without sword
    elif "second" in user_choice and hasSword == false:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You approached the zombie without a weapon and get eaten alive.")
      print("Please be prepared next time.")
      sys.exit()	
      
    # approach THIRD without sword
    elif "third" in user_choice and hasSword == false:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You approached the zombie without a weapon and get eaten alive.")
      print("Please be prepared next time.")
      sys.exit()	
        
    #only one of the cells can be opened with a key  
    elif "first" in user_choice and hasSword == true and hasKey == True:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You kill the zombie with the sword and reach the chest.")
      print("But unfortunately the key can't be used on this chest.")
      continue
    elif "first" in user_choice and hasSword == true and hasKey == False:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You kill the zombie with the sword and reach the chest.")
      print("Unfortunately you need a key before you try to open it.")
      continue
    elif "third" in user_choice and hasSword == true and hasKey == True:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You kill the zombie with the sword and reach the chest.")
      print("But unfortunately the key can't be used on this chest.")
      continue
    elif "third" in user_choice and hasSword == true and hasKey == False:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You kill the zombie with the sword and reach the chest.")
      print("Unfortunately you need a key before you try to open it.")
      continue
    elif "second" in user_choice and hasSword == true and hasKey == True:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You kill the zombie with the sword and reach the chest.")
      print("You feel like you can use your key here.")
      print("You can try to open chest with the 'open' command.")
      previous = user_choice
      continue
    elif "second" in user_choice and hasSword == true and hasKey == False:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You kill the zombie with the sword and reach the chest.")
      print("Unfortunately, you need a key before you try to open it.")
      continue
    # open a chest  
    elif hasKey == True and hasSword == true and previous == "second" and "open" in user_choice and alreadyPickedDiamond4 == False:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("The chest has been opened.")
      print("There is a diamond inside. You can pick up it using 'pick up' command")
      previous1 = user_choice
      continue
    # diamond already picked
    elif hasKey == True and "open" in user_choice and alreadyPickedDiamond4 == True:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You've already picked up a diamond from this box.")
      continue
    # pick up a diamond
    elif hasKey == True and previous1 == "open" and "pick up" in user_choice and alreadyPickedDiamond4 == False:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You've got your diamond.")
      alreadyPickedDiamond4 = True
      countDiamonds = countDiamonds + 1
      print("Now you have " + str(countDiamonds) + " diamonds.")
      # check win condition
      if countDiamonds == 5 and secretRoomFound == False:
        winGame()
      else:
        continue
    # if player type anything than desired directions    
    else:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("Your intention is undefined. Let try again.")
      continue
      
# helper function for room 4      
def lookAroundRoom4():
  print("###################################################################################")
  print("In front there are 3 zombie cells; you can approach them by using the commands 'first', 'second' or 'third'")
  print("Maybe you can find something interesting inside if you have a key.")
  print("On the right you see a dying man who looks like he was bitten to death.")
  print("There is a shovel at your left. If you'd like to pick it up, type 'left'.")
  print("There is a sword to your right. If you'd like to pick it up, type 'right'.")
  print("Behind you the door has closed by itself.")
  print("Type exit to quit at any time.")


# there is secret room underground, if a player finds it, he will lose the game.
def room5():
  print("###################################################################################")
  print("Welcome to the chamber of thirst. You will suffer from the lack of water and scorching, dry air.")
  print("There is nothing but an endless road ahead of you.")
  print("In this room there is a treasure chest. You can open it with the 'open' command only if you have a key.")
  print("Look around and maybe you can find something useful to help you escape this house. Type 'check'. ")
  print("If you a have shovel, you can try to find a secret room.")
  print("In this room you can only go back north.")
  print("If you feel like you can't take it choose 'exit'.")

  global hasKey
  global hasShovel
  global countDiamonds
  global secretRoomFound
  
  previous_choice = None
  global alreadyPickedDiamond5
  while True:
    user_choice = requestString("What are you going to do?")
    if "help" in user_choice:
      intoAndHelp()
      continue
    elif "exit" in user_choice:
      print("Ok, goodbye.")
      sys.exit()	
    elif "north" in user_choice:
      room4()
    elif "south" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You cannot go that way. Try again.")
      continue  
    elif "east" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You cannot go that way. Try again.")
      continue 
    elif "west" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You cannot go that way. Try again.")
      continue   
    elif "check" in user_choice:
      lookAroundRoom5()
      continue
    # player can open the chest only if there is a key  
    elif hasKey == False and "open" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You need the key to open the chest. Look for it in one of the rooms.")
      continue
    elif hasKey == True and "open" in user_choice and alreadyPickedDiamond5 == False:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You've opened the box.")
      print("There is a diamond inside. You can pick up it using the 'pick up' command.")
      previous_choice = user_choice
      continue
     # diamond already picked
    elif hasKey == True and "open" in user_choice and alreadyPickedDiamond5 == True:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You've already picked up a diamond from this box.")
      continue
    elif hasKey == True and previous_choice == "open" and "pick up" in user_choice and alreadyPickedDiamond5 == False:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You've got your diamond.")
      alreadyPickedDiamond5 = True
      countDiamonds = countDiamonds + 1
      print("Now you have " + str(countDiamonds) + " diamonds.")
      # player win a game if he has 5 diamonds and didn't find secret room
      if countDiamonds == 5 and secretRoomFound == False:
        winGame()
      else:
        continue
    # lose condition: secret room is a trap, player lose the game if he finds a secret room    
    elif hasShovel == True and "dig" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("Upon digging deep enough, you discover a large chamber under the sandy surface.")
      print("In it is a large sand serpent who was awakened from the sound of digging.")
      print("It is furious from being iterrupted from it's hibernation and proceeds to devour you.")
      print("Sometimes curiousity really kills the cat... Please try again.")
      sys.exit()
    # dig without shovel 
    elif "dig" in user_choice:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("You need a shovel to dig. Try to find it in another room.")
      continue
    # if player type anything than desired directions  
    else:
      print("~~~~~~~~~~~~~~~~~~~~~~~")
      print("Your intention is undefined. Let's try again.")
      continue

# helper function for room 5
def lookAroundRoom5():
  print("###################################################################################")
  print("In front of you is full of sandstorms.")
  print("The Treasure chest is at your right.")
  print("There is nothing behind you to look at.")

# after a player win a game, he can choose to play again or to exit
def winGame():
  global hasKey
  global hasShovel
  global countDiamonds
  global secretRoomFound
  print("~~~~~~~~~~~~~~~~~~~~~~~")
  print("Congratulations! You have won the game!")
  while True:
    user_choice = requestString("Do you want to play again? Yes/No")
    if "yes" in user_choice.lower():
      hasKey = False    #initially a player doesn't have a key
      countDiamonds = 0  # initially a player doesn't have diamonds
      hasShovel = False   # item needed to find a secret room
      secretRoomFound = False
      startGame()
    else:
      print("Ok, bye.")
      sys.exit()  
      
startGame()

                                                                                                                                                                                                                                            