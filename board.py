class Board:
    def __init__(self):
        self.board = [  [" "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "] 
                    ]
    def print_board(self):
        rowId = 0
        columnId = "1   2   3   4   5   6   7"
        print(columnId)
        for row in self.board:
            line = ""
            

            
            for column in row:
                line += column + " | "
            # Remove the last 3 characters from the line
            line = line[:-3]
            rowId += 1
            print(line)

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board

    def get_column(self, column):
        return [row[column] for row in self.board]

    def get_row(self, row):
        return self.board[row]

    def place_piece(self, column, piece):
        for row in range(len(self.board)-1, -1, -1):
            if self.board[row][column] == " ":
                self.board[row][column] = piece
                return True
        return False

    def remove_piece(self, column):
        for row in range(len(self.board)):
            if self.board[row][column] != " ":
                self.board[row][column] = " "
                return True
        return False

    def check_win(self):
        # Check for horizontal wins
        for row in self.board:
            for column in range(len(row)-3):
                if row[column] == row[column+1] == row[column+2] == row[column+3] != " ":
                    return row[column]

        # Check for vertical wins
        for column in range(len(self.board[0])):
            for row in range(len(self.board)-3):
                if self.board[row][column] == self.board[row+1][column] == self.board[row+2][column] == self.board[row+3][column] != " ":
                    return self.board[row][column]

        # Check for diagonal wins
        for column in range(len(self.board[0])-3):
            for row in range(len(self.board)-3):
                if self.board[row][column] == self.board[row+1][column+1] == self.board[row+2][column+2] == self.board[row+3][column+3] != " ":
                    return self.board[row][column]

        for column in range(len(self.board[0])-3):
            for row in range(3, len(self.board)):
                if self.board[row][column] == self.board[row-1][column+1] == self.board[row-2][column+2] == self.board[row-3][column+3] != " ":
                    return self.board[row][column]

        #Check for Tie
        for row in self.board:
            for column in range(len(row)-1):
                if row[column] == " ":
                    return " "
        return "T"
    
    def try_place_piece(cBoard, column, piece, board):
        for row in range(len(board)-1, -1, -1):
            if board[row][column] == " ":
                return (True, row, column)
        return (False, -1, -1)

    def check_if_useless_move(self, column, piece, board):
        #Get the row that the piece would be placed in
        able, row, col = self.try_place_piece(column, piece, board)
        if not able:
            return True
        #Check if the piece would be useless, if move is useless, and wont cause a win, return true
        board[row][col] = piece
        if self.check_win() == piece:
            board[row][col] = " "
            return False
        #Check if the piece stops the opponent from winning
        board[row][col] = "R" if piece == "B" else "B"
        if self.check_win() == "R" if piece == "B" else "B":
            board[row][col] = " "
            return False
        
        #Check if there is enough empty space vertically or enough of the same piece vertically to make the move useful
        board[row][col] = piece
        #Check if there is enough empty space vertically to the left of the piece by 4 and to the right of the piece by 4
        freeSpaceV = 0
        for i in range(1, 5):
            if col - i < 0:
                break
            if board[row][col-i] == " ":
                freeSpaceV += 1
            else:
                break
        for i in range(1, 5):
            if col + i > 6:
                break
            if board[row][col+i] == " ":
                freeSpaceV += 1
            else:
                break
        if freeSpaceV < 4:
            board[row][col] = " "
            return False
        
        #Check if there is enough of the same piece vertically to the left of the piece by 4 and to the right of the piece by 4
        samePieceV = 0
        for i in range(1, 5):
            if col - i < 0:
                break
            if board[row][col-i] == piece:
                samePieceV += 1
            else:
                break
        for i in range(1, 5):
            if col + i > 6:
                break
            if board[row][col+i] == piece:
                samePieceV += 1
            else:
                break
        if samePieceV < 4:
            board[row][col] = " "
            return False
        
         #Check if there is enough empty space horizontally to the up of the piece by 4 and to the down of the piece by 4
        freeSpaceH = 0
        for i in range(1, 5):
            if row - i < 0:
                break
            if board[row-i][col] == " ":
                freeSpaceH += 1
            else:
                break
        for i in range(1, 5):
            if row + i > 5:
                break
            if board[row+i][col] == " ":
                freeSpaceH += 1
            else:
                break
        if freeSpaceH < 4:
            board[row][col] = " "
            return False
        
        #Check if there is enough of the same piece horizontally to the up of the piece by 4 and to the down of the piece by 4
        samePieceH = 0
        for i in range(1, 5):
            if row - i < 0:
                break
            if board[row-i][col] == piece:
                samePieceH += 1
            else:
                break
        for i in range(1, 5):
            if row + i > 5:
                break
            if board[row+i][col] == piece:
                samePieceH += 1
            else:
                break
        if samePieceH < 4:
            board[row][col] = " "
            return False
        
        #Check if there is enough empty space diagonally to the up left of the piece by 4 and to the down right of the piece by 4
        freeSpaceDL = 0
        for i in range(1, 5):
            if row - i < 0 or col - i < 0:
                break
            if board[row-i][col-i] == " ":
                freeSpaceDL += 1
            else:
                break
        for i in range(1, 5):
            if row + i > 5 or col + i > 6:
                break
            if board[row+i][col+i] == " ":
                freeSpaceDL += 1
            else:
                break
        if freeSpaceDL < 4:
            board[row][col] = " "
            return False
        
        #Check if there is enough of the same piece diagonally to the up left of the piece by 4 and to the down right of the piece by 4
        samePieceDL = 0
        for i in range(1, 5):
            if row - i < 0 or col - i < 0:
                break
            if board[row-i][col-i] == piece:
                samePieceDL += 1
            else:
                break
        for i in range(1, 5):
            if row + i > 5 or col + i > 6:
                break
            if board[row+i][col+i] == piece:
                samePieceDL += 1
            else:
                break
        if samePieceDL < 4:
            board[row][col] = " "
            return False
        
        #Check if there is enough empty space diagonally to the up right of the piece by 4 and to the down left of the piece by 4
        freeSpaceDR = 0
        for i in range(1, 5):
            if row - i < 0 or col + i > 6:
                break
            if board[row-i][col+i] == " ":
                freeSpaceDR += 1
            else:
                break
        for i in range(1, 5):
            if row + i > 5 or col - i < 0:
                break
            if board[row+i][col-i] == " ":
                freeSpaceDR += 1
            else:
                break
        if freeSpaceDR < 4:
            board[row][col] = " "
            return False
        
        #Check if there is enough of the same piece diagonally to the up right of the piece by 4 and to the down left of the piece by 4
        samePieceDR = 0
        for i in range(1, 5):
            if row - i < 0 or col + i > 6:
                break
            if board[row-i][col+i] == piece:
                samePieceDR += 1
            else:
                break
        for i in range(1, 5):
            if row + i > 5 or col - i < 0:
                break
            if board[row+i][col-i] == piece:
                samePieceDR += 1
            else:
                break
        if samePieceDR < 4:
            board[row][col] = " "
            return False
        
        board[row][col] = " "
        return True


        

        
        

        
           
        
    