import random

def coinFlip():
  coin = random.randint(1,2)
  if coin == 1:
    print("Heads")
  if coin == 2:
    print("Tails")

coinFlip()
