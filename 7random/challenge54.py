import random

user_choice = input("Enter your choice Heads: (h) or Tails: (t)? : ")

coin_toss = random.choice(["h","t"])

if coin_toss == user_choice:
    print("You win")
else:
    print("You Loose Buddy!")
