from typing import Text
from classes import Board, Screen, NavButton,variables,Text,SelectionButtons
import variables
#WELCOME SCREEN(SCREEN 1)
##welcome screen where player 1 and 2 select X or O
welcomeScreen = Screen("Welcome screen")
#Next Button
NextButton = NavButton(300, 450, 80, 50, variables.GOLD,
					variables.RED, "TimesNewRoman",
					variables.WHITE, "Next")
#title
Title = Text("Tobias' Tic-Tac-Toe",variables.screenWidth,80,variables.TEAL,25)

Player1SymbolChoice = Text("Player1 X or O?",variables.screenWidth-200,
							170,variables.TEAL,20)
XButton = SelectionButtons(170,65,40,40,None,variables.RED,
							"PermanentMarker-Regular.ttf",
							variables.WHITE, "X")
OButton = SelectionButtons(230,65,40,40,None,variables.RED,
							"PermanentMarker-Regular.ttf",
							variables.WHITE, "O")
PlayerSymbols1 = Text(variables.p1ix,variables.screenWidth,270,variables.TEAL,25)
PlayerSymbols2 = Text(variables.p1io,variables.screenWidth,270,variables.TEAL,25)

#BOARD
p1turn = Text("Player1's turn",variables.screenWidth-20,340,variables.TEAL,25)
p2turn = Text("Player2's turn",variables.screenWidth-20,340,variables.TEAL,25)




board = Board(variables.boardX,variables.boardY)





#SCREEN 2 Board Screen
goScreen = Screen("go screen")
goButton = NavButton(0, 450, 80, 50, variables.BLACK,
					variables.RED, "TimesNewRoman",
					variables.WHITE, "Back") 

#winner screen
winnerScreen = Screen("Winner screen")


#end screen 
endScreen = Screen("end screen")
