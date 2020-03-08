import string

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

players = {"X": "Player 1 (X)", "O": "Player 2 (O)"}

def display_board():
    '''
    Input: none
    
    Prints a formatted string, e.g.
      A   B   C
    -------------
    | X | X | X |  1
    -------------
    | O | O | X |  2
    -------------
    | X |   | O |  3
    -------------
    
    Returns nothing
    '''
    print("\n  A   B   C")
    for i, row in enumerate(board):
        print("-------------")
        print("|", end="") # no newline
        for item in row:
            print(f" {item} |", end="")
        print(f"  {i+1}")
    print("-------------")

def is_game_over(board):
    '''
    Input: board (list of lists)

    Returns True if
        - At least one row contains 3 identical, non-empty* items
        - At least one column contains 3 identical, non-empty* items
        - At least one diagonal contains 3 identical, non-empty* items
        - Board is full but there are no 3-in-a-row markers
    * Empty squares contain the string " "
    
    Returns False otherwise
    '''
    # column contains 3 identical, non-empty items
    # board[0][0/1/2] == board[1][0/1/2] == board[2][0/1/2]
    for j in range(3): # column index
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != " ":
            return True

    # row contains 3 identical, non-empty items
    # row[0] == row[1] == row[2]
    for i, row in enumerate(board):    
        if all(square == row[0] for square in row) and row[0] != " ":
            return True

    # diagonal contains 3 identical, non-empty items
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] != " ":
            return True

    # tie: board is full but no 3-in-a-row
    all_squares = [square for row in board for square in row]
    if all(square != " " for square in all_squares):
        return True

    return False

def check_input(raw_input):
    '''
    Removes unallowed characters, capitalizes letters, and zero-indexes numbers

    Input: raw string input from user
    Output: if input is sanitized or able to be sanitized,
        returns a 2-character string where the 1st char is A, B, or C
        and 2nd char is 1, 2, or 3
    '''
    processed_input = raw_input.upper()

    allowed_letters = ["A", "B", "C"]
    allowed_numbers = ["1", "2", "3"]

    if len(processed_input) != 2:
        return False
    
    if processed_input[0] not in allowed_letters or processed_input[1] not in allowed_numbers:
        return False

    # if square is empty
    row = allowed_numbers.index(processed_input[1])
    col = allowed_letters.index(processed_input[0])
    if board[row][col] == " ":
        return processed_input

    return False

def get_result_message(board):
    '''
    Input: board (list of lists)
    Returns a message indicating either the winning player or a tie
    '''
    # column contains 3 identical, non-empty items
    # board[0][0/1/2] == board[1][0/1/2] == board[2][0/1/2]
    for j in range(3): # column index
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != " ":
            return f"{players[board[0][j]]} won :0"

    # row contains 3 identical, non-empty items
    # row[0] == row[1] == row[2]
    for i, row in enumerate(board):    
        if all(square == row[0] for square in row) and row[0] != " ":
            return f"{players[row[0]]} won :0"

    # diagonal contains 3 identical, non-empty items
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] != " ":
            return f"{players[board[1][1]]} won :0"

    # tie: board is full but no 3-in-a-row
    return "There was a tie :0"

current_player = "X"

while not is_game_over(board):
    print(f"Your turn, {players[current_player]}.")

    user_input = input("Enter your move by selecting a square (e.g. B2): ")
    valid_move = check_input(user_input)

    while not valid_move:
        print("Invalid move :(\n")
        print(f"Still your turn, {players[current_player]}.")
        user_input = input("Enter your move by selecting a square (e.g. B2): ")
        valid_move = check_input(user_input)

    # place X/O on selected square
    letter_to_number = {"A": 0, "B": 1, "C": 2}
    letter = valid_move[0]
    number = valid_move[1]
    board[int(number) - 1][letter_to_number[letter]] = current_player

    display_board()
    print("\n")

    # switch player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print("Game over!")
print(get_result_message(board))
display_board()