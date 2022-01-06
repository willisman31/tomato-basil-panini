from getpass import getpass
import random

# Main gameplay
def game():
    print("Welcome to Hangman")
    print("For single player, press 1")
    player = input("For two player, press 2\n")
    if player == '2' or player.casefold() == 'two':
        print("Player one, input your secret word: (with no spaces) ")
        secret = getpass()
    else:
        words = ['lobster', 'tomato', 'nth', 'banana', 'shoe', 'monkey', 'quotation', 'rhythm', 'matter', 'senate', 'letter', 'program', 'python', 'words', 'super', 'pineapple', 'lynx', 'mint', 'cinnamon']
        secret = random.choice(words)
    standing_guess = ""
    for i in secret:
        standing_guess += "_ "
    print(standing_guess)
    guesses = 0
    letters = {}
    while not guesses == -1 and not guesses == 6:
        try:
            guess = input("Guess a letter: ")[0]
        except IndexError:
            print("Input required")
            continue 
        if (secret.casefold().count(guess) > 0):
            print("Good guess!")
            hang(guesses)
            start = 0
            while True:
                try:
                    start = secret.casefold().index(guess, start,)
                    standing_guess = standing_guess[:2 * start] + guess + " " + standing_guess[(2 * start) + 2:]
                    start += 1
                except ValueError:
                    break
            if standing_guess.count("_") == 0:
                if guesses == 0:
                    print("Good job!")
                else:
                    print("You've survived, but at what cost?")
                guesses = -1
        else:
            print("No")
            guesses += 1
            hang(guesses)
            letters[guess] : False
            print(letters)
            if guesses == 6:
                print("You have been unalived")
        print(standing_guess)
    print("Game Over")

# For Displaying Hangman Progress
def hang(var):
  if var == 0:
      print("  __ ")
      print(" |  | ")
      print(" |")
      print(" |")
      print(" |")
      print("_|_____")
  elif var == 1:
      print("  __ ")
      print(" |  | ")
      print(" |  o")
      print(" |")
      print(" |")
      print("_|_____")
  elif var == 2:
      print("  __ ")
      print(" |  | ")
      print(" |  o")
      print(" |  |")
      print(" |")
      print("_|_____")
  elif var == 3:
      print("  __ ")
      print(" |  | ")
      print(" |  o")
      print(" | -|")
      print(" |")
      print("_|_____")
  elif var == 4:
      print("  __ ")
      print(" |  | ")
      print(" |  o")
      print(" | -|-")
      print(" |")
      print("_|_____")
  elif var == 5:
      print("  __ ")
      print(" |  | ")
      print(" |  o")
      print(" | -|-")
      print(" | /")
      print("_|_____")
  else:
      print("  __ ")
      print(" |  | ")
      print(" |  o")
      print(" | -|-")
      print(" | / \\")
      print("_|_____")

game()
