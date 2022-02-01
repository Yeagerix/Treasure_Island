
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


health = 3
damage = 1

if health == 0:
  print("You lost all your health. GAME OVER.")

left_right = input("You see a cave in the distance. You don't know how to get up there, so you must choose. Left or Right ? ")
if left_right == "Right":
  health -= damage
  print(f"You Trip and take {damage} damage. You now have a total of {health} Health  ")
  sneak_attack = input("Do you want to Sneak Past or Attack the dragon? ")
  if sneak_attack == "Attack":
    health -= damage 
    print(f"You try to attack but you take {damage} damage and now have a total of {health} Health ") 
    if health == 0:
      print("You lost all your health. GAME OVER.")
      exit()
    dragon_chase = input("The Dragon now chases you. Do you go Left or Right ? ")
    if dragon_chase == "Right":
      print("The Dragon burns you to a crisp GAME OVER ")
      exit()
  elif sneak_attack == "Sneak":
    print("You Successfully sneak past the dragon")
    dragon_awakens = input("The dragon hears you sneaking past him. He awakens and chases you. Which way do you go? Left or Right ? ")
    if dragon_awakens == "Right":
      print("The Dragon burns you to a crisp. GAME OVER ")
      exit()
    elif dragon_awakens == "Left":
      well_done = print("Well done you've escaped. ")
      print(well_done)
    


elif left_right == "Left":
  print("You make you way up a path that leads to the cave.")
  attack_sneak = input("You see a Dragon in the cave sleeping. Do you Sneak past or Attack it? ")
  if attack_sneak == "Attack":
    health -= damage
    print(f"You try to attack but you take {damage} damage and now have a total of {health} Health ")
  elif attack_sneak == "Sneak":
    print("You sucessfully sneak past the dragon")
     