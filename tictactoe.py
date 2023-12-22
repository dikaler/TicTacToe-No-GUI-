import os

play = True

# Draw the board
def draw_board(spots):
  board = (f"     |   |\n"
           f"   {spots[1]} | {spots[2]} | {spots[3]} \n"
           f"---------------\n"
           f"   {spots[4]} | {spots[5]} | {spots[6]} \n"
           f"---------------\n"
           f"   {spots[7]} | {spots[8]} | {spots[9]} \n"
           f"     |   |\n")
  print(board)


# Alternate spot place holder
def check_turn(turn):
  if turn % 2 == 0: return 'O'
  else: 
    return 'X'

def check_for_win(dict):
  # Check Horizontal Win Cases
  if   (spots[1] == spots[2] == spots[3]) \
    or (spots[4] == spots[5] == spots[6]) \
    or (spots[7] == spots[8] == spots[9]):
    return True
  # Check Vertical Win Cases
  elif   (spots[1] == spots[4] == spots[7]) \
    or (spots[2] == spots[5] == spots[8]) \
    or (spots[3] == spots[6] == spots[9]):
    return True
  # Check Diagonal Win Cases
  elif (spots[1] == spots[5] == spots[9]) \
    or (spots[3] == spots[5] == spots[7]):
    return True
  
  # No one won
  else: 
    return False

# Set all spots on the board
spots = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}
playing, complete = True, False
turn = 0
prev_turn = -1

# Game Loop
while playing:
    
    # Draw the current Game Board
    draw_board(spots)

    # If player tries to select already selected spot
    if prev_turn == turn:
      print("Invalid spot selected, please pick another.")
    prev_turn = turn
    print("Player " + str((turn % 2) +1 ) + "'s turn: Pick your spot or press q to quit")
    
    # Get input and make sure it's valid
    choice = input()

    # The game has quit 
    if choice == 'q':
        playing = False

    elif str.isdigit(choice) and int(choice) in spots:
      # Check if the spot is already selected
      if not spots[int(choice)] in {"X", "O"}:
        # If not, update board and increment the turn
        turn += 1
        spots[int(choice)] = check_turn(turn)
      
    # Check if the game has ended
    # If game ended, also check if someone won or ended in a draw
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing = False
    
draw_board(spots)
# If there was a winner, say who won
if complete:
  if check_turn(turn) == 'X': print("Player 1 Wins!")
  else: print("Player 2 Wins!")

else: 
  # Tie Game
  print("No Winner")
  
print("Thanks for playing!") 
