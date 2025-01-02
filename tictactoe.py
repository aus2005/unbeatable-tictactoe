import sys
import pygame
import numpy as np

pygame.init()

WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
ROW = 3
COL = 3
SQSIZE = WIDTH // COL
RAD = SQSIZE // 3
CIRC = 15
CROSS = 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BLACK)

board = np.zeros((ROW, COL))

def draw_lines(color=WHITE):
    for i in range(1, ROW):
        pygame.draw.line(screen, color, (0, SQSIZE * i), (WIDTH, SQSIZE * i), LINE_WIDTH)  # Horizontal lines
        pygame.draw.line(screen, color, (SQSIZE * i, 0), (SQSIZE * i, HEIGHT), LINE_WIDTH)  # Vertical lines

def draw_fig(color=WHITE):
    for row in range(ROW):
        for col in range(COL):
            if board[row][col] == 1:
                pygame.draw.circle(screen, color, 
                                   (int(col * SQSIZE + SQSIZE // 2), int(row * SQSIZE + SQSIZE // 2)), 
                                   RAD, CIRC)
            elif board[row][col] == 2:
                pygame.draw.line(screen, color, 
                                 (col * SQSIZE + SQSIZE // 4, row * SQSIZE + SQSIZE // 4), 
                                 (col * SQSIZE + 3 * SQSIZE // 4, row * SQSIZE + 3 * SQSIZE // 4), CROSS)
                pygame.draw.line(screen, color, 
                                 (col * SQSIZE + SQSIZE // 4, row * SQSIZE + 3 * SQSIZE // 4), 
                                 (col * SQSIZE + 3 * SQSIZE // 4, row * SQSIZE + SQSIZE // 4), CROSS)

def available_square(row, col):
    return board[row][col] == 0

def mark_square(row, col, player):
    board[row][col] = player

# Check if board is full
def isFull():
    return not np.any(board == 0)

# Check if a player has won
def check_win(player):
    for col in range(COL):  # Vertical win
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    for row in range(ROW):  # Horizontal win
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    # Diagonal wins
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[2][0] == board[1][1] == board[0][2] == player:
        return True
    return False

def minimax(minimax_board, depth, is_maximizing):
    if check_win(2):  # Computer wins
        return 10 - depth
    elif check_win(1):  # Player wins
        return depth - 10
    elif isFull():  # Tie
        return 0

    if is_maximizing:
        best_score = -1000
        for row in range(ROW):
            for col in range(COL):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth + 1, False)
                    minimax_board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for row in range(ROW):
            for col in range(COL):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth + 1, True)
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -1000
    move = (-1, -1)
    for row in range(ROW):
        for col in range(COL):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
    if move != (-1, -1):
        mark_square(move[0], move[1], 2)

# Reset al boxes
def restart():
    screen.fill(BLACK)
    draw_lines()
    board.fill(0)

draw_lines()
player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // SQSIZE
            mouseY = event.pos[1] // SQSIZE

            if available_square(mouseY, mouseX):
                mark_square(mouseY, mouseX, player)
                if check_win(player):
                    game_over = True
                player = 3 - player  # Switch player

        if not game_over and player == 2:
            best_move()
            if check_win(2):
                game_over = True
                player = 3 - player

        if not game_over and isFull():
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
                player = 1

    screen.fill(BLACK)
    draw_lines()
    draw_fig()
    pygame.display.update()
