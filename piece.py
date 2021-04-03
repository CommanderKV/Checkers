import pygame


class Piece:

    def __init__(self, x, y, color, team):
        self.x = x
        self.y = y
        self.clicked = False
        self.takeOverPiece = None

        if y < 160:
            self.team = 2
        else:
            self.team = 3

        self.king = False
        self.color = color
        self.radius = 25

    def draw(self, win):
        pygame.draw.circle(
            win, 
            self.color, 
            (self.x, self.y), 
            self.radius
        )

        if self.king is True:
            pygame.font.init()
            font = pygame.font.SysFont("comicsans", 30)
            txt = font.render("K", 1, (255, 255, 255))
            win.blit(txt, (self.x - int(txt.get_width()/2), self.y - int(txt.get_height()/2)))
    
    def isOver(self, pos):

        mouseX = pos[0]
        mouseY = pos[1]

        if -self.radius**2 < (mouseX - self.x)**2 + (mouseY - self.y)**2 < self.radius**2:
            return True
        else:
            return False




