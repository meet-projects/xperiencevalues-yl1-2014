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
    main_screen.blit(label, (160, 180))
    
    



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
    button2=buttonclass.button(115, 70,300,100)
    button2.draw(main_screen)
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render("Equality", 1, (11,206,7))
    main_screen.blit(label, (330, 120))
    global button3
    button3=buttonclass.button(115, 70,165,240)
    button3.draw(main_screen)
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render("Team work", 1, (11,206,7))
    main_screen.blit(label, (180, 265))
    global finishb
    finishb=buttonclass.button(100,50,320,320)
    finishb.draw(main_screen)
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render("Finish", 1, (11,206,7))
    main_screen.blit(label, (340, 340))

def equality(main_screen):
    myfont = pygame.font.SysFont("ComicSansMS", 48)
    label = myfont.render("Equality", 1, (11,46,7))
    main_screen.blit(label, (5, 20))
    global button5
    button5=buttonclass.button(155, 70,25,100)
    button5.draw(main_screen)
    button5.button_su.fill((205, 92, 92))
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render("Work with people ", 1, (11,206,7))
    label2 = myfont.render("from another nationality ", 1, (11,206,7))
    main_screen.blit(label, (28, 120))
    main_screen.blit(label2, (28, 140))
    label3=myfont.render("50$",1,(11,206,7))
    main_screen.blit(label3, (35, 180))
    global button6
    button6=buttonclass.button(150, 70,230,100)
    button6.draw(main_screen)
    button6.button_su.fill((205, 92, 92))
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render("Work with old people", 1, (11,206,7))
    main_screen.blit(label, (240, 120))
    label3=myfont.render("50$",1,(11,206,7))
    main_screen.blit(label3, (250, 180))

def Teamwork(main_screen):
    myfont = pygame.font.SysFont("ComicSansMS", 48)
    label = myfont.render("Lead by example", 1, (11,46,7))
    main_screen.blit(label, (5, 20))
    global button9
    button9=buttonclass.button(155, 70,15,100)
    button9.draw(main_screen)
    button9.button_su.fill((205, 92, 92))
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render("Work with  ", 1, (11,206,7))
    label2 = myfont.render("childern ", 1, (11,206,7))
    main_screen.blit(label, (28, 120))
    main_screen.blit(label2, (28, 140))
    label3 = myfont.render("100$", 1, (11,206,7))
    main_screen.blit(label3, (35, 180))
    global button10
    button10=buttonclass.button(150, 70,230,100)
    button10.draw(main_screen)
    button10.button_su.fill((205, 92, 92))
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render("Travel guide", 1, (11,206,7))
    main_screen.blit(label, (240, 120))
    label3 = myfont.render("100$", 1, (11,206,7))
    main_screen.blit(label3, (260, 180))

def leadbyexample(main_screen):
    myfont = pygame.font.SysFont("ComicSansMS", 48)
    label = myfont.render("Lead by example:", 1, (11,46,7))
    main_screen.blit(label, (5, 20))
    global button7
    button7=buttonclass.button(155, 70,15,100)
    button7.draw(main_screen)
    button7.button_su.fill((205, 92, 92))
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render("Work with  ", 1, (11,206,7))
    label2 = myfont.render("childern ", 1, (11,206,7))
    main_screen.blit(label, (28, 120))
    main_screen.blit(label2, (28, 140))
    label3 = myfont.render("75$", 1, (11,206,7))
    main_screen.blit(label3, (35, 180))
    global button8
    button8=buttonclass.button(150, 70,230,100)
    button8.draw(main_screen)
    button8.button_su.fill((205, 92, 92))
    myfont = pygame.font.SysFont("ComicSansMS", 18)
    label = myfont.render("Travel guide", 1, (11,206,7))
    main_screen.blit(label, (240, 120))
    label3 = myfont.render("75$", 1, (11,206,7))
    main_screen.blit(label3, (260, 180))


if __name__=="__main__":
    pygame.init()
    main_screen = pygame.display.set_mode((430, 400))
    main_screen.fill((255,255,255))
    XperienceValues(main_screen)
    screenname="main"
    global backbutton
    backbutton=buttonclass.button(50,50,15,340)

    price = 0


    while True: 
        ev = pygame.event.poll()
       
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = ev.pos
            if valuesbutton.button_rec.collidepoint(x, y):
                screenname="mainvalues"
                values(main_screen)
            if screenname=="mainvalues":
                if button.button_rec.collidepoint(x, y):
                    main_screen.fill((255,255,255))
                    backbutton=buttonclass.button(50,50,15,340)
                    backbutton.draw(main_screen)
                    myfont = pygame.font.SysFont("ComicSansMS", 18)
                    label = myfont.render(" Back", 1, (11,206,7))
                    main_screen.blit(label, (20, 350))
                    leadbyexample(main_screen)
                    screenname="example"
                if button2.button_rec.collidepoint(x, y):
                    main_screen.fill((255,255,255))
                    myfont = pygame.font.SysFont("ComicSansMS", 30)
                    backbutton.draw(main_screen)
                    myfont = pygame.font.SysFont("ComicSansMS", 18)
                    label = myfont.render(" Back", 1, (11,206,7))
                    main_screen.blit(label, (20, 350))
                    equality(main_screen)
                    screenname="Equality"
                if button3.button_rec.collidepoint(x, y):
                    main_screen.fill((250,250,250))
                    myfont = pygame.font.SysFont("ComicSansMS", 30)
                    backbutton.draw(main_screen)
                    myfont = pygame.font.SysFont("ComicSansMS", 18)
                    label = myfont.render(" Back", 1, (11,206,7))
                    main_screen.blit(label, (20, 350))
                    Teamwork(main_screen)
                    screenname="Team work"
                if finishb.button_rec.collidepoint(x,y):
                    main_screen.fill((250,250,250))
                    myfont = pygame.font.SysFont("ComicSansMS", 80)
                    label = myfont.render("Price: "+str(price)+"$", 1, (11,206,7))
                    main_screen.blit(label, (75, 150))
            elif screenname=="example" or screenname=="Team work" or screenname=="Equality":
                if screenname=="Equality":
                    if button5.button_rec.collidepoint(x,y) or button6.button_rec.collidepoint(x,y):
                        price+=50
                        print price
                        print screenname
                if screenname=="example":
                    if button7.button_rec.collidepoint(x,y) or button8.button_rec.collidepoint(x,y):
                        price+=75
                        print price
                        print screenname
                if screenname=="Team work":
                    if button9.button_rec.collidepoint(x,y) or button10.button_rec.collidepoint(x,y):
                        price+=100
                        print price  
                        print screenname    


                if backbutton.button_rec.collidepoint(x, y):
                    values(main_screen)
                    screenname="mainvalues"
          
        pygame.display.flip()
    
