from getpass import getpass
import random

letters = {}

def game():
    print("Welcome to Hangman")
    print("For single player, press 1")
    player = input("For two player, press 2\n")
    if player == 2:
        print("Player one, input your secret word: (with no spaces) ")
        secret = getpass()
    else:
        words = ['lobster', 'tomato', 'nth', 'banana', 'shoe', 'monkey', 'quotation', 'rhythm', 'matter', 'senate', 'letter', 'program', 'python']
        secret = random.choice(words)
    word = ""
    for i in secret:
        word += "_ "
    print(word)
    guesses = 0
    while not guesses == 6 and not guesses == -1:
        guesses = turn(secret, guesses, word)
    if guesses == 6:
        print("You have been unalived")
    elif guesses == -1:
        print("You have survived, but at what cost?")

def turn(secret, guesses, word):
    guess = input("Guess a letter: ")
    if guess in secret:
        print("Woot!  Good guess!")
        hang(guesses)
        letters[guess] = True
        find_replace(guess, secret, word, 0)
    else:
        guesses += 1
        hang(guesses)
        letters[guess] = False
        print(letters)
    return guesses

def find_replace(guess, secret, guessed, start):
    while not secret.index(guess, start,) == ValueError:
        start = secret.index(guess, start,)
        guessed = guessed[:start] + guess + guessed[start + 1:]
        start += 1
    return guessed

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
      print("Oof")

game()
