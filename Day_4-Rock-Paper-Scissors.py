import random
print("Beat me if you can in Rock, Paper, Scissors!")
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

user_choice = int(input('''What do you choose? 
Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'''))

if user_choice > 2 or user_choice < 0:
    print("You typed an invalid number! You lose !")

else: 
    if user_choice == 0:
        print(rock)
    if user_choice == 1:
        print(paper)
    if user_choice == 2:
        print(scissors)



    computer_choice = random.randint(0,2)
    print(f"Computer chose {computer_choice}")

    if computer_choice == 0:
        print(rock)
    if computer_choice == 1:
        print(paper)
    if computer_choice == 2:
        print(scissors)


    if user_choice == 0:
        if computer_choice == 0:
            print("You just smashed rocks together. It's a draw !")
        elif computer_choice == 1:
            print("Paper blocked your rock. You lose !")
        elif computer_choice == 2:
            print("Rocks broke hell on my scissors. You win !")
        
    elif user_choice == 1:
        if computer_choice == 1:
            print("It's a draw!")
        elif computer_choice == 0:
            print("Aah! You blocked my rock. You win!")
        elif computer_choice == 2:
            print("Haha! I shredded your paper. You lose !")
    elif user_choice == 2:
        if computer_choice == 0:
            print("Haha! I destroyed your scissors. You lose!")
        elif computer_choice == 1:
            print("Oops! You shredded my paper. You win!")
        elif computer_choice == 2:
            print("It's a draw!")
    else:
        none

