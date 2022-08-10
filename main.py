import screens,time,pygame

done = False

toggle = False

# CALLING OF THE FUNCTION TO
# MAKE THE SCREEN FOR THE WINDOW
win = screens.welcomeScreen.makeCurrentScreen()


# MAIN LOOPING
while not done:
	# CALLING OF screenUpdate
	# function FOR MENU SCREEN
	screens.welcomeScreen.screenUpdate()
	
	# CALLING THE FUNCTION OF CONTROL BAR
	screens.winnerScreen.screenUpdate()
	# STORING THE MOUSE EVENT TO
	# CHECK THE POSITION OF THE MOUSE
	mouse_pos = pygame.mouse.get_pos()
	# CHECKING THE MOUSE CLICK EVENT
	mouse_click = pygame.mouse.get_pressed()
	# KEY PRESSED OR NOT
	keys = pygame.key.get_pressed()

# MENU BAR CODE TO ACCESS
	# CHECKING MENU SCREEN FOR ITS UPDATE
	if screens.welcomeScreen.checkUpdate():
		screens.goScreenbutton = screens.NextButton.focusCheck(mouse_pos,
												mouse_click)
		screens.NextButton.showButton(screens.welcomeScreen.returnTitle())

		if screens.goScreenbutton:
			win = screens.winnerScreen.makeCurrentScreen()
			screens.welcomeScreen.endCurrentScreen()

	# CONTROL BAR CODE TO ACCESS
	# CHECKING CONTROL SCREEN FOR ITS UPDATE
	elif screens.goScreen.checkUpdate():
		return_back = screens.goButton.focusCheck(mouse_pos,
												mouse_click)
		screens.goButton.showButton(screens.goScreen.returnTitle())

		if return_back:
			screens.goScreen.endCurrentScreen()
			win = screens.welcomeScreen.makeCurrentScreen()
			
	# CHECKING IF THE EXIT BUTTON HAS BEEN CLICKED OR NOT
	for event in pygame.event.get():
	
		# IF CLICKED THEN CLOSE THE WINDOW
		if(event.type == pygame.QUIT):
			done = True

    
	pygame.display.update()
	time.sleep(.02)
# CLOSE THE PROGRAM
pygame.quit()



