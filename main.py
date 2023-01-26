import pygame as pg
import sys

from screen     import screen
from kb         import keyboard
from object     import object
from fighter    import fighter

def run_game(screen:screen, running = True):

    def loop(*obj:object):
        while running:
            screen.tick()
            # create keyboard instance and catch key presses
            kb = keyboard() 

            for event in pg.event.get():
                if event.type == pg.QUIT: sys.exit()
                
                kb.move(event, f1, kb.set_move_AD())
                kb.move(event, f2, kb.set_move_AK())

            kb.borderEx(screen, *fighter.getFighterList())
            kb.jumpEx(*fighter.getFighterList())



            for o in obj:
                if o.show == True:
                    o.draw(screen)

            if f1.isAttacking:
                f1.drawAtk(screen, f2)

            if f2.isAttacking:
                f2.drawAtk(screen, f1)

            screen.draw_healthBar(f1.health, 20, 20)            
            screen.draw_healthBar(f2.health, 580, 20)


            pg.display.update()

    # objects
    background  = object('assets//images//background//background.jpg')
    f1          = fighter(config='assets//chara//fighter1.json', coord=(200,310))
    f2          = fighter(config='assets//chara//fighter2.json', coord=(700,310))


    loop(*object.getObjList())     # loop wrapper
    pg.quit()                      # kill pygame after exit

def main():
    #initialize pygame
    pg.init()

    #setup game screen
    fscreen = screen( (1000,600), color=(205,200,0), caption="Fighting Game", fps=60)

    #game loop
    run_game(fscreen)

if __name__ == "__main__":
    main()
