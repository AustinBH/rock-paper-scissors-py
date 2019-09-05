from random import choice
# Similar setup to v1, we still want to keep track of wins
# Now with functions
player_wins = 0
computer_wins = 0
# Here we are starting the game
playing = True
# Adding initial welcome and quit information
def welcome_message():
    print('Welcome to Rock, Paper, Scissors')
    print('Type q or quit to exit')
# Adding game start print message
def start_game():
    print('...rock...')
    print('...paper...')
    print('...scissors...')
# Saving choices for computer and player
def get_choices():
    global player
    global computer
    global playing
    player = input('Enter your choice: \n').lower()
    # This is where we use the choice function to generate a random choice
    computer = choice(['rock', 'paper', 'scissors'])
    print(f'The computer plays: {computer}')
    if player == 'quit' or player == 'q':
        # Rather than breaking we are now toggling playing
        playing = False
# This is the logic determining who wins a round
def play_round():
    global computer_wins
    global player_wins
    if player == computer:
        print("It's a tie!")
    elif player == 'rock':
        if computer == 'paper':
            computer_wins += 1
            print('Computer wins!')
        elif computer == 'scissors':
            player_wins += 1
            print('You win!')
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

def end_game():
    print(f'Player Score: {player_wins} Computer Score: {computer_wins}')
    # Our final if statement here determines who won the entire game
    if player_wins > computer_wins:
        print('Congrats, you won!')
    # This elif is used to display a correct statment if the user leaves early
    elif player_wins == computer_wins:
        print("It's a tie")
    else:
        print('Oh no ;( the computer won...')

welcome_message()
while playing:
    start_game()
    get_choices()
    play_round()
end_game()

