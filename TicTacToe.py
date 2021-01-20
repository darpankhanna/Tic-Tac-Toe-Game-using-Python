import os
import time

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player = 1

win = 1
draw = -1
running = 0
stop = 1

Game = running
Mark = 'O'

#This Function displays Game Board
def GameBoard():
    print(" %c | %c | %c " % (board[1],board[2],board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4],board[5],board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7],board[8],board[9]))
    print("   |   |   ")

#Check whether the position is empty or not
def checkPosition(x):
    if(board[x] == ' '):
        return True
    else:
        return False

#Check whether player has won or not
def Checkwin():
    global Game
    #Horizontal win
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = win
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = win
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = win
    #Vertical win
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = win
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = win
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game=win
    #Diagonal win
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = win
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game=win
    #Draw condition
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        Game=draw
    else:
        Game=running

print("TIC TAC TOE GAME")
print("Player 1 [0]   Player 2 [X]\n")
print()
print()
time.sleep(2)
while(Game == running):
    os.system('cls')
    GameBoard()
    if(player % 2 != 0):
        print("Player 1's turn")
        Mark = 'O'
    else:
        print("Player 2's turn")
        Mark = 'X'
    choice = int(input("Enter the position [1-9] : "))
    if(checkPosition(choice)):
        board[choice] = Mark
        player+=1
        Checkwin()

os.system('cls')
GameBoard()
if(Game==draw):
    print("Game Draw")
elif(Game==win):
    player-=1
    if(player%2!=0):
        print("Player 1 is the WINNER")
    else:
        print("Player 2 is the WINNER")
