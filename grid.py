from piece import Piece

class Grid:
    
    def __init__(self, p1Color=(0, 0, 0), p2Color=(255, 255, 255), grid=None):
        self.piece1Turn = 2
        self.piece2Turn = 3

        if grid is None:
            self.piece1Color = p1Color
            self.piece2Color = p2Color

            self.piece1Amount = 12
            self.piece2Amount = 12

            self.grid = [
                [None,                          Piece(90, 30, p1Color, 0),      None,                           Piece(210, 30, p1Color, 0),     None,                           Piece(330, 30, p1Color, 0),     None,                           Piece(450, 30, p1Color, 0)      ],
                [Piece(30, 90, p1Color, 0),     None,                           Piece(150, 90, p1Color, 0),     None,                           Piece(270, 90, p1Color, 0),     None,                           Piece(390, 90, p1Color, 0),     None                            ],
                [None,                          Piece(90, 150, p1Color, 0),     None,                           Piece(210, 150, p1Color, 0),    None,                           Piece(330, 150, p1Color, 0),    None,                           Piece(450, 150, p1Color, 0)     ],
                
                [None,                          None,                           None,                           None,                           None,                           None,                           None,                           None                            ],
                [None,                          None,                           None,                           None,                           None,                           None,                           None,                           None                            ],
                
                [Piece(30, 330, p2Color, 1),    None,                           Piece(150, 330, p2Color, 1),    None,                           Piece(270, 330, p2Color, 1),    None,                           Piece(390, 330, p2Color, 1),    None                            ],
                [None,                          Piece(90, 390, p2Color, 1),     None,                           Piece(210, 390, p2Color, 1),    None,                           Piece(330, 390, p2Color, 1),    None,                           Piece(450, 390, p2Color, 1)     ],
                [Piece(30, 450, p2Color, 1),    None,                           Piece(150, 450, p2Color, 1),    None,                           Piece(270, 450, p2Color, 1),    None,                           Piece(390, 450, p2Color, 1),    None                            ]
            ]

        else:
            self.piece1Amount = 0
            self.piece2Amount = 0

            for row in grid:
                for piece in row:
                    if isinstance(piece, Piece) is True:
                        if piece.turn == self.piece1Turn:
                            self.piece1Color = piece.color
                            self.piece1Amount += 1
                        
                        elif piece.turn == self.piece2Turn:
                            self.piece2Color = piece.color
                            self.piece2Amount += 1

            self.grid = grid



    def getDirection(self, startPos, endPos):
        direction = 0 # Need to put something in here to get it to work

        if True:
            # To the right
            if startPos[0] > endPos[0]:

                # Up 
                if startPos[1] < endPos[1]:
                    # print("RIGHT UP")
                    direction = 2
                
                # Down
                elif startPos[1] > endPos[1]:
                    # print("RIGHT DOWN")
                    direction = -2
            

            # To the left
            elif startPos[0] < endPos[0]:
                
                # Up 
                if startPos[1] < endPos[1]:
                    # print("LEFT UP")
                    direction = 1
                
                # Down
                elif startPos[1] > endPos[1]:
                    # print("LEFT DOWN")
                    direction = -1
        
        if True:
            # Bottom right
            if direction == 1:
                xDiff = 1
                yDiff = 1
                
            # Botom left
            elif direction == -1:
                xDiff = -1
                yDiff = 1

            # Top right
            elif direction == 2:
                xDiff = 1
                yDiff = -1
            
            # Top left
            elif direction == -2:
                xDiff = -1
                yDiff = -1

        return xDiff, yDiff


    def move(self, startPos, endPos):
        
        xDiff, yDiff = self.getDirection(startPos, endPos)

        self.grid[endPos[0]][endPos[1]] = self.grid[startPos[0]][startPos[1]]
        self.grid[endPos[0]][endPos[1]].clicked = False

        self.grid[endPos[0]][endPos[1]].x += 60*xDiff
        self.grid[endPos[0]][endPos[1]].y += 60*yDiff

        self.grid[startPos[0]][startPos[1]] = None


    def killMove(self, startPos, endPos):

        xDiff, yDiff = self.getDirection(startPos, endPos)
        x = 120*xDiff
        y = 120*yDiff

        if xDiff > 0:
            if yDiff > 0:
                removeX = endPos[1]-1
                removeY = endPos[0]-1
                # print(1)
            elif yDiff < 0:
                removeX = endPos[1]-1
                removeY = endPos[0]+1
                # print(2)
        
        elif xDiff < 0:
            if yDiff > 0:
                removeX = endPos[1]+1
                removeY = endPos[0]-1
                # print(3)
            
            elif yDiff < 0:
                removeX = endPos[1]+1
                removeY = endPos[0]+1
                # print(4)

        self.grid[endPos[0]][endPos[1]] = self.grid[startPos[0]][startPos[1]]
        self.grid[endPos[0]][endPos[1]].clicked = False

        self.grid[endPos[0]][endPos[1]].x += x
        self.grid[endPos[0]][endPos[1]].y += y

        if self.grid[startPos[0]][startPos[1]].team == self.piece1Turn:
            self.piece1Amount -= 1
        else:
            self.piece2Amount -= 1
             
        self.grid[startPos[0]][startPos[1]] = None

        self.grid[removeY][removeX] = None








