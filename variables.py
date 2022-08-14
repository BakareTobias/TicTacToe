import objects

screenWidth = 380
screenHeight=520


#set up colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (215,0,0)
GREEN  = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
TEAL = (0,128,128)
GOLD = (212,175,55)
SUNSET_YELLOW = (255,201,34)
SEA_BLUE = (0,105,148)
NIGHT_SKY = (19,24,98)

p1ix = ("Player1 is X \n Player 2 is O")

p1io = ("Player1 is O \n Player 2 is X")

movesLeft = [1,2,3,4,5,6,7,8,9]

boardX=100
boardY=200

        
def BoardGate(movesMade,pSymbol,boardX,boardY):
	if movesMade[0] == True:
			if pSymbol == 'X' :
				objects.board.drawX(objects.welcomeScreen.returnTitle(),boardX,boardY)
			elif pSymbol == 'O' :
				objects.board.drawO(objects.welcomeScreen.returnTitle(),boardX,boardY)
            
            


	if movesMade[1] == True:
			if pSymbol == 'X' :
				objects.board.drawX(objects.welcomeScreen.returnTitle(),boardX+50,boardY)
			elif pSymbol == 'O' :
				objects.board.drawO(objects.welcomeScreen.returnTitle(),boardX+50,boardY)

	if movesMade[2] == True:
		if pSymbol == 'X' :
			objects.board.drawX(objects.welcomeScreen.returnTitle(),boardX+100,boardY)
		elif pSymbol == 'O' :
			objects.board.drawO(objects.welcomeScreen.returnTitle(),boardX+100,boardY)

	
	if movesMade[3] == True:
		if pSymbol == 'X' :
			objects.board.drawX(objects.welcomeScreen.returnTitle(),boardX,boardY+50)
		elif pSymbol == 'O' :
			objects.board.drawO(objects.welcomeScreen.returnTitle(),boardX,boardY+50)


	if movesMade[4] == True:
		if pSymbol == 'X' :
			objects.board.drawX(objects.welcomeScreen.returnTitle(),boardX+50,boardY+50)
		elif pSymbol == 'O' :
			objects.board.drawO(objects.welcomeScreen.returnTitle(),boardX+50,boardY+50)

	
	if movesMade[5] == True:
		if pSymbol == 'X' :
			objects.board.drawX(objects.welcomeScreen.returnTitle(),boardX+100,boardY+50)
		elif pSymbol == 'O' :
			objects.board.drawO(objects.welcomeScreen.returnTitle(),boardX+100,boardY+50)


	if movesMade[6] == True:
		if pSymbol == 'X' :
			objects.board.drawX(objects.welcomeScreen.returnTitle(),boardX,boardY+100)
		elif pSymbol == 'O' :
			objects.board.drawO(objects.welcomeScreen.returnTitle(),boardX,boardY+100)

	
	if movesMade[7] == True:
		if pSymbol == 'X' :
			objects.board.drawX(objects.welcomeScreen.returnTitle(),boardX+50,boardY+100)
		elif pSymbol == 'O' :
			objects.board.drawO(objects.welcomeScreen.returnTitle(),boardX+50,boardY+100)


	if movesMade[8] == True:
		if pSymbol == 'X' :
			objects.board.drawX(objects.welcomeScreen.returnTitle(),boardX+100,boardY+100)
		elif pSymbol == 'O' :
			objects.board.drawO(objects.welcomeScreen.returnTitle(),boardX+100,boardY+100)


def checkForWin(movesMade,pWon,pSymbol):#CHECK IF THE MOVE IS A WINNING MOVE 
    for _ in (1,4,7):
        _ = _-1
        if (movesMade[_] == movesMade[_+1] == movesMade[_+2]==True):
            return True
		


    for _ in (1,2,3):
        _ = _-1
        if (movesMade[_] == movesMade[_+3] == movesMade[_+6]==True):
            return True
		
    _ = 3
    _ = _-1
    if (movesMade[_] == movesMade[_+2] == movesMade[_+4]==True):
            return True
		
    _ = 1
    _ = _-1
    if (movesMade[_] == movesMade[_+4] == movesMade[_+8]==True):
            return True

 