import pygame,sys

class Scene():
    def __init__(self,window,fonts,wm):
        self.title = 'Press Space To Start'
        self.backgroundMusic = ""
        self.maxtime = -1
        self.w = window
        self.f = fonts
        self.wm = wm
        
    def render(self):
        self.w.fill(pygame.Color(235,124,42))
        title = self.f['xl'].render(self.title,1,(255,255,255))
        self.w.blit(title,self.wm.center(title))
        for e in pygame.event.get():
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_SPACE:
                    return "main"
                if e.key == pygame.K_ESCAPE:
                    sys.exit(2)
            if e.type == pygame.QUIT:
                sys.exit(1)
        return True
