rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
print("\n\n     \x1B[1;4m\x1B[3mROCK PAPER SCISSORS` GAME\x1B[0m")
def comp():
    print("Computer's choice: ")
    if computer_input == 0:
        print("Rock\n")
        return rock
    elif computer_input == 1:
        print("Paper\n")
        return paper
    elif computer_input == 2:
        print("Scissors\n")
        return scissors

def user():
    print("You choice: ")
    if user_input == 0:
        print("Rock\n")
        return rock
    elif user_input == 1:
        print("Paper\n")
        return paper
    elif user_input == 2:
        print("Scissors\n")
        return scissors

def compare():
    if computer_input == user_input:
        print("Draw!")
    elif (computer_input == 0 and user_input == 2) or (computer_input == 2 and user_input == 1) or (computer_input== 1 and user_input==  0):
        print("Opps, You lose!")
    else:
        print("You win!")

game_continue = True

while game_continue:
    print("\n\n")
    user_input = int(input("Type '0' for Rock, '1' for Paper, '2' for scissors: "))
    print("\n")
    print(user())

    computer_input= random.randint(0,2)
    print("\n")
    print(comp())

    compare()

    play_again = input("Do you want to play again? Type 'Y' for yes or 'N' for no\n").upper()
    if play_again == 'N':
        game_continue = False
    else:
        continue

