import pygame
import buttonclass

if __name__=="__main__":
    pygame.init()
    main_screen = pygame.display.set_mode((400, 400))
    main_screen.fill((255,255,255))

    # myfont = pygame.font.SysFont("ComicSansMS", 48)
    # label = myfont.render("Pick a value:", 1, (11,46,7))
    # main_screen.blit(label, (100, 20))
    # button=buttonclass.button(115, 70,20,100)
    # button.draw(main_screen)
    # myfont = pygame.font.SysFont("ComicSansMS", 18)
    # label = myfont.render(" Lead by example", 1, (11,206,7))
    # main_screen.blit(label, (22, 120))
    # button2=buttonclass.button(115, 70,320,100)
    # button2.draw(main_screen)
    # myfont = pygame.font.SysFont("ComicSansMS", 18)
    # label = myfont.render("Equality", 1, (11,206,7))
    # main_screen.blit(label, (22, 120))
    # button3=buttonclass.button(115, 70,165,240)
    # button3.draw(main_screen)
    # myfont = pygame.font.SysFont("ComicSansMS", 18)
    # label = myfont.render("Team work", 1, (11,206,7))
    # main_screen.blit(label, (22, 120))

    myfont = pygame.font.SysFont("ComicSansMS", 48)
    label = myfont.render("Lead by example:", 1, (11,46,7))
     
    main_screen.blit(label, (5, 20))

    button3=buttonclass.button(150, 70,20,100)
    button3.draw(main_screen)
    button3.button_su.fill((205, 92, 92))
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render("Working with children", 1, (11,206,7))

    main_screen.blit(label, (28, 120))

    button4=buttonclass.button(150, 70,230,100)
    button4.draw(main_screen)
    button4.button_su.fill((205, 92, 92))
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render("Travel guide", 1, (11,206,7))

    main_screen.blit(label, (260, 120))
    
    while True: 
        ev = pygame.event.poll()
       
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = ev.pos
            # if button_rec.collidepoint(x, y):
                # print "you clicked me!"
        pygame.display.flip()
    
