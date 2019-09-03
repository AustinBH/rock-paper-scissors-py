from random import choice

player_wins = 0
computer_wins = 0
# Playing first to 5
winning_score = 5
while player_wins < winning_score and computer_wins < winning_score:
    # Adding initial score tracker and rps countdown
    print(f'Player Score: {player_wins} Computer Score: {computer_wins}')
    print('...rock...')
    print('...paper...')
    print('...scissors...')
    player = input('Enter your choice: \n').lower()
    # Here we are allowing a user to quit using q or quit whenever they want
    if player == 'quit' or player == 'q':
        break
    # This is where we use the choice function to generate a random choice
    computer = choice(['rock', 'paper', 'scissors'])
    print(f'The computer plays: {computer}')
    # This is the logic determining who wins a round
    if player == computer:
        print("It's a tie!")
    elif player == 'rock':
        if computer == 'paper':
            computer_wins += 1
            print('Computer wins!')
        elif computer == 'scissors':
            print('You win!')
            player_wins += 1
    elif player == 'paper':
        if computer == 'scissors':
            print('Computer wins!')
            computer_wins += 1
        elif computer == 'rock':
            print('You win!')
            player_wins += 1
    elif player == 'scissors':
        if computer == 'rock':
            print('Computer wins!')
            computer_wins += 1
        elif computer == 'paper':
            print('You win!')
            player_wins += 1
    else:
        print('Please enter a valid choice')
# Our final if statement here determines who won the entire game
if player_wins > computer_wins:
    print('Congrats, you won!')
# This elif is used to display a correct statment if the user leaves early
elif player_wins == computer_wins:
    print("It's a tie")
else:
    print('Oh no ;( the computer won...')
