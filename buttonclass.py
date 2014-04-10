import pygame
class button(object):
	def __init__(self, sizex,sizey,locationx,locationy):
		self.sizex = sizex
		self.sizey = sizey 
		self.locationx = locationx 
		self.locationy= locationy
		

		self.button_rec = pygame.Rect(locationx,locationy,sizex,sizey)
		self.button_su = pygame.Surface([sizex,sizey])
		self.button_su.fill((25,102,16))
	def draw(self, main_screen):
		main_screen.blit(self.button_su, self.button_rec)
        
#everything below this is a test
	
if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600,600))
	main_screen.fill((255,255,255))
	b=button(100,100,120,120,)
	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x,y = ev.pos
			if button_rec.collidepoint(x,y):
				print "click"
		
		pygame.display.flip()
