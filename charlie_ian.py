# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:24:19 2024

@author: ikowa
"""

import pygame, simpleGE, random

class Charlie(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(25,25)
        self.position = (320,400)
        self.moveSpeed = 5 
        
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
  
class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Coin.png")
        self.setSize(25,25)
        self.minSpeed= 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed,self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("headshot.jpg")
        #self.sndCoin = simpleGE.Sound("coin.wav")
        self.numCoins = 10
        self.charlie = Charlie(self)
        self.coins = []
        for i in range(self.numCoins):
            self.coins.append(Coin(self))
            
        self.sprites = [self.charlie,
                        self.coins]
        
    def process(self):
        for coin in self.coins:
            """
            if self.charlie.collidesWith(self.coin):
                self.sndCoin.play()
                self.coin.reset()
            """
            if coin.collidesWith(self.charlie):
                coin.reset()
                #self.sndCoin.play()
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()