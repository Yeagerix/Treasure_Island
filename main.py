
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


health = 2
damage = 1


if health == 0:
  print("You lost all your health. GAME OVER.")

left_right = input("You see a cave in the distance. You don't know how to get up there, so you must choose. left or right ? ").lower()
if left_right == "right":
  health -= damage
  print(f"You Trip and take {damage} damage. You now have a total of {health} Health  ")
  sneak_attack = input("Do you want to sneak Past or attack the dragon? ").lower()
  if sneak_attack == "attack":
    health -= damage 
    print(f"You try to attack but you take {damage} damage and now have a total of {health} Health ") 
    if health == 0:
      print("You lost all your health. GAME OVER.")
      exit()
    dragon_chase = input("The Dragon now chases you. Do you go left or right ? ").lower()
    if dragon_chase == "right":
      print("The Dragon burns you to a crisp GAME OVER ")
      exit()
    elif dragon_chase == "left":
      print("Well Done, You've Escaped the dragon.")
      doors3 = input("You see three Doors ahead of you. Which door do you pick? door1 , door2 , door3 ? ").lower()
      if doors3 == "door1":
        print("Game Over!")
        exit()
      elif doors3 == "door2":
        health -= damage
        print(f"You take 1 damage. You know have {health} health ")
        if health == 0:
          print("Game Over you lost all your health")
      elif doors3 == "door3":
        print("Well done you win!")
      else:
        print("What are you doing...That's not an Answer!")
 

  elif sneak_attack == "Sneak":
    print("You Successfully sneak past the dragon")
    dragon_awakens = input("The dragon hears you sneaking past him. He awakens and chases you. Which way do you go? left or right ? ").lower()
    if dragon_awakens == "right":
      print("The Dragon burns you to a crisp. GAME OVER ")
      exit()
    elif dragon_awakens == "left":
      print("Well done you've escaped. ")
     
    


elif left_right == "left":
  print("You make you way up a path that leads to the cave.")
  attack_sneak = input("You see a Dragon in the cave sleeping. Do you sneak past or attack it? ").lower()
  if attack_sneak == "attack":
    health -= damage
    print(f"You try to attack but you take {damage} damage and now have a total of {health} Health, ")
    chase2 = input("The dragon chases you. You now have to pick left Or right Which one?").lower()
    if chase2 == "right":
      print("The Dragon Burns you to a crisp. GAME OVER")
      exit()
    elif chase2 == "left":
      print("Well done You've escaped the dragon. ")
      doors2 = input("You come across three doors door1 , door2 , door3. Which door do you pick? ").lower()
      if doors2 == "door1":
        print("Game Over")
        exit()
      elif doors2 == "door2":
        health -= damage
        print(f"You take 1 Damage. You now have a total of {health} health")
        if health == 0:
          print("Game Over")
          exit()
        else:
          print("You've made it by a scratch lucky you! Well done for completing it")
      elif doors2 == "door3":
        print("You awaken. well done... You've completed the game")
      else:
        print("What are you doing. That's not an answer!!")
    
    
  elif attack_sneak == "Sneak":
    print("You sucessfully sneak past the dragon..But wait")
    chase3 = input("The dragon notices you and chases you which way do you go? left or right ? ").lower()
    if chase3 == "Left":
      print("Well done. You've escaped the dragon")
      doors = input("There are three doors ahead of you door1 , door2 , and door3. Which door do you take?").lower()
      if doors == "door1":
        print("You fall into an abyss. GAME OVER")
        exit()
      elif doors == "door2":
        health -= damage
        print(f"You take {damage} damage and now have a total of {health} health")
        if health == 0:
          print("GAME OVER")
          exit()
      elif doors == "door3":
        print("Well Done, You've awoken up from this terrible nightmare in your lovely comfy bed. Snuggle in some more won't you :) only a couple more days before WW3 breaks out.")
      else:
        print("What are you doing? that's not an option! Well...You're dead now. So good job")
    elif chase3 == "right":
      print("You've come up to a dead end. The dragon Burns you to a crisp, GAME OVER")
      exit()

