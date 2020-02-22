import pygame
import threading
import sys
from math import *

pygame.init()
screen=pygame.display.set_mode((1000,500))
pygame.display.set_caption('move')
bg=(255,255,255)
clock=pygame.time.Clock()

class fig():
    def __init__(self,screen,clock):
        self.screen=screen
        self.clock=clock
        self.screen_rect=self.screen.get_rect()
        self.move=False
        self.load_img('front.png')
        self.rect=self.image.get_rect()
        
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery
        
        self.count=0
    def load_img(self,img):
        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(self.image,(50,75))
    def flip(self):
        self.image=pygame.transform.flip(self.image,True,False)
    def movetomouse(self,x,y):
        self.x=float(self.rect.centerx)
        self.y=float(self.rect.bottom)
        
        self.dx=fabs(x-self.x)
        self.dy=fabs(y-self.y)
        
        self.txy=self.dx+self.dy
        
        try:
            self.rx=self.dx/self.txy
            self.ry=self.dy/self.txy
        except ZeroDivisionError:
            self.rx=1
            self.ry=1
        self.sx=self.rx*300
        self.sy=self.ry*300
        
        TbT=self.clock.get_time()
        s=TbT/1000
        
        self.mx=s*self.sx
        self.my=s*self.sy
        
        if self.x<x:
            self.x+=self.mx
        if self.x>x:
            self.x-=self.mx
        if self.y>y:
            self.y-=self.my
        if self.y<y:
            self.y+=self.my
        if self.dx<10 and self.dy<10:
            self.x=x
            self.y=y
            self.move=False
            self.load_img('front.png')
        self.rect.centerx=self.x
        self.rect.bottom=self.y
    def blitme(self):
        self.screen.blit(self.image,self.rect)

def mpos():
    x,y=pygame.mouse.get_pos()
    return [x,y]

ID=pygame.USEREVENT+1
pygame.time.set_timer(ID,300)

f=fig(screen,clock)
get_pos=False
check_pos=False
images=['front.png','side.png']

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            f.count=0
            check_pos=True
            f.move=True    
            get_pos=True
            f.flip()
        if event.type==pygame.MOUSEBUTTONUP:
            get_pos=False
            check_pos=False
        if event.type==ID and f.move:
            f.flip()
    if check_pos:
        check=mpos()
    if get_pos:
        if check[1]<150:
            y=75
            if check[0]>=975:
                x=975
            elif check[0]<=25:
                x=25
            else:
                x=mpos()[0]
        elif check[0]>=975:
            x=975
            y=mpos()[1]
        elif check[0]<=25:
            x=25
            y=mpos()[1]
        else:
            x=mpos()[0]
            y=mpos()[1]
    if f.move:
        f.count+=1
        if f.count==1:
            f.load_img('side.png')
        f.movetomouse(x,y)
        
    screen.fill(bg)
    f.blitme()
    pygame.display.flip()
