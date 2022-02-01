
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


health = 2
damage = 1

left_right = input("You see a cave in the distance. You don't know how to get up there, so you must choose. Left or Right ? ")
if left_right == "Right":
  health - damage 
  print(f"You Trip and lose {damage} Health. You now have a total of {health} Health  ")

