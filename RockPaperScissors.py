import random

while True:
  print('')
  print('     ----- Welcome To Rock Paper Scissors Game -----')
  print('')
  user_action = input("Enter a choice (rock, paper, scissors): ")
  game_choices = ["rock", "paper", "scissors"]
  AI_action = random.choice(game_choices)
  print(f"\nYou chose {user_action}, computer chose {AI_action}.\n")

  if user_action == AI_action:
    print(f"Both players selected {user_action}. It's a tie!")
  elif user_action == "rock":
    if AI_action == "scissors":
      print("Rock smashes scissors! You win!")
      print('')
    else:
      print("Paper covers rock! You lose.")
      print('')
  elif user_action == "paper":
    if AI_action == "rock":
      print("Paper covers rock! You win!")
      print('')
    else:
      print("Scissors cuts paper! You lose.")
      print('')
  elif user_action == "scissors":
    if AI_action == "paper":
      print("Scissors cuts paper! You win!")
      print('')
    else:
      print("Rock smashes scissors! You lose.")

  print('')
  play_again = input("Play again? (y/n): ")
  if play_again.lower() != "y":
    print('Thank you for playing. Goodbye!')
    break