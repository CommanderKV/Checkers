import pygame
from piece import Piece
from grid import Grid



def getVaildMoves(grid, gridObject):

    movesPossible = {}


    for rowPos, row in enumerate(grid):
        for colPos, piece in enumerate(row):
            moves = []
            killMoves = []
            if isinstance(piece, Piece) is True:
                i = 0
                while i == 0:
                    try:
                        # Right blank
                        if grid[rowPos+1][colPos+1] is None:
                            if piece.team == gridObject.piece1Turn or piece.king == True:
                                moves.append((rowPos+1, colPos+1))

                        # Right piece
                        elif isinstance(grid[rowPos+1][colPos+1], Piece) is True:
                            if piece.team == gridObject.piece1Turn or piece.king == True:
                                if grid[rowPos+1][colPos+1].team != piece.team:
                                    if grid[rowPos+2][colPos+2] is None:
                                        killMoves.append((rowPos+2, colPos+2))

                    except:
                        pass


                    try:
                        # Left None
                        if grid[rowPos+1][colPos-1] is None:
                            if piece.team == gridObject.piece1Turn or piece.king == True:
                                if colPos-1 >= 0:
                                    moves.append((rowPos+1, colPos-1))

                        # Left piece
                        elif isinstance(grid[rowPos+1][colPos-1], Piece) is True:
                            if piece.team == gridObject.piece1Turn or piece.king == True:
                                if colPos-1 >= 0:
                                    if grid[rowPos+1][colPos-1].team != piece.team:
                                        if grid[rowPos+2][colPos-2] is None:
                                            if colPos-2 >= 0:
                                                killMoves.append((rowPos+2, colPos-2))

                    except:
                        pass


                    try:
                        # Back right None
                        if grid[rowPos-1][colPos+1] is None:
                            if piece.team == gridObject.piece2Turn or piece.king == True:
                                if rowPos-1 >= 0:
                                    moves.append((rowPos-1, colPos+1))
                        
                        # Back right piece
                        elif isinstance(grid[rowPos-1][colPos+1], Piece) is True:
                            if piece.team == gridObject.piece2Turn or piece.king == True:
                                if rowPos-1 >= 0:
                                    if grid[rowPos-1][colPos+1].team != piece.team:
                                        if grid[rowPos-2][colPos+2] is None:
                                            if rowPos-2 >= 0:
                                                killMoves.append((rowPos-2, colPos+2))

                    except:
                        pass


                    try:
                        # Back Left None
                        if grid[rowPos-1][colPos-1] is None:
                            if piece.team == gridObject.piece2Turn or piece.king == True:
                                if rowPos-1 >= 0 and colPos-1 >= 0:
                                    moves.append((rowPos-1, colPos-1))

                        # Back right piece
                        elif isinstance(grid[rowPos-1][colPos-1], Piece) is True:
                            if piece.team == gridObject.piece2Turn or piece.king == True:
                                if rowPos-1 >= 0 and colPos-1 >= 0:
                                    if grid[rowPos-1][colPos-1].team != piece.team:
                                        if grid[rowPos-2][colPos-2] is None:
                                            if rowPos-2 >= 0 and colPos-2 >= 0:
                                                killMoves.append((rowPos-2, colPos-2))

                    except:
                        pass
                

                    i += 1

            movesPossible[(rowPos, colPos)] = (moves, killMoves)
    
    return movesPossible


def showPossibleMoves(board, grid, moves):
    if len(moves[0]) != 0 or len(moves[1]) != 0:
        if len(moves[0]) != 0:
            for move in moves[0]:
                board[move[0]][move[1]] = 4

        if len(moves[1]) != 0:
            for kill in moves[1]:
                board[kill[0]][kill[1]] = 5


def checkKing(grid):
    for row in grid.grid:
        for piece in row:
            if isinstance(piece, Piece) is True:
                if piece.y <= 30 and piece.team == grid.piece2Turn:
                    piece.king = True

                elif piece.y >= 450 and piece.team == grid.piece1Turn:
                    piece.king = True


def copyGrid(grid):
    newGrid = []

    for aRow in grid.grid:
        row = []
        for col in aRow:
            row.append(col)
        
        newGrid.append(row)
    
    return newGrid


def checkGameEnd(grid):
    piece1Moves = 0
    piece2Moves = 0
    piece1 = False
    piece2 = False
    movesList = []
    killsList = []

    moves = getVaildMoves(grid.grid, grid)
    
    # Count all of the playable 
    # moves.
    for move in moves:
        if isinstance(grid.grid[move[0]][move[1]], Piece):
            piece = grid.grid[move[0]][move[1]]
            if piece.team == grid.piece1Turn:
                piece1 = True
                piece2 = False
            
            elif piece.team == grid.piece2Turn:
                piece2 = True
                piece1 = False

            someMoves = moves[move]
            if len(someMoves[0]) != 0:
                for aMove in someMoves[0]:
                    if piece1 is True:
                        piece1Moves += 1
                    
                    elif piece2 is True:
                        piece2Moves += 1
                    
                    movesList.append((aMove, piece))

            if len(someMoves[1]) != 0:
                for aKill in someMoves[1]:
                    if piece1 is True:
                        piece1Moves += 1
                    
                    elif piece2 is True:
                        piece2Moves += 1
                    
                    killsList.append(aKill)
    
    if piece1Moves != 0 or piece2Moves != 0:
        # Piece2 wins
        if piece1Moves == 0 and piece2Moves > 0:
            return (True, grid.piece2Color)

        # Piece1 wins
        elif piece2Moves == 0 and piece1Moves > 0:
            return (True, grid.piece1Color)
        
        # Tie
        elif piece1Moves == piece2Moves and piece1Moves == 0:
            return (True, "tie")
    
    # Tie
    elif piece1Moves == piece2Moves:
        return (True, "tie")
    
    return (False, None)


def drawWindow(win, board, grid, turnColor, won=None):

    oriBoard = [
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0]
    ]
    
    width = 60
    height = 60

    x = 0
    y = 0

    # Draw board
    for rowPos, row in enumerate(board):
        for colPos, color in enumerate(row):

            square = pygame.rect.Rect(
                x, 
                y, 
                width, 
                height
            )

            # Draw a square of the board
            if color == 0:
                pygame.draw.rect(
                    win,
                    (255, 153, 0),
                    square
                )

            # Draw a highlighted player piece
            elif color == 2:
                pygame.draw.rect(
                    win,
                    (255, 255, 0),
                    square
                )          

            # Draw a square of the board
            elif color == 1:
                pygame.draw.rect(
                    win,
                    (0, 255, 60),
                    square
                )
            
            # Draw a highlighted player piece
            elif color == 3:
                pygame.draw.rect(
                    win,
                    (0, 255, 255),
                    square
                )
            
            # Draw the possible moves
            elif color == 4:
                pygame.draw.rect(
                    win,
                    (0, 0, 255),
                    square
                )
                board[rowPos][colPos] = oriBoard[rowPos][colPos]
            
            # Draw kill moves
            elif color == 5:
                pygame.draw.rect(
                    win,
                    (255, 0, 0),
                    square
                )
                board[rowPos][colPos] = oriBoard[rowPos][colPos]


            x += width

        x = 0
        y += height

    # Draw pieces
    for row in grid:
        for piece in row:
            if isinstance(piece, Piece):
                piece.draw(win)

    # Draw text to say 
    # whos turn it is.
    if True:
        colorToWord = {
            (255, 0, 0): "red",
            (0, 255, 0): "green",
            (0, 0, 255): "blue"
        }
        font = pygame.font.SysFont("comicsans", 30)
        if won == None:
            text = font.render(f"It is {colorToWord[turnColor]}s turn.", 1, (0, 0, 0))
            win.blit(text, (0, 0))
        else:
            if type(won) == str:
                text = font.render("TIE!!", 1, (0, 0, 0))
                win.blit(text, (240 - int(text.get_width() / 2), 240 - int(text.get_height() / 2)))
            
            elif type(won) == tuple:
                text = font.render(f"{colorToWord[won]} WON!!", 1, (0, 0, 0))
                win.blit(text, (240 - int(text.get_width() / 2), 240 - int(text.get_height() / 2)))


    pygame.display.update()



def main():

    # Setup boards
    if True:
        oriBoard = [
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0]
        ]

        board = [
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0]
        ]

    grid = Grid((255, 0, 0), (0, 0, 255))
    selectedPiece = (0, 0)

    SIZE = (480, 480)
    WIN = pygame.display.set_mode(SIZE)
    pygame.font.init()
    clock = pygame.time.Clock()
    turn = grid.piece1Turn
    won = None


    FPS = 60
    run = True
    while run:
        clock.tick(FPS)

        # Get and draw possible moves for 
        # selected piece.
        if True:
            validMovesForPiece = getVaildMoves(grid.grid, grid)
            # print(validMovesForPiece)
            validMovesForPiece = validMovesForPiece[selectedPiece]

            showPossibleMoves(board, grid.grid, validMovesForPiece)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()

                # Look for what piece the user 
                # may have clicked.
                for rowPos, row in enumerate(grid.grid):
                    for piecePos, piece in enumerate(row):

                        # Check to see if it is 
                        # a piece and not None.
                        if isinstance(piece, Piece) is True:

                            # If it's the turn of the 
                            # piece they are trying to 
                            # click then let them select 
                            # that piece.
                            if piece.team == turn:
                                clicked = piece.isOver(mousePos)
                                if clicked is True:
                                    piece.clicked = True

                                    if piece.takeOverPiece is not oriBoard[rowPos][piecePos]:
                                        piece.takeOverPiece = board[rowPos][piecePos]

                                    board[rowPos][piecePos] = piece.team
                                    selectedPiece = (rowPos, piecePos)
                                
                                elif piece.clicked is True:
                                    piece.clicked = False
                                    board[rowPos][piecePos] = piece.takeOverPiece

                # If the selectedPiece is not 
                # the initalied value then
                if selectedPiece != (0, 0):
                    for rowPos, row in enumerate(board):
                        for colPos, color in enumerate(row):
                            x = colPos*60
                            y = rowPos*60

                            # If user clicked over a 
                            # highlighed square move there.
                            if x < mousePos[0] < x+60:
                                if y < mousePos[1] < y+60:

                                    # If you the move is to 
                                    # move then move.
                                    if color == 4:
                                        grid.move((selectedPiece[0], selectedPiece[1]), (rowPos, colPos))
                                        selectedPiece = (0, 0)

                                        # Switch who's turn it is
                                        if turn == grid.piece1Turn:
                                            turn = grid.piece2Turn
                                        else:
                                            turn = grid.piece1Turn
                                    
                                    # Move and kill piece. 
                                    elif color == 5:
                                        grid.killMove((selectedPiece[0], selectedPiece[1]), (rowPos, colPos))
                                        selectedPiece = (0, 0)

                                        # Switch who's turn it is
                                        if turn == grid.piece1Turn:
                                            turn = grid.piece2Turn
                                        else:
                                            turn = grid.piece1Turn

        # Get the color of whoevers turn it is.
        if turn == grid.piece1Turn:
            turnColor = grid.piece1Color
        else:
            turnColor = grid.piece2Color

        checkKing(grid)
        gameEnd = checkGameEnd(grid)
        
        if gameEnd[0] is True:
            won = gameEnd[1]

        # Draw the screen
        drawWindow(WIN, board, grid.grid, turnColor, won)

    pygame.display.quit()





if __name__ == "__main__":
    main()



