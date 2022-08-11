from typing import Text
from classes import Screen, NavButton,variables,Text,SelectionButtons

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
							320,variables.TEAL,20)
XButton = SelectionButtons(170,140,40,40,None,variables.RED,
							"PermanentMarker-Regular.ttf",
							variables.WHITE, "X")
OButton = SelectionButtons(230,140,40,40,None,variables.RED,
							"PermanentMarker-Regular.ttf",
							variables.WHITE, "O")
PlayerSymbols1 = Text(variables.p1ix,variables.screenWidth,420,variables.TEAL,25)
PlayerSymbols2 = Text(variables.p1io,variables.screenWidth,420,variables.TEAL,25)


#board screen
goScreen = Screen("go screen")
goButton = NavButton(0, 450, 80, 50, variables.BLACK,
					variables.RED, "TimesNewRoman",
					variables.WHITE, "Back") 

#winner screen
winnerScreen = Screen("Winner screen")


#end screen 
endScreen = Screen("end screen")
