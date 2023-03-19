import time
import random

print(" ----- Welcome To Hangman game ----- ")
print('')

print("Start guessing...")
print('')
time.sleep(1)

words = ["python", "javascript", "coding", "application", "server", "developer"]
secret_word = random.choice(words)

guesses = ''

turns = 10

while turns > 0:

  failed = 0

  for char in secret_word:
    if char in guesses:
      print(char, end=""),
    else:
      print("_", end=""),
      failed += 1

  if failed == 0:
    print('')
    print('')
    print(" --- Goodjob You WON ---")
    break
  guess = input(" guess a character: ")
  print('')

  guesses += guess

  if guess not in secret_word:
    turns -= 1
    print('')
    print(f'Wrong. You have {turns} more guesses!')
    print('')

    if turns == 0:
      print('')
      print("You Lose")