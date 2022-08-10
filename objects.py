from classes import Screen, NavButton,variables

##welcome screen where player 1 and 2 select X or O
welcomeScreen = Screen("Welcome screen")
NextButton = NavButton(300, 450, 80, 50, variables.GOLD,
					variables.RED, "TimesNewRoman",
					variables.WHITE, "Next")

#board screen
goScreen = Screen("go screen")
goButton = NavButton(0, 450, 80, 50, variables.BLACK,
					variables.RED, "TimesNewRoman",
					variables.WHITE, "Back") 

#winner screen
winnerScreen = Screen("Winner screen")


#end screen 
endScreen = Screen("end screen")
