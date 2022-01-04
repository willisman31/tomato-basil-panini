from getpass import getpass

def game():
    print("Welcome to Hangman")
    print("For single player, press 1")
    player = input("For two player, press 2")
    if player.equals("2"):
        print("Player one, input your secret word: (with no spaces) ")
        secret = getpass()
    else:
        words = ["lobster", "tomato", "nth", "banana", "shoe", "monkey", "quotation", "rhythm", "matter", "senate", "letter", "program", "python"]
        secret = words.random()
    guesses = 0
    while guesses not 6 and guesses not -1:
        guesses = turn(secret, guesses)
    if guesses == 6:
        print("You have been unalived")
    elif guesses == -1:
        print("You have survived, but at what cost?")

def turn(secret, guesses):
    guess = input("Guess a letter: ")
    if guess in secret:
        print("Woot!  Good guess!")
        hang(guesses)

    else:
        guesses += 1
        hang(guesses)
        print("Only ")
    return guesses

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
      print(" | / \")
      print("_|_____")
      print("Oof")
