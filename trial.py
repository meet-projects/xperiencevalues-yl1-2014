import pygame
def crtrec(x,y,sx,sy):
	button_rec = pygame.Rect(x,y,120,120)
	button_su = pygame.Surface([120,120])
	main_screen.blit(button_su,button_rec)

if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600,600))
	main_screen.fill((255,255,255))

	#button_rec = pygame.Rect(0,0,120,120)
	#button_su = pygame.Surface([120,120])
	#main_screen.blit(button_su,button_rec)
	a=0
	b=0
	while True:
		ev = pygame.event.poll()
		crtrec(a,b,120,120)
		if ev.type == pygame.MOUSEBUTTONDOWN:
			a,b=ev.pos
			if button_rec.collidepoint(a,b):
				crtrec(a,b,120,120)
				a+=120
				b+=120
		pygame.display.flip()
					
