import pygame
import os,importlib,time,sys

from scenes import title,main
from libraries import windowManager


screen = {'size':[int(each) for each in raw_input("Resolution: ").split('x')]}
cs = 'title'
xf = 0

pygame.init()
window = pygame.display.set_mode(screen['size'],pygame.FULLSCREEN)


fonts = {'s':pygame.font.SysFont('monospace',14),'m':pygame.font.SysFont('monospace',26),'l':pygame.font.SysFont('monospace',48),'xl':pygame.font.SysFont('monospace',62)}
wm = windowManager.Manager(screen['size'],fonts,window)
scenes = {'title':title.Scene(window,fonts,wm),'main':main.Scene(window,fonts,wm)}

go = True
while go:
    out = scenes[cs].render()
    if type(out) == str:
        cs = out
    pygame.display.update()
    #time.sleep(0.01)
    xf += 1
