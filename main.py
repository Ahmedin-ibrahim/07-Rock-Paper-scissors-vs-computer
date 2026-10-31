player_score = 0
computer_score = 0

def get_player_choice():
    """
    Asks the player for their move.
    Translates 'r', 'p', 's' or full words into 'rock', 'paper', 'scissors'.
    """
    while True:
        choice = input("\nEnter your choice (rock/r, paper/p, scissors/s): ").lower().strip()

        if choice == 'r' or choice == 'rock':
            return 'rock'
        elif choice == 'p' or choice == 'paper':
            return 'paper'
        elif choice == 's' or choice == 'scissors':
            return 'scissors'
        else:
            print("Invalid choice! Please choose rock, paper, or scissors.")

def get_computer_choice():
    """
    Randomly select rock, paper, or scissors for the computer.
    Returns the computer's choice as a string.
    """
    import random
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def who_wins(player_choice, computer_choice):
    """
    Determine the winner of the game based on player and computer choices.
    Returns 'player', 'computer', or 'tie' based on the outcome.
    """
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'player'
    else:
        return 'computer'

while player_score < 3 and computer_score < 3:
    # 1. Call your functions from Steps 1 & 2
    player = get_player_choice()
    computer = get_computer_choice()

    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")

    # 2. Check who won the round using your Step 3 function
    winner = who_wins(player, computer)

    # 3. Update the score based on the winner
    if winner == 'player':
        player_score += 1
    elif winner == 'computer':
        computer_score += 1

print(f"\nFinal Score - You: {player_score}, Computer: {computer_score}")