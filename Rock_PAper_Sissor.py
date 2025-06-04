import random

emojie = {'r': '🪨', 's': '✂️', 'p': '📃'}  # Moved outside the loop (no need to redefine every time)
#using tuple cause immutable
choices = ('r', 'p', 's')  # Also moved outside the loop

while True:
    user_choice = input("rock, paper or scissor (r,p,s): ").lower()
    
    if user_choice not in choices:
        print("Invalid choice!")
        continue
        
    computer_choice = random.choice(choices)
    
    print(f'You chose: {emojie[user_choice]}')
    print(f'Computer chose: {emojie[computer_choice]}')
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'r' and computer_choice == 'p') or \
         (user_choice == 'p' and computer_choice == 's') or \
         (user_choice == 's' and computer_choice == 'r'):
        print("Computer wins!!")
    else:
        print("You win!!") 
        
    check = input("Do you want to continue? (y/n): ").lower()
    if check == 'n':
        break