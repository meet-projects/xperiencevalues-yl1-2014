import pygame
import buttonclass

def XperienceValues(main_screen):
    main_screen.fill((255,255,255))
    global myfont
    myfont = pygame.font.SysFont("ComicSansMS", 56)
    global label
    label = myfont.render("X", 1, (11,46,7))
    main_screen.blit(label, (120, 20))
    myfont = pygame.font.SysFont("ComicSansMS", 52)
    label = myfont.render("perience", 1, (11,206,7))
    main_screen.blit(label, (145, 20))
    myfont = pygame.font.SysFont("ComicSansMS", 52)
    label = myfont.render("Values", 1, (11,46,7))
    main_screen.blit(label, (135, 62))
    global valuesbutton
    valuesbutton=buttonclass.button(130, 130,125,140)
    valuesbutton.draw(main_screen)
    myfont = pygame.font.SysFont("ComicSansMS",60)
    label = myfont.render("=>", 1, (11,206,7))
    main_screen.blit(label, (130, 140))
    # global screenname
    
    



def values(main_screen):
    main_screen.fill((255,255,255))
    myfont = pygame.font.SysFont("ComicSansMS", 48)
    label = myfont.render("Pick a value:", 1, (11,46,7))
    main_screen.blit(label, (100, 20))
    global button
    button=buttonclass.button(115, 70,20,100)
    button.draw(main_screen)
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render(" Lead by example", 1, (11,206,7))
    main_screen.blit(label, (22, 120))
    global button2
    button2=buttonclass.button(115, 70,320,100)
    button2.draw(main_screen)
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render("Equality", 1, (11,206,7))
    main_screen.blit(label, (340, 120))
    global button3
    button3=buttonclass.button(115, 70,165,240)
    button3.draw(main_screen)
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render("Team work", 1, (11,206,7))
    main_screen.blit(label, (180, 265))

###########################################################
# def example(main_screen):
#     myfont = pygame.font.SysFont("ComicSansMS", 48)
#     label = myfont.render("Lead by example:", 1, (11,46,7))  
#     main_screen.blit(label, (5, 20))
#     # button3=buttonclass.button(150, 70,20,100)
#     # # button 
#     # button=buttonclass.button(115, 70,20,100)
#     # button.draw(main_screen)
#     # myfont = pygame.font.SysFont("ComicSansMS", 18)
#     # label = myfont.render(" Lead by example", 1, (11,206,7))
#     # main_screen.blit(label, (22, 120))
# # def equality(main_screen):
# #     #button 2
# #     button2=buttonclass.button(100, 70,320,100)
# #     button2.draw(main_screen)
# #     myfont = pygame.font.SysFont("ComicSansMS", 18)
# #     label = myfont.render(" Equality", 1, (11,206,7))
# #     main_screen.blit(label, (340, 120))
#     #button 3
#     button3=buttonclass.button(115, 70,165,240)
#     button3.draw(main_screen)
#     button3.button_su.fill((205, 92, 92))
#     myfont = pygame.font.SysFont("ComicSansMS", 18)
#     label = myfont.render("Working with children", 1, (11,206,7))
#     main_screen.blit(label, (28, 120))
#     button4=buttonclass.button(150, 70,230,100)
#     button4.draw(main_screen)
#     button4.button_su.fill((205, 92, 92))
#     myfont = pygame.font.SysFont("ComicSansMS", 18)
#     label = myfont.render("Travel guide", 1, (11,206,7))
#     label = myfont.render(" Team work", 1, (11,206,7))
#     main_screen.blit(label, (185, 260))
#     screenname=""

if __name__=="__main__":
    pygame.init()
    main_screen = pygame.display.set_mode((430, 400))
    main_screen.fill((255,255,255))
    XperienceValues(main_screen)
    screenname="main"

    # global myfont
    # label = myfont.render("X", 1, (11,46,7))
    # main_screen.blit(label, (260, 120))
    global backbutton
    backbutton=buttonclass.button(50,50,15,340)

    price = []

    while True: 
        ev = pygame.event.poll()
       
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = ev.pos
            if valuesbutton.button_rec.collidepoint(x, y):
                screenname="mainvalues"
                values(main_screen)
            if screenname=="mainvalues":
                if button.button_rec.collidepoint(x, y):
                    main_screen.fill((0,0,0))
                    myfont = pygame.font.SysFont("ComicSansMS", 30)
                    label = myfont.render("You Clicked Button 1", 1, (11,46,7))
                    main_screen.blit(label, (120, 20))
                    screenname="example"
                    backbutton=buttonclass.button(50,50,15,340)
                    backbutton.draw(main_screen)
                    myfont = pygame.font.SysFont("ComicSansMS", 18)
                    label = myfont.render(" Back", 1, (11,206,7))
                    main_screen.blit(label, (20, 350))
                if button2.button_rec.collidepoint(x, y):
                    main_screen.fill((255,255,255))
                    myfont = pygame.font.SysFont("ComicSansMS", 30)
                    label = myfont.render("You Clicked Button 2", 1, (11,46,7))
                    main_screen.blit(label, (120, 20))
                    screenname="Equality"
                    # backbutton=buttonclass.button(50,50,15,340)
                    backbutton.draw(main_screen)
                    myfont = pygame.font.SysFont("ComicSansMS", 18)
                    label = myfont.render(" Back", 1, (11,206,7))
                    main_screen.blit(label, (20, 350))
                if button3.button_rec.collidepoint(x, y):
                    main_screen.fill((50,50,50))
                    myfont = pygame.font.SysFont("ComicSansMS", 30)
                    label = myfont.render("You Clicked Button 3", 1, (11,46,7))
                    main_screen.blit(label, (120, 20))
                    screenname="Team work"
                    # backbutton=buttonclass.button(50,50,15,340)
                    backbutton.draw(main_screen)
                    myfont = pygame.font.SysFont("ComicSansMS", 18)
                    label = myfont.render(" Back", 1, (11,206,7))
                    main_screen.blit(label, (20, 350))
            if screenname=="example" or screenname=="Team work" or screenname=="Equality":
                if backbutton.button_rec.collidepoint(x, y):
                    values(main_screen)
                    screenname="mainvalues"
          
        pygame.display.flip()
    
