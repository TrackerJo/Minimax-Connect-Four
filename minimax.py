ai, player, empty = 'B', 'R', ' '

def areMovesLeft(board):
    for i in range(6):
        for j in range(7):
            
            if board[i][j] == empty:
                return True
    return False

def evaluate(board):
   
 # Check for horizontal wins
    for row in board:
        for column in range(len(row)-3):
            if row[column] == row[column+1] == row[column+2] == row[column+3] != " ":
                return 10 if row[column] == ai else -10

    # Check for vertical wins
    for column in range(len(board[0])):
        for row in range(len(board)-3):
            if board[row][column] == board[row+1][column] == board[row+2][column] == board[row+3][column] != " ":
                return 10 if board[row][column] == ai else -10

    # Check for diagonal wins
    for column in range(len(board[0])-3):
        for row in range(len(board)-3):
            if board[row][column] == board[row+1][column+1] == board[row+2][column+2] == board[row+3][column+3] != " ":
                return 10 if board[row][column] == ai else -10

    for column in range(len(board[0])-3):
        for row in range(3, len(board)):
            if board[row][column] == board[row-1][column+1] == board[row-2][column+2] == board[row-3][column+3] != " ":
                return 10 if board[row][column] == ai else -10
    
    
    return 0

#Only need to consider placing in one of the columns, then figuring where it would go, this is a 6x7 board
#Set a depth limit, and if it reaches that depth, evaluate the board
def minimax(board, depth, isMax, boardObj, depthLimit):
    
    score = evaluate(board)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not areMovesLeft(board):
        return 0
    
    if depth >= depthLimit:
        return score
    
    if isMax:
        best = -1000
        for i in range(7):
            able, row, col = boardObj.try_place_piece(i, ai, board)
            if able:
                
                board[row][col] = ai
                best = max(best, minimax(board, depth+1, not isMax, boardObj, depthLimit))
                board[row][col] = empty
                
        return best
    else:
        best = 1000
        for i in range(7):
            able, row, col = boardObj.try_place_piece(i, player, board)
            if able:
                board[row][col] = player
                best = min(best, minimax(board, depth+1, not isMax, boardObj, depthLimit))
                board[row][col] = empty
        return best
    
def findBestMove(board, boardObj, depthLimit):
    bestVal = -1000
    bestMove = -1
    print("Finding best move")
    for i in range(7):
        able, row, col = boardObj.try_place_piece(i, ai, board)
        if able:
            if not boardObj.check_if_useless_move(col, ai, board):
                board[row][col] = ai
                moveVal = minimax(board, 0, False, boardObj,depthLimit)
                board[row][col] = empty
                if moveVal > bestVal:
                    bestMove = i
                    bestVal = moveVal
    print("Found best move")
    return bestMove