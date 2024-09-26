import pygame
from pygame import mixer 
import os
from pygame.locals import *  
from time import sleep
import random
import math

    
class Game:
   





    def __init__(self):
        self.randomsound = ["cash1.mp3","cash2.mp3","cash3.mp3"]
        self.colorlist = ["#FFA07A", "#FF8C00", "#FF6347", "#FF7F50", "#FFB347", "#E9967A", "#F08080", "#FFA500", "#FF4500", "#FF7043", "#FF6F00", "#FF9E80", "#FFA07A", "#FF8C00", "#FF6347", "#FF7F50", "#FFB347", "#E9967A", "#F08080", "#FFA500", "#FF4500", "#FF7043", "#FF6F00", "#FF9E80", "#FFA07A", "#FF8C00", "#FF6347", "#FF7F50", "#FFB347", "#E9967A", "#F08080", "#FFA500", "#FF4500", "#FF7043"]
        self.cookies = 0
        self.cookie_per_click = 1
        self.cookie = pygame.Rect(950 - 150,400 - 150,300,300)
        self.clicked = False
        self.cookie_color = "#9A3334"
        self.costume_immage = pygame.image.load('fidesz.png')
        self.onCokkie = False
        self.python = pygame.image.load('fidesz.png')
        self.cooinnumb = 10

    def drawotp(self):
        self.python = pygame.image.load('fidesz.png')
        screen.blit(self.python, (650,120))
    
    def textfidesz(self):
        self.maintxt = text_font.render("Fidesz  Clicker","True","black")
        screen.blit(self.maintxt, (400,500))

        
    def draw_score(self):
        self.maintxt = text_font.render("Közpénz  Clicker","True","black")  
        screen.blit(self.maintxt, (800,100))

        if self.cookies < 10:
            self.display_cookies = text_font.render(f"Közpénz score: {str(self.cookies)}","True","purple")
            screen.blit(self.display_cookies, (10,100))
        if self.cookies >= 10:
            self.display_cookies = text_font.render(f"Közpénz score: {str(self.cookies)}","True","#654520")
            screen.blit(self.display_cookies, (10,100))
        if self.cookies >= 50:
            self.display_cookies = text_font.render(f"Közpénz score: {str(self.cookies)}","True","#825B32")
            screen.blit(self.display_cookies, (10,100))
        if self.cookies >= 100:
            self.display_cookies = text_font.render(f"Közpénz score: {str(self.cookies)}","True","#F05A7E")
            screen.blit(self.display_cookies, (10,100))
        if self.cookies >= 500:
            self.display_cookies = text_font.render(f"Közpénz score: {str(self.cookies)}","True","#D91656")
            screen.blit(self.display_cookies, (10,100))
    

    def playsounds(self,soundpath,channel,volume):
        mixer.init()
        mixer.Channel(channel).play(pygame.mixer.Sound(soundpath))
        mixer.Channel(channel).set_volume(volume)

    def displaycoins(self,x,y,unit):
        for a in range(unit):
            screen.blit(pygame.image.load('coin.png'), (x,y + a * 100))


    def moneyonscreen(self):
        if self.cookies <= self.cooinnumb * 10:
            unit = self.cooinnumb - math.floor(self.cookies / 10)
            self.displaycoins(1800,0,unit)
            if self.cookies % 10 == 9 and self.cookies > 0:
                self.isplayingsound = True
                self.playsounds("kozpenz.mp3",1,0.4)


    def bacgkround(self):
        self.background = pygame.image.load('idk.jpeg')
        screen.blit(self.background, (0,0))

    def click_button(self):
        self.onCokkie = False
        self.mouse_pos = pygame.mouse.get_pos()
        if self.cookie.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
                
            else:
                if self.clicked:
                    self.cookies += 1
                    self.clicked = False
                    self.cookie_color = random.choice(self.colorlist)
                    self.playsounds(random.choice(self.randomsound),0,0.1) #annyonig game sound


            self.onCokkie = True
                    

        else: 
            self.cookie_color = "#f6871f"
            
            
        pygame.draw.rect(screen,self.cookie_color,self.cookie,border_radius=150)

    def render(self):
        
        self.textfidesz()
        self.bacgkround()
        self.moneyonscreen()
        self.draw_score()
        self.click_button()
        
        self.drawotp()

pygame.init()
widt = 1920
height = 1820

game = Game()

fs = pygame.RESIZABLE
screen = pygame.display.set_mode((widt, height), fs)
pygame.display.set_caption("OTP Clicker")
clock = pygame.time.Clock()
text_font = pygame.font.Font(None,50)
title = text_font.render("OTP Clicker",True,"orange")
keeeys = pygame.key.get_pressed()

while True:
    
    
    
    
    #screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(title, (850,90))
   
    
    game.render()
    pygame.display.update()
    clock.tick(600) 