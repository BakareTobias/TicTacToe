from re import T
from shutil import move
import sys
from tkinter import font
import variables,pygame
pygame.init()
pygame.event.get()

class Board():
	def __init__(self,x,y):
		self.x = x
		self.y = y


	def drawBoard(self,display):
		pygame.draw.line(display,variables.WHITE,(self.x+50,self.y),(self.x+50,self.y+150),6)
		pygame.draw.line(display,variables.WHITE,(self.x+100,self.y),(self.x+100,self.y+150),6)
		pygame.draw.line(display,variables.WHITE,(self.x,self.y+50),(self.x+150,self.y+50),6)
		pygame.draw.line(display,variables.WHITE,(self.x,self.y+100),(self.x+150,self.y+100),6)

	def drawX(self,display,x,y):
		x+=10
		y+=10
		pygame.draw.line(display,variables.BLACK,(x,y),(x+30,y+30),4)
		pygame.draw.line(display,variables.BLACK,(x,y+30),(x+30,y),4)

	def drawO(self,display,x,y):
		x+=25
		y+=25
		pygame.draw.circle(display,variables.WHITE,(x,y),17,3)

	def DrawMove(Pmove,pSymbol):
		if Pmove ==1 and pSymbol=='X':
			move1=True
			return move1

	def validatemove(self,display,mousepos,mouseclick ):
		
		#ROW 1
		if self.x<=mousepos[0]<=self.x+54 and self.y<=mousepos[1]<=self.y+50 and 1 in variables.movesLeft and pygame.mouse.get_pressed()[0] :
			variables.movesLeft.remove(1)
			return mouseclick[0],1
		if self.x+55<=mousepos[0]<=self.x+110 and self.y<=mousepos[1]<=self.y+50 and 2 in variables.movesLeft and pygame.mouse.get_pressed()[0]:
			variables.movesLeft.remove(2)
			return mouseclick[0],2
		if self.x+111<=mousepos[0]<=self.x+166 and self.y<=mousepos[1]<=self.y+50 and 3 in variables.movesLeft and pygame.mouse.get_pressed()[0]:  
			variables.movesLeft.remove(3)
			return mouseclick[0],3
		#ROW 2
		if self.x<=mousepos[0]<=self.x+54 and self.y+51<=mousepos[1]<=self.y+101 and 4 in variables.movesLeft and pygame.mouse.get_pressed()[0]:
			variables.movesLeft.remove(4)
			return mouseclick[0],4
		if self.x+55<=mousepos[0]<=self.x+110 and self.y+51<=mousepos[1]<=self.y+101 and 5 in variables.movesLeft and pygame.mouse.get_pressed()[0]:
		
			variables.movesLeft.remove(5)
			return mouseclick[0],5
		if self.x+111<=mousepos[0]<=self.x+166 and self.y+51<=mousepos[1]<=self.y+101 and 6 in variables.movesLeft and pygame.mouse.get_pressed()[0]:
		  
			variables.movesLeft.remove(6)
			return mouseclick[0],6
		#ROW 3
		if self.x<=mousepos[0]<=self.x+54 and self.y+102<=mousepos[1]<=self.y+152 and 7 in variables.movesLeft and pygame.mouse.get_pressed()[0]:
		  
			variables.movesLeft.remove(7)
			return mouseclick[0],7
		if self.x+55<=mousepos[0]<=self.x+110 and self.y+102<=mousepos[1]<=self.y+152 and 8 in variables.movesLeft and pygame.mouse.get_pressed()[0]:
		
			variables.movesLeft.remove(8)
			return mouseclick[0],8
		if self.x+111<=mousepos[0]<=self.x+166 and self.y+102<=mousepos[1]<=self.y+152 and 9 in variables.movesLeft and pygame.mouse.get_pressed()[0]:
		  
			variables.movesLeft.remove(9)
			return mouseclick[0],9
		else:
			return False,0
			



class Screen():

	# INITIALIZATION OF SCREEN HAVING TITLE,
	# WIDTH, HEIGHT AND COLOUR
	# HERE (0,0,255) IS A COLOUR CODE
	def __init__(self, title, width=variables.screenWidth, height=variables.screenHeight,
				backgroundColor=variables.TEAL):
		# HEIGHT OF A WINDOW
		self.height = height
		# TITLE OF A WINDOW
		self.title = title
		# WIDTH OF A WINDOW
		self.width = width
		# COLOUR CODE
		self.backgroundColor = backgroundColor
		# CURRENT STATE OF A SCREEN
		self.CurrentState = False

	# DISPLAY THE CURRENT SCREEN OF
	# A WINDOW AT THE CURRENT STATE
	def makeCurrentScreen(self):
	
		# SET THE TITLE FOR THE CURRENT STATE OF A SCREEN
		pygame.display.set_caption(self.title)
		# SET THE STATE TO ACTIVE
		self.CurrentState = True
		# ACTIVE SCREEN SIZE
		self.screen = pygame.display.set_mode((self.width,
										self.height))

	# THIS WILL SET THE STATE OF A CURRENT STATE TO OFF
	def endCurrentScreen(self):
		self.CurrentState = False

	# THIS WILL CONFIRM WHEHTER THE NAVIGATION OCCURS
	def checkUpdate(self):
		return self.CurrentState

	# THIS WILL UPDATE THE SCREEN WITH
	# THE NEW NAVIGATION TAB
	def screenUpdate(self):
		if self.CurrentState:
			self.screen.fill(self.backgroundColor)
			

	# RETURNS THE TITLE OF THE SCREEN
	def returnTitle(self):
		return self.screen


class Button:
	# INITIALIZATION OF BUTTON
	# COMPONENTS LIKE POSITION OF BUTTON,
	# COLOR OF BUTTON, FONT COLOR OF BUTTON, FONT SIZE,
	# TEXT INSIDE THE BUTTON
	def __init__(self, x, y, sx, sy, bcolour,
				fbcolour, font, fcolour, text):
		# ORIGIN_X COORDINATE OF BUTTON
		self.x = x
		# ORIGIN_Y COORDINATE OF BUTTON
		self.y = y
		# LAST_X COORDINATE OF BUTTON
		self.sx = sx
		# LAST_Y COORDINATE OF BUTTON
		self.sy = sy
		# FONT SIZE FOR THE TEXT IN A BUTTON
		self.fontsize = 25
		# BUTTON COLOUR
		self.bcolour = bcolour
		# RECTANGLE COLOR USED TO DRAW THE BUTTON
		self.fbcolour = fbcolour
		# BUTTON FONT COLOR
		self.fcolour = fcolour
		# TEXT IN A BUTTON
		self.text = text
		# CURRENT IS OFF
		self.CurrentState = False
		#font
		self.font =font
		# FONT OBJECT FROM THE SYSTEM FONTS
		self.buttonf = pygame.font.SysFont(self.font, self.fontsize)# A comment.

	# DRAW THE BUTTON FOR THE SCREENS
	def showButton(self, display):
		if(self.CurrentState):
			pygame.draw.rect(display, self.fbcolour,
						(self.x, self.y,
						self.sx, self.sy),0,9)
		else:
			pygame.draw.rect(display, self.fbcolour,
						(self.x, self.y,
						self.sx, self.sy),0,9)
		# RENDER THE FONT OBJECT FROM THE STSTEM FONTS
		textsurface = self.buttonf.render(self.text,
										False, self.fcolour)

		# THIS LINE WILL DRAW THE SURF ONTO THE SCREEN
		display.blit(textsurface,
					(self.x + (self.sx/4) 
					, (self.y + (self.sy/4))))
	
# NAVIGATION BUTTON CLASS
class NavButton(Button):
	# THIS FUCNTION CAPTURE WHETHER
	# ANY MOUSE EVENT OCCUR ON THE BUTTON
	def focusCheck(self, mousepos, mouseclick):
		if(mousepos[0] >= self.x and mousepos[0] <= self.x +
				self.sx and mousepos[1] >= self.y and mousepos[1]
				<= self.y + self.sy):
			self.fbcolour=variables.GOLD	
			self.CurrentState = True
			# IF MOUSE BUTTON CLICK THEN
			# NAVIGATE TO THE NEXT OR PREVIOUS TABS
			return mouseclick[0]

		else:
			self.fbcolour=variables.RED	
			# ELSE LET THE CURRENT STATE TO BE OFF
			self.CurrentState = False
			return False

class SelectionButtons(Button):
	def focusCheck(self, mousepos, mouseclick):
		if(mousepos[0] >= self.x and mousepos[0] <= self.x +
				self.sx and mousepos[1] >= self.y and mousepos[1]
				<= self.y + self.sy):
			self.fbcolour = variables.GOLD
			self.CurrentState = True
			# IF MOUSE BUTTON CLICK THEN
			# NAVIGATE TO THE NEXT OR PREVIOUS TABS
			return mouseclick[0]

		else:
			self.fbcolour=variables.RED	

			# ELSE LET THE CURRENT STATE TO BE OFF
			self.CurrentState = False
			return False


class Text():
	#class for all text in TicTacToe program
	def __init__(self,content,x,y,backgroundColor,fontSize):
		self.content = content
		self.x = x
		self.y = y
		self.backgroundColor  = backgroundColor
		self.fontColor = variables.WHITE
		self.fontsize = fontSize
		self.buttonf = pygame.font.Font("Quicksand-VariableFont_wght.ttf",self.fontsize)

	def drawText(self,display):
		textsurface = self.buttonf.render(self.content,True,self.fontColor,self.backgroundColor)
			# THIS LINE WILL DRAW THE SURF ONTO THE SCREEN
		textRect = textsurface.get_rect()
		textRect.center = (self.x//2,self.y//2)

		display.blit(textsurface,textRect)
			
		

	

		
