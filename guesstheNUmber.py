import random

target=random.randint(1,100)

while True:
  userChoice=int(input("guess the target or quit:"))
  if(userChoice=="Quit"):
    break
  
  userChoice=int(userChoice)
  if(userChoice==target):
    print("success:Correct Guess!!")
    break
  if(userChoice<target):
    print("your number is too small.Take a bigger guess..")
  else:
    print("your number was too big.Take a smaller guess..")

print("---GAME OVER-----")   