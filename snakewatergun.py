#Snake water gun
import random
print("rock for 1, paper for 2,scissors for 3")

def get_user_choice():
  user_choice=input("enter your choice( 1, 2 , 3 )")
  return user_choice

def get_computer_choice():
  return random.choice([' 1',' 2', ' 3 '])

def determine_winner(user_choice,computer_choice):
  if(user_choice==computer_choice):
   return "draw"
  elif(user_choice==1 and computer_choice==3) or \
     (user_choice==2 and computer_choice==1) or\
     (user_choice==3 and computer_choice==2):
    return "you win"
  else:
    return "computer win"

def play_game():
  print("welcome to game")
  while True:
    user_choice=get_user_choice()
    computer_choice=get_computer_choice()
    print(f"\n You chose:{user_choice}")
    print(f"computer chose:{computer_choice}")
    print(determine_winner(user_choice,computer_choice))
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()
    
  