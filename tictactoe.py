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
                    pygame.draw.line(screen, color, (col * SQSIZE + SQSIZE // 4, row * SQSIZE + SQSIZE // 4), 
                    (col * SQSIZE + 3 * SQSIZE // 4, row * SQSIZE + 3 * SQSIZE // 4))
                    pygame.draw.line(screen, color, (col * SQSIZE + SQSIZE // 4, row * SQSIZE + 3 * SQSIZE // 4), 
                    (col * SQSIZE + 3 * SQSIZE // 4, row * SQSIZE + SQSIZE // 4))
def available_square(row, col):
     return board[row][col] == 0
def mark_square(row, col, player): #mark the squares occupied by players
     board[row][col] = player

def isFull(check_board = board): #check if the board is full
      for row in range (ROW):
           for col in range(COL):
                if check_board[row][col] == 0:
                     return False
      return True

def check_win(player, check_board = board): #check if a player already won
    for col in range(COL):
        if check_board[0][col] == player and check_board[1][col] == player and check_board[1][col] == player: #three in a column
            return True
    for row in range(ROW):
        if check_board[row][0] == player and check_board[row][1] == player and check_board[row][2] == player: #three in  a row
            return True    
    if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player: #diagonal three
            return True
    if check_board[2][0] == player and check_board[1][1] == player and check_board[0][2] == player: #diagonal three
            return True
    
    return False



def minimax(minimax_board, depth, is_maximizing):
    if check_win(2,minimax_board):
        return float('inf')
    elif check_win(1, minimax_board):
        return float('-inf')
    elif isFull(minimax_board):
         return 0
    

    if is_maximizing:
         best_score = -1000
         for row in range(ROW):
              for col in range(COL):
                   if minimax_board[row][col] == 0:
                        minimax_board[row][col] = 2
                        score = minimax(minimax_board, depth +1, is_maximizing=False)
                        minimax_board[row][col] = 0
                        best_score = max(score, best_score)
         return best_score
    else:
         best_score = 1000
         for row in range(ROW):
              for col in range(COL):
                   if minimax_board[row][col] == 0:
                        minimax_board[row][col] = 1
                        score = minimax(minimax_board, depth +1, is_maximizing=True)
                        minimax_board[row][col] = 0
                        best_score = min(score, best_score)
         return best_score
    
def best_move():
    best_score = -1000
    move = (-1, -1)
    for row in range(ROW):
         for col in range(COL):
              if board[row][col] == 0:
                   board[row][col] =2
                   score = minimax(board, depth=0, is_maximizing=False)
                   board[row][col] =0
                   if score > best_score:
                        best_score = score
                        move = (row, col)


    if move != (-1, -1):
        mark_square(move[0], move[1], 2)
        return True
    return False
         
def restart(): #reset all squares to zero
     screen.fill(BLACK)
     draw_lines()
     for row in range(ROW):
          for col in range(COL):
               board[row][col] = 0

draw_lines()

player = 1
game_over = False

while True:
     for event in pygame.event.get():
          if event.type == pygame.quit:
               sys.exit()

          if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
               mouseX = event.pos[0] // SQSIZE
               mouseY = event.pos[1] // SQSIZE

               if available_square(mouseY, mouseX):
                    mark_square(mouseX, mouseY, player)
                    if check_win(player):
                         game_over = True
                    player=player % 2 +1

          if not game_over:
                if best_move():
                    if check_win(2):
                        game_over = True
                        player = player %2 +1

          if not game_over:
                if isFull():
                  game_over = True

     if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
                player = 1


if not game_over:
     draw_fig()
else:
     if check_win(1):
          draw_fig(GREEN)
          draw_lines(GREEN)
     elif check_win(2):
          draw_lines(RED)
          draw_fig(RED)
     else:
          draw_fig(GRAY)
          draw_lines(GRAY)