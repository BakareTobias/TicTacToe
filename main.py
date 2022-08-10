import objects,time,pygame

done = False

toggle = False

# CALLING OF THE FUNCTION TO
# MAKE THE SCREEN FOR THE WINDOW
win = objects.welcomeScreen.makeCurrentScreen()


# MAIN LOOPING
while not done:
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
	# CHECKING MENU SCREEN FOR ITS UPDATE
	if objects.welcomeScreen.checkUpdate():
		objects.goScreenbutton = objects.NextButton.focusCheck(mouse_pos,
												mouse_click)
		objects.NextButton.showButton(objects.welcomeScreen.returnTitle())

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
			
	# CHECKING IF THE EXIT BUTTON HAS BEEN CLICKED OR NOT
	for event in pygame.event.get():
	
		# IF CLICKED THEN CLOSE THE WINDOW
		if(event.type == pygame.QUIT):
			done = True

    
	pygame.display.update()
	time.sleep(.02)
# CLOSE THE PROGRAM
pygame.quit()



