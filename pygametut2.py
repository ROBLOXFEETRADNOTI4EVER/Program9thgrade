import pygame
import os
from pygame.locals import *



    
class Game:
   





    def __init__(self):
        self.cookies = 0
        self.cookie_per_click = 1
        self.cookie = pygame.Rect(950 - 150,400 - 150,300,300)
        self.clicked = False
        self.cookie_color = "#9A3334"
        self.costume_immage = pygame.image.load('fidesz.png')
        self.onCokkie = False
        self.python = pygame.image.load('fidesz.png')

    def drawotp(self):
        self.python = pygame.image.load('fidesz.png')
        screen.blit(self.python, (650,120))
    
    def textfidesz(self):
        self.maintxt = text_font.render("Fidesz  Clicker","True","black")
        screen.blit(self.maintxt, (400,500))

        
    def draw_score(self):
        if self.cookies >= 10:
            self.display_cookies = text_font.render(f"Fidesz score: {str(self.cookies)}","True","#507642")
            screen.blit(self.display_cookies, (10,100))
        if self.cookies < 10:
            self.display_cookies = text_font.render(f"Fidesz score: {str(self.cookies)}","True","purple")
            screen.blit(self.display_cookies, (10,100))

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



            self.onCokkie = True
            self.cookie_color = "#985815"
        else: 
            self.cookie_color = "#f6871f"
            print("notcolliding")
            
        pygame.draw.rect(screen,self.cookie_color,self.cookie,border_radius=150)

    def render(self):
        self.textfidesz()
        self.bacgkround()
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