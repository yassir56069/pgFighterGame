import pygame as pg
import orjson


from object import object
from screen import screen

class fighter(object):

    _fighterList = []

    def __init__(self, config="", img="",  show:bool = True, coord:tuple = (0,0), size= (80,180) ) -> None:
        """the fighter class represents the playable fighter character pygame objects

        Args:
            img (str, optional): The image of the fighter. Defaults to "".
            show (bool, optional): Whether to show the object or not. Defaults to "" (True).
            coord (tuple, optional): The coordinates of the object's initial position. Defaults to (0,0).
            size (tuple, optional): The size of the object in question. Defaults to (80,180).
        """
        super().__init__(img, show)
        
        self.x = coord[0]
        self.y = coord[1]
        self.dx = self.dy = self.vel_y = 0
            

        if config: 
           self.speed, self.jumpVal, self.gravity, self.health = readConfigJSON(config)
        else:
            self.speed        = 3
            self.jumpVal      = 6
            self.gravity      = 1
            self.health       = 100
        

        self.jump = False
        self.isAttacking = False


        self.WIDTH  = size[0]
        self.HEIGHT = size[1]

        self.rect = pg.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)

        fighter._fighterList.append(self)

    def draw(self, screen: screen, scale=True, coord=(0,0)):
        """Draw the fighter to the game screen [Overwirtes the object function]

        Args:
            screen (screen): Game screen object
            scale (bool, optional): Whether to scale the object or not. Defaults to True.
            coord (tuple, optional): The coordinates of the of the object to . Defaults to (0,0).
        """

        if self.img == "": pg.draw.rect(screen.SCREEN, (255,0,0), self.rect)
        else: super().draw(screen, scale, coord)

        self.rect.x += self.dx
        self.rect.y += self.dy

    def drawAtk(self, screen:screen, target):
        self.atkRect = pg.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)

        if self.atkRect.colliderect(target.rect):
            color = (255,0,0)
            target.health -= 10
        else:
            color = (0,255,0)

        pg.draw.rect(screen.SCREEN, color, self.atkRect)
        self.isAttacking = False

    #region Getters and Setters

        @property 
        def dx(self): return self._dx
            
        @dx.setter
        def dx(self, c:float): self._dx = c
        
        @dx.deleter 
        def dx(self): del self._dx
                        
        @property 
        def dy(self): return self._dy
            
        @dy.setter
        def dy(self, c:float): self._dy = c
        
        @dy.deleter 
        def dy(self): del self._dy

        @property 
        def vel_y(self): return self._vel_y
            
        @vel_y.setter
        def vel_y(self, c:float): self._vel_y = c
        
        @vel_y.deleter 
        def vel_y(self): del self._vel_y
        
        @property 
        def isAttacking(self): return self._isAttacking
            
        @vel_y.setter
        def vel_y(self, b:bool): self._isAttacking = b
        
        @vel_y.deleter 
        def vel_y(self): del self._isAttacking

    #endregion
    
    def getFighterList(): 
        return fighter._fighterList


def readConfigJSON(config):
    """Read a config JSON file for character values

    Args:
        config (_type_): the relative path to the config file to read

    Returns:
        integer values for the parameters that were given (speed, jump height and gravity strength)
    """
    with open(config, "r") as f:
        data = orjson.loads(f.read())

        speed   = int(data["speed"])
        jump    = int(data["jump"])
        gravity = int(data["gravity"])
        health  = int(data["health"])

    print(f"s: {speed} j: {jump} g: {gravity}")

    return speed, jump, gravity, health