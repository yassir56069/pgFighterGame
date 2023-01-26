import pygame as pg

# use dictionaries instead of if statements, put keyboard inputs as values etc, should be easy to do.

from fighter import fighter
from screen import screen

def move_left(obj:fighter):
    """left movement for object

    Args:
        obj (fighter): the object to apply the movement
    """
    obj.dx = -obj.speed

def move_right(obj:fighter):
    """right movement for object

    Args:
        obj (fighter): the object to apply the movement
    """
    obj.dx = obj.speed

def move_jump(obj:fighter): 
    """jump movement for object

    Args:
        obj (fighter): the object to apply the movement
    """
    if obj.jump == False:
        obj.jump = True
        obj.vel_y = -obj.jumpVal

def attack_1(obj:fighter):
    obj.isAttacking = True

def attack_2(obj:fighter):
    obj.isAttacking = True

def stop(obj:fighter):
    obj.dx = 0

class keyboard:

    def __init__(self) -> None:
        """The keyboard object deals with filtering and processing keyboard inputs using pygame
        """
        self.key = pg.key.get_pressed()
        
        # The input dictionary sets the inputs for what each movement to be processed. 
        # The default is the AD Control scheme below 
        self.inputs = {
            pg.K_a: move_left, 
            pg.K_d: move_right,
            pg.K_w: move_jump, 
        } 

    def borderEx(self, screen:screen, *obj:fighter ) -> None:
        """Sets the exception preventing objects going past the game screen.

        Args:
            screen (screen): The screen object for the game
            obj (fighter): the objects to obey the exception
        """
        for o in obj:
            if o.rect.left  + o.dx < 0:
                o.dx = -o.rect.left
            
            if o.rect.right + o.dx > screen.WIDTH:
                o.dx = screen.WIDTH - o.rect.right
            
            if o.rect.bottom + o.dy > screen.HEIGHT - 110:
                o.vel_y = 0
                o.dy = screen.HEIGHT - 110 - o.rect.bottom
                o.jump = False
    
    def jumpEx(self, *obj:fighter) -> None:
        """Sets the exception making objects obey their gravity variable

        Args:
            obj (fighter): the objects to obey the exception
        """
        for o in obj:
            if o.jump:
                o.vel_y += o.gravity                
                o.dy += o.vel_y

    def set_move_AD(self):
        inputs = {
            pg.K_a: move_left,
            pg.K_d: move_right,
            pg.K_w: move_jump,
            pg.K_r: attack_1,
            pg.K_t: attack_2
        }

        return inputs

    def set_move_AK(self):
        inputs = {
            pg.K_LEFT: move_left,
            pg.K_RIGHT: move_right,
            pg.K_UP: move_jump,
            pg.K_k: attack_1,
            pg.K_l: attack_2
        }

        return inputs

    def move(self, event, obj:fighter, inputs:dict) -> None:
        """Set object inputs to the Arrow Keys control scheme

        Args:
            event (_type_): pygame event object
            obj (fighter): object to use control scheme
        """
     
        if event.type == pg.KEYDOWN:
                if not (obj.isAttacking):
                    try:
                        inputs[event.key](obj)

                    except KeyError:
                        pass

        if event.type == pg.KEYUP:
            stop(obj)
