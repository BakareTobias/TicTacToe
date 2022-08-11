import sys
import objects,time,pygame


# CALLING OF THE FUNCTION TO
# MAKE THE SCREEN FOR THE WINDOW
screen1 = objects.welcomeScreen.makeCurrentScreen()

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
			win = objects.winnerScreen.makeCurrentScreen()
			objects.welcomeScreen.endCurrentScreen()

	# CONTROL BAR CODE TO ACCESS
	# CHECKING CONTROL SCREEN FOR ITS UPDATE
	elif objects.goScreen.checkUpdate():
		return_back = objects.goButton.focusCheck(mouse_pos,
												mouse_click)
		objects.goButton.showButton(objects.goScreen.returnTitle())

		if return_back:
			objects.goScreen.endCurrentScreen()
			win = objects.welcomeScreen.makeCurrentScreen()
	if textBool1:
		objects.PlayerSymbols1.drawText(objects.welcomeScreen.returnTitle())#Player1 X or O
	elif textBool2:
		objects.PlayerSymbols2.drawText(objects.welcomeScreen.returnTitle())#Player1 X or O

	# CHECKING IF THE EXIT BUTTON HAS BEEN CLICKED OR NOT
	for event in pygame.event.get():
	
		# IF CLICKED THEN CLOSE THE WINDOW
		if(event.type == pygame.QUIT):
			pygame.quit()
			sys.exit()

    
	pygame.display.update()
	time.sleep(.02)




