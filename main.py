from http import client
from shutil import move
import sys
import objects,time,pygame,variables
from variables import boardX,boardY
x=0
p1turn = True
p2turn = False
p1Won  = False
p2Won = False
click = True
movesMade2 = [False,False,False,False,False,False,False,False,False]
movesMade1 = [False,False,False,False,False,False,False,False,False]

# CALLING OF THE FUNCTION TO
# MAKE THE SCREEN FOR THE WINDOW
screen1 = objects.welcomeScreen.makeCurrentScreen()

#whose turn is it
Turn = 0

#bool to help draw text
textBool1  = False
textBool2 =  False
# MAIN LOOPING
while True:
	# CALLING OF screenUpdate
	# function FOR MENU SCREEN
	objects.welcomeScreen.screenUpdate()
	
	# CALLING THE FUNCTION OF CONTROL BAR
	objects.winnerScreen.screenUpdate()
	# STORING THE MOUSE EVENT TO
	# CHECK THE POSITION OF THE MOUSE
	mouse_pos = pygame.mouse.get_pos()
	# CHECKING THE MOUSE CLICK EVENT
	mouse_click = pygame.mouse.get_pressed()
	# KEY PRESSED OR NOT
	keys = pygame.key.get_pressed()

# MENU BAR CODE TO ACCESS
	# CHECKING MENU SCREEN FOR ITS UPDATE	screen1
	if objects.welcomeScreen.checkUpdate():
		#Write  title text
		objects.Title.drawText(objects.welcomeScreen.returnTitle())#Tobias' Tictactoe
		objects.Player1SymbolChoice.drawText(objects.welcomeScreen.returnTitle())#Player1 X or O
		#X button
		objects.XButton.showButton(objects.welcomeScreen.returnTitle())
		objects.Player1symbol = objects.XButton.focusCheck(mouse_pos,mouse_click)
		if objects.Player1symbol:
			textBool1=True
		#O button
		objects.OButton.showButton(objects.welcomeScreen.returnTitle())
		objects.Player1symbol = objects.OButton.focusCheck(mouse_pos,mouse_click)
		if objects.Player1symbol:
			textBool2 = True
		#NExt button
		#check whether mouse is clicked while in button borders
		objects.goScreenbutton = objects.NextButton.focusCheck(mouse_pos,
												mouse_click)
		#draw next button
		objects.NextButton.showButton(objects.welcomeScreen.returnTitle())
		#if next button is pressed
		if objects.goScreenbutton:
			sys.exit()
		#which player is x 
		if textBool1:
			objects.PlayerSymbols1.drawText(objects.welcomeScreen.returnTitle())#Player1 X or O
			#player1 symbol is X
			p1Symbol ='X'
			p2Symbol ='O'
		elif textBool2:
			objects.PlayerSymbols2.drawText(objects.welcomeScreen.returnTitle())#Player1 X or O
			#player1 symbol is O
			p1Symbol ='O'
			p2Symbol ='X'
		
		
		#BOARD ASPECT OF GAME	
		
		#draw board
		objects.board.drawBoard(objects.welcomeScreen.returnTitle())
		#indicate whose turn it is
		if Turn %2 == 0:
			objects.p1turn.drawText(objects.welcomeScreen.returnTitle())
			isClicked,mov3 =objects.board.validatemove(objects.welcomeScreen.returnTitle(),mouse_pos,mouse_click)#if the move is valid
			#check if a valid move is made
			if click:	
				if isClicked:
					movesMade1[mov3-1]=True		
					Turn+=1	

		else:
			objects.p2turn.drawText(objects.welcomeScreen.returnTitle())
			isClicked,mov3 =objects.board.validatemove(objects.welcomeScreen.returnTitle(),mouse_pos,mouse_click)#if the move is valid
			#check if a valid move is made
			if click:
				if isClicked:
					movesMade2[mov3-1]=True	
					Turn +=1
		
		try:
			variables.BoardGate(movesMade1,p1Symbol,boardX,boardY)
			variables.BoardGate(movesMade2,p2Symbol,boardX,boardY)
			p1Won = variables.checkForWin(movesMade1,p1Won,p1Symbol)
			p2Won = variables.checkForWin(movesMade2,p2Won,p2Symbol)
			print(p1Won)
		except NameError:
			objects.p1_chooseXorO.drawText(objects.welcomeScreen.returnTitle())

			pass

		if p1Won == True:
			objects.p1Wins.drawText(objects.welcomeScreen.returnTitle())
			click = False

		if p2Won == True:
			objects.p2Wins.drawText(objects.welcomeScreen.returnTitle())
			click=False



	

	

	# CHECKING IF THE EXIT BUTTON HAS BEEN CLICKED OR NOT
	for event in pygame.event.get():
	
		# IF CLICKED THEN CLOSE THE WINDOW
		if(event.type == pygame.QUIT):
			pygame.quit()
			sys.exit()

    
	pygame.display.update()
	time.sleep(.02)




