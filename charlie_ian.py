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
        if self.isKeyPressed(pygame.K_UP):
            self.y -= self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.moveSpeed
            """
            while keepGoing:
                if self.y == 316:
                    while keepGoing:
                        if self.y < 320:
                            self.y += 1
                        else: 
                            keepGoing = False
                            
                            while keepGoing:
                                if self.y > 315:
                                    self.y -= 1
                                else:
                                    keepGoing = False
                     # I was initially trying to make charlie "jump". Couldn't get it to work'
            """
                        
                    
           
            """
            while keepGoing:
                if self.y == 315:
                    self.y -= self.moveSpeed
                elif self.y > 315:
                    self.y -= self.moveSpeed
                else:
                    
                    keepGoing = False
            """
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
class Hurt(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("hurtCharlie.png")
        self.setSize(25,25)
        self.minSpeed= 5
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
        self.setImage("backgroundV1.png")
        self.sndCoin = simpleGE.Sound("pickupCoin.wav")
        self.sndHurt = simpleGE.Sound("hurtNoise.wav")
        self.numCoins = 10
        self.numHurt = 4
        self.charlie = Charlie(self)
        self.coins = []
        self.hurts = []
        for i in range(self.numCoins):
            self.coins.append(Coin(self))
        for i in range(self.numHurt):
            self.hurts.append(Hurt(self))
        self.sprites = [self.charlie,
                        self.coins,
                        self.hurts]
        
    def process(self):
        for coin in self.coins:
            """
            if self.charlie.collidesWith(self.coin):
                self.sndCoin.play()
                self.coin.reset()
            """
            if coin.collidesWith(self.charlie):
                coin.reset()
                self.sndCoin.play()
        for hurt in self.hurts:
            
            if hurt.collidesWith(self.charlie):
                hurt.reset()
                self.sndHurt.play()
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()