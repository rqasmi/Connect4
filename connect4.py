""" This program implements a simple connect4 game where 2 players take turns alternatively to place their respective pieces on a 7*7 board.

The program prompts each player on the console to enter the column where they want to place their repective piece (either red or black).
For simplicity, the black piece is drawn as 'X' and the red piece as 'O'. The player cannot choose the row as stated by the game rules.
The program then prints the current board and checks if the current player had won the game. A player wins when he has 4 consecutive 
pieces of his own placed either horizontally, vertically or diagonally. The program also implements error checks and game tie.
"""

"""These are global and constant variables needed to play the game"""
current_board = [['  ','  ','  ','  ', '  ', '  '], ['  ','  ','  ','  ', '  ', '  '], ['  ','  ','  ','  ', '  ', '  '],
                ['  ','  ','  ','  ', '  ', '  '], ['  ','  ','  ','  ', '  ', '  '], ['  ','  ','  ','  ', '  ', '  '],
                ['  ','  ','  ','  ', '  ', '  ']]
board_rows, board_columns, actual_rows, actual_columns = 11, 13, 6, 7
consecutive_count_to_win = 4
black = ' X'
red = ' O'
player_piece_dict = {
  "1": black,
  "2": red
}

def drawBoard(board):
  """Draws the input board on the console (The input is a 2D array)."""
  for row in range(board_rows):
    if row % 2 == 0:
      row_pattern = ""
      for column in range(board_columns):       
        if column % 2 == 0:
          row_pattern += current_board[int(column / 2)][int(row / 2)]
        else:
          row_pattern += "|"
      print(row_pattern)
    else:
      print("-" * (board_columns+actual_columns))


def playGame():
  """Implements the logic of the game."""
  curr_player = "1"
  occupied_columns = 0  
  while(True):
    print("Current player turn: ", curr_player)
    try:
      column = int(input("Select a column between 0 and 6:\n>"))
      if column < 0 or column >= actual_columns:
        raise IndexError("Column index not in range of board.")
    except ValueError:
      print("Column index must be an integer")
      continue
    except IndexError as e:
      print(str(e))
      continue
    
    is_set = False
    for curr_row in range (actual_rows-1, -1, -1):    
      if current_board[column][curr_row] == '  ':
        current_board[column][curr_row] = player_piece_dict[curr_player]
        is_set = True
        drawBoard(current_board)
        if isGameWon(column, curr_row, curr_player):
          print(f"Player {curr_player} won the game!!")
          return
        curr_player = switchPlayer(curr_player)
        break

    if curr_row == 0 and is_set:
      occupied_columns += 1
      if occupied_columns == actual_columns:
        print("Game ended with no winner!")
        return

    if not is_set:
      print("Column", column, "is entirely occupied. Select another column.")


def switchPlayer(player):
  """Switch and return player turn."""
  if player == "1": 
    player = "2"
  else:
    player = "1"
  return player


def isGameWon(col, row, player):
  """Returns a boolean indicating whether the game has been won by the current player."""
  return (checkRowCountForWin(col, row, player) or checkColumnCountForWin(col, row, player) or
          checkFirstDiagonalCountForWin(col, row, player) or checkSecondDiagonalCountForWin(col, row, player))


def checkRowCountForWin(col, row, player):
  """Returns a boolean indicating whether the current row count for the player's pieces has fulfilled the count for the win."""
  count = 1
  for curr_row in range(row + 1, actual_rows):
    if current_board[col][curr_row] == player_piece_dict[player]:
      count += 1
      if count == consecutive_count_to_win:
        return True
    else:
      return False


def checkColumnCountForWin(col, row, player):
  """Returns a boolean indicating whether the current column count for the player's pieces has fulfilled the count for the win."""
  count = 0
  i, j = col, col +1
  while i >= 0:
    if current_board[i][row] == player_piece_dict[player]:
      count += 1
    else:
      i = 0
    i -= 1
  while j < actual_columns:
    if current_board[j][row] == player_piece_dict[player]:
      count += 1
    else:
      j = actual_columns
    j += 1
  
  if count >= consecutive_count_to_win:
    return True
  return False


def checkFirstDiagonalCountForWin(col, row, player):
  """Returns a boolean indicating whether the current right diagonal count for the player's pieces has fulfilled the count for the win."""
  count, secondDiagonalCount = 0, 0
  i, j, k, l = col, col +1, row, row +1
  while i >= 0 and k >= 0:
    if current_board[i][k] == player_piece_dict[player]:
      count += 1
    else:
      i = 0
    i -= 1
    k -= 1

  while j < actual_columns and l < actual_rows:
    if current_board[j][l] == player_piece_dict[player]:
      count += 1
    else:
      j = actual_columns
    j += 1
    l += 1
  
  if count >= consecutive_count_to_win:
    return True
  return False


def checkSecondDiagonalCountForWin(col, row, player):
  """Returns a boolean indicating whether the current left diagonal count for the player's pieces has fulfilled the count for win."""
  count = 0
  i, j, k, l = col, col +1, row, row -1
  while i >= 0 and k < actual_rows:
    if current_board[i][k] == player_piece_dict[player]:
      count += 1
    else:
      i = 0
    i -= 1
    k += 1
  while j < actual_columns and l >= 0:
    if current_board[j][l] == player_piece_dict[player]:
      count += 1
    else:
      j = actual_columns
    j += 1
    l -= 1
  
  if count >= consecutive_count_to_win:
    return True
  return False


drawBoard(current_board)
playGame()
