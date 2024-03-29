# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:35:34 2024

@author: ikowa
"""

import simpleGE, pygame
"""
class Charlie(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")

        self.setSize(50,50)
        self.position = (320, 400)
        self.moveSpeed = 5
"""
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("headshot.jpg")
        #self.charlie = Charlie(self)
    
        #self.sprites = [self.charlie]
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()