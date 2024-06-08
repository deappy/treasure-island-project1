print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''')

print("\nWelcome to Treasure Island.")
print("Your mission is to find the treasure.")
ch1=input('You are at an intersection in the path. Which way do you wish to go?\nEnter your left or right option to type.\n')

if ch1.lower()=="left":
  ch2 = input("\nYou have reached a lake. Do you wish to swim or wait for a boat?")
  if ch2.lower()=="wait":
    print("\nYou have reached the island unharmed using a boat. There is a house with 3 doors.\nOne red,one blue, one yellow.")
    ch3 = input("\nWhich door do you choose?\n(Hint:What color do we associate with the centre of a daisy flower)")
    if ch3.lower()=="yellow":
      print("\nYou have found the treasure. You win!")
    elif ch3.lower()=="red":
      print("\nYou have entered a room full of fire. Game Over.")
    elif ch3.lower()=="blue":
      print("\nYou have entered a room full of beasts. Game Over.")
    else:
      print("\nYou have entered a room that does not exist. Game Over.")
else:
  print("\nThere was a trap and you fell into a hole. Game Over.")
