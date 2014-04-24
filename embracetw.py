import pygame
import buttonclass

if __name__=="__main__":
    pygame.init()
    main_screen = pygame.display.set_mode((400, 400))
    main_screen.fill((255,255,255))

    
    myfont = pygame.font.SysFont("ComicSansMS", 48)
    label = myfont.render("Embrace team work: ", 1, (11,46,7))
     
    main_screen.blit(label, (5, 20))

    button9=buttonclass.button(155, 70,20,100)
    button9.draw(main_screen)
    button9.button_su.fill((205, 92, 92))
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render("playing team  ", 1, (11,206,7))
    label2 = myfont.render("sport ", 1, (11,206,7))

    main_screen.blit(label, (28, 120))
    main_screen.blit(label2, (28, 140))
    button10=buttonclass.button(150, 70,230,100)
    button10.draw(main_screen)
    button10.button_su.fill((205, 92, 92))
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render("Work with people", 1, (11,206,7))

    main_screen.blit(label, (240, 120))
    
    while True: 
        ev = pygame.event.poll()
       
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = ev.pos
            # if button_rec.collidepoint(x, y):
                # print "you clicked me!"
        pygame.display.flip()
    
