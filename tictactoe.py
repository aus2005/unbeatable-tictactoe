import sys
import pygame
import numpy as np

pygame.init()

WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)

WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
ROW = 3
COL = 3
SQSIZE = WIDTH//COL
RAD = SQSIZE //3
CIRC = 15
CROSS = 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(0,0,0)
pygame.display.set_caption('Tic Tac Toe')
screen.fill(0,0,0)


board = np.zeros((ROW, COL))

def draw_lines(color=WHITE):
    for i in range(1, ROW):
        pygame.draw.line(screen, color, (0, SQSIZE * i), (WIDTH, SQSIZE * i), LINE_WIDTH)  # Horizontal line
        pygame.draw.line(screen, color, (SQSIZE * i, 0), (SQSIZE * i, HEIGHT), LINE_WIDTH)  # Vertical line

def draw_fig(color = WHITE):
    for row in range(ROW):
        for col in range(COL):
            if board[row][col] == 1:
                pygame.draw.circle(screen, color, (int(col * SQSIZE + SQSIZE // 2), int(row * SQSIZE + SQSIZE // 2)), RAD, CIRC)
            elif board[row][col] == 2:
                pygame.draw.line(screen, color, start_pos;(col *SQSIZE +SQSIZE //4, row*SQSIZE + SQSIZE //4), (row*SQSIZE+ 3*SQSIZE)) 