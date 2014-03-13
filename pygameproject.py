import pygame

if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((400, 400))
	main_screen.fill((255,255,255))
	button_rec = pygame.Rect(1,1,3000,3000)
	button_su = pygame.Surface([20, 20])
	button_su.fill((34,100,100))
	main_screen.blit(button_su, button_rec)

while True: 
        ev = pygame.event.poll()
       
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = ev.pos
            if button_rec.collidepoint(x, y):
                print "you clicked me!"
        pygame.display.flip()
    
