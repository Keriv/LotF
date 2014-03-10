import pygame,time,sys,datetime

class Manager():
    def __init__(self,size,fonts,window):
        self.width = size[0]
        self.height = size[1]
        self.f = fonts
        self.window = window
        
    def center(self,object):
        a,a,w,h = object.get_rect()
        return ((self.width / 2) - (w / 2),(self.height / 2) - (h / 2))
        
    def blit_alpha(self,target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)
        
    def drawmenu(self,index,title,items,scene):
        scene.render(keys = False,story = False,eventOveride = True)
        longest = 0
        tallest = 0
        space = 100
        lis = []
        title = self.f['xl'].render(title,1,(255,255,255))
        a,a,tw,th = title.get_rect()
        tsurface = pygame.Surface([tw+50,th]).convert()
        tsurface.fill(pygame.Color(0,0,0))
        for e in items:
            text = self.f['l'].render(e,1,(255,255,255))
            lis.append(text)
            a,a,w,h = text.get_rect()
            if h > tallest:
                tallest = h
            if w > longest:
                longest = w
        totalh = (tallest * len(lis)) + (space * (len(lis) - 1))
        surface = pygame.Surface([longest+200,totalh]).convert()    
        surface.fill(pygame.Color(0,0,0))    
        a,a,w,a = surface.get_rect()
        self.blit_alpha(self.window,surface,self.center(surface),150)
        y = space / 2
        for l in lis:
            a,a,w,a = l.get_rect()
            self.window.blit(l,(((self.width / 2)-(w / 2)),(self.height / 2) - (totalh / 2) + y))
            y += space
        pygame.draw.circle(self.window,pygame.Color(255,255,255),(
                (self.width / 2)-(longest / 2)-50,
                (self.height / 2) - (totalh / 2) + (((space*(index+1)) - (space / 2)) + (tallest / 2))
            ),10)
        self.blit_alpha(self.window,tsurface,(self.center(tsurface)[0],(self.height / 2) - (totalh / 2) - 100 - (th / 2)),150)
        self.window.blit(title,(
            self.center(title)[0],
            (self.height / 2) - (totalh / 2) - 100 - (th / 2)))
        pygame.display.update()
        
    def menu(self,title,items,scene):
        index = 0
        display = True
        pygame.event.clear()
        while display == True:
            self.drawmenu(index,title,items,scene)
            for e in pygame.event.get():
                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_s or e.key == pygame.K_DOWN:
                        if index != (len(items) - 1):
                            index += 1
                    if e.key == pygame.K_w or e.key == pygame.K_UP:
                        if index != 0:
                            index -= 1
                    if e.key == pygame.K_RETURN or e.key == pygame.K_KP_ENTER:
                        return index
                        display = False
                    if e.key == pygame.K_ESCAPE:
                        return None
                if e.type == pygame.QUIT:
                    sys.exit(1)
       
    def Timestamp(self):
        return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000) 
            
    def dialog(self,message,time,scene):
        start = self.Timestamp()
        while self.Timestamp() - start < time:
            scene.render(keys = True,story = False)
            title = self.f['xl'].render(message,1,(255,255,255))
            a,a,tw,th = title.get_rect()
            tsurface = pygame.Surface([self.width,th + 50]).convert()
            tsurface.fill(pygame.Color(0,0,0))
            self.blit_alpha(self.window,tsurface,(self.center(tsurface)[0],(self.height) - (th + 50)),150)
            self.window.blit(title,(
                self.center(title)[0],
                (self.height) - (th + 50) + ((th + 50) / 2) - (th / 2)
            ))
            pygame.display.update()
