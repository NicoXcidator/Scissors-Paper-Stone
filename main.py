import random as rand

player_score = 0
com_score = 0

for i in range(10):
  print(f"Round number {i + 1}")
  player_w = input("Choose your weapon (i - Scissors, 2 - Paper, 3 - Stone): ")
  while player_w.isnumeric() == False:
    player_w = input("Choose your weapon (i - Scissors, 2 - Paper, 3 - Stone): ")
  player_w = int (player_w)
  com_w = rand.randint(1,3)

  print(f"Player has selected {player_w} and  Computer has selected {com_w}.")

  if player_w == com_w:
    print("It's a tie!")
  elif (player_w == 1 and com_w == 2) or (player_w == 2 and com_w == 3) and (player_w == 3 and com_w == 1):
    print("Player wins the round!")
    player_score += 1
  else:
    print("Computer wins the round!")
    com_score += 1  
  print(f"Player score: {player_score} ; Computer score: {com_w}")

if player_score == com_score:
  print("The game end with a tie!")
elif player_score > com_score:
  print("Player win!!!")
else:
  print("Computer win!!!")
