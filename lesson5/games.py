import random
def fun_game(die_sides):
  """This is a game to roll a die 5 times"""
  die_rolls=[random.randint(1,die_sides) for die in range(5)]
  return(die_rolls)

def number_game():
  """THis is a guessing game"""
  secret=random.randint(1,10)
  guess=int(input("guess a number"))
  if guess==secret:
    return("Great")
  else:
    return("wrong - the number was ",secret)
