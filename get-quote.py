import random

def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes)

  last = 13
  last = len(quotes) - 1
  rnd = random.randint(0, last)

  print(quotes[rnd])

if __name__== "__main__":
  primary()
