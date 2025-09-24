import random

while True:
    user = input("Enter (r) for Rock, (s) for Scissor and (p) for Paper: ")
    computer = random.choice(['r', 's', 'p'])

    user_lower= user.lower()
    print(f"Computer selected: {computer.upper()}")

    if user_lower in ['r', 's', 'p']:
        if user_lower == computer:
            print("Draw")
        elif user_lower == "p" and computer == 'r':
            print("User Wins")
        elif user_lower == "r" and computer == 'p':
            print("Computer Wins")
        elif user_lower == "s" and computer == 'r':
            print("computer Wins")
        elif user_lower == "r" and computer == 's':
            print("User Wins")
        elif user_lower == "p" and computer == 's':
            print("Computer Wins")
        elif user_lower == "s" and computer == "p":
            print("User Wins")
        else:
            print('Invalid')
    query = input('Would you like to continue [(Y)es/(N)o]: ')

    if 'y' in query.lower():
        continue
    else:
        print("Starting next round")
        break
