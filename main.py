import copy
from board import Board
from minimax import findBestMove



def main():
    currentBoard = Board()
    
    run = True
    turn = 1
    depthLimit = input("Enter the depth limit (suggested: 4 or 5): ")
    while run:
        takeTurn(turn, currentBoard, int(depthLimit))

       
        print("\n")
        winner = currentBoard.check_win()

        if winner != " " and winner != "T":
            currentBoard.print_board()
            print("The winner is " + winner)
            
            run = False
        elif winner == "T":
            currentBoard.print_board()
            print("Tie Game")
            
            run = False

        turn = (turn + 1) % 2

def takeTurn(turn, currentBoard, depthLimit):
    if turn == 0:
        print("Player 2's turn")
        #Deep copy the board
        currentBoardCopy = copy.deepcopy(currentBoard)
        bestMove = findBestMove(currentBoard.get_board(), currentBoardCopy, depthLimit)
        
        #row = bestMove[0]
        col = bestMove
    else:
        print("Player 1's turn")
        currentBoard.print_board()
        col = input("Enter the column number (e.x 1): ")
    
        col = int(col) - 1
        if(col < 0 or col > 6):
            print("Invalid column, try again")
            takeTurn(turn, currentBoard, depthLimit)
            return

    
    
    if currentBoard.place_piece(col, "R" if turn == 0 else "B"):
        print("Piece placed")
        currentBoard.print_board()
    else:
        print("Column is full, try again")
        takeTurn(turn, currentBoard, depthLimit)
    


main()