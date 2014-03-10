import pygame,os,sys,time

class Scene():
    def __init__(self):
        self.screen = {'size':[int(each) for each in raw_input("Resolution: ").split('x')]}
        pygame.init()
        self.w = pygame.display.set_mode(self.screen['size'],pygame.FULLSCREEN)
        self.maxtime = -1
        self.p = {'pos':[1,5]}
        self.OLDSIZE = [0,0]
        self.map = []
        self.fmap = []
        self.bos = 30
        self.font = pygame.font.SysFont('monospace',48)
        self.showFoliage = True
        self.newTex = "s"
        with open('data/terrain.md') as mapdata:
            for l in mapdata.read().split("\n"):
                row = []
                for x in l.split(' '):
                    row.append(x)
                self.map.append(row)
            self.map = self.map[0:len(self.map)-1]
        self.startx = 0
        self.starty = 0
        self.block = float(self.screen['size'][0]) / float(len(self.map[0]))
        self.bh = self.screen['size'][1] / self.block
    def saveTile(self,x,y,newt):
        if newt in ['r','grass','t','f','n']:
            path = "data/foliage.md"
            m = self.fmap
        else:
            path = "data/terrain.md"
            m = self.map
        if newt == "r":
            if self.fmap[y][x] == "r":
                newt = "x"
            elif self.fmap[y][x] == "x":
                newt = "z"
            elif self.fmap[y][x] == "z":
                newt = "r"
            else:
                newt = "x"
        elif newt == "grass":
            if self.fmap[y][x] == "q":
                newt = "w"
            elif self.fmap[y][x] == "w":
                newt = "e"
            elif self.fmap[y][x] == "e":
                newt = "q"
            else:
                newt = "w"
        m[y][x] = newt
        with open(path,'w') as new:
            for y in range(0,len(m)):
                for x in range(0,len(m[0])):
                    new.write(m[y][x])
                    if x != len(m[y]) - 1:
                        new.write(" ")
                if y != len(m):
                    new.write("\n")
    def getTexture(self,i):
        if i == "g":
            return self.grass
        elif i == "s":
            return self.sand
        elif i == "w":
            return self.water
    def render(self):
        self.map = []
        self.fmap = []
        with open('data/terrain.md') as mapdata:
            for l in mapdata.read().split("\n"):
                row = []
                for x in l.split(' '):
                    row.append(x)
                self.map.append(row)
            self.map = self.map[0:len(self.map)-1]
        with open('data/foliage.md') as mapdata:
            for l in mapdata.read().split("\n"):
                row = []
                for x in l.split(' '):
                    row.append(x)
                self.fmap.append(row)
            self.fmap = self.fmap[0:len(self.fmap)-1]

        self.block = self.screen['size'][0] / self.bos
        self.bh = self.screen['size'][1] / self.block

        scenerypath = "textures/scenery/"
        self.water = pygame.image.load(scenerypath+"water.png").convert()
        self.water = pygame.transform.scale(self.water,(self.block,self.block))
        self.grass = pygame.image.load(scenerypath+"grass.png").convert()
        self.grass = pygame.transform.scale(self.grass,(self.block,self.block))
        self.sand = pygame.image.load(scenerypath+"sand.png").convert()
        self.sand = pygame.transform.scale(self.sand,(self.block,self.block))
        self.sandr = pygame.image.load(scenerypath+"water-sand-r.png").convert()
        self.sandr = pygame.transform.scale(self.sandr,(self.block,self.block))
        self.sandt = pygame.image.load(scenerypath+"water-sand-t.png").convert()
        self.sandt = pygame.transform.scale(self.sandt,(self.block,self.block))
        self.sandl = pygame.image.load(scenerypath+"water-sand-l.png").convert()
        self.sandl = pygame.transform.scale(self.sandl,(self.block,self.block))
        self.sandb = pygame.image.load(scenerypath+"water-sand-b.png").convert()
        self.sandb = pygame.transform.scale(self.sandb,(self.block,self.block))
        self.sand1 = pygame.image.load(scenerypath+"water-sand-1.png").convert()
        self.sand1 = pygame.transform.scale(self.sand1,(self.block,self.block))
        self.sand2 = pygame.image.load(scenerypath+"water-sand-2.png").convert()
        self.sand2 = pygame.transform.scale(self.sand2,(self.block,self.block))
        self.sand3 = pygame.image.load(scenerypath+"water-sand-3.png").convert()
        self.sand3 = pygame.transform.scale(self.sand3,(self.block,self.block))
        self.sand4 = pygame.image.load(scenerypath+"water-sand-4.png").convert()
        self.sand4 = pygame.transform.scale(self.sand4,(self.block,self.block))
        self.sandi1 = pygame.image.load(scenerypath+"water-sand-i1.png").convert()
        self.sandi1 = pygame.transform.scale(self.sandi1,(self.block,self.block))
        self.sandi2 = pygame.image.load(scenerypath+"water-sand-i2.png").convert()
        self.sandi2 = pygame.transform.scale(self.sandi2,(self.block,self.block))
        self.sandi3 = pygame.image.load(scenerypath+"water-sand-i3.png").convert()
        self.sandi3 = pygame.transform.scale(self.sandi3,(self.block,self.block))
        self.sandi4 = pygame.image.load(scenerypath+"water-sand-i4.png").convert()
        self.sandi4 = pygame.transform.scale(self.sandi4,(self.block,self.block))

        self.grassm1 = pygame.image.load(scenerypath+"grass/grass1.png").convert()
        self.grassm1 = pygame.transform.scale(self.grassm1,(self.block,self.block))
        self.grassm2 = pygame.image.load(scenerypath+"grass/grass2.png").convert()
        self.grassm2 = pygame.transform.scale(self.grassm2,(self.block,self.block))
        self.grassm3 = pygame.image.load(scenerypath+"grass/grass3.png").convert()
        self.grassm3 = pygame.transform.scale(self.grassm3,(self.block,self.block))

        self.grassr = pygame.image.load(scenerypath+"grass-r.png").convert_alpha()
        self.grassr = pygame.transform.scale(self.grassr,(self.block,self.block))
        self.grasst = pygame.image.load(scenerypath+"grass-t.png").convert_alpha()
        self.grasst = pygame.transform.scale(self.grasst,(self.block,self.block))
        self.grassl = pygame.image.load(scenerypath+"grass-l.png").convert_alpha()
        self.grassl = pygame.transform.scale(self.grassl,(self.block,self.block))
        self.grassb = pygame.image.load(scenerypath+"grass-b.png").convert_alpha()
        self.grassb = pygame.transform.scale(self.grassb,(self.block,self.block))
        self.grass1 = pygame.image.load(scenerypath+"grass-1.png").convert_alpha()
        self.grass1 = pygame.transform.scale(self.grass1,(self.block,self.block))
        self.grass2 = pygame.image.load(scenerypath+"grass-2.png").convert_alpha()
        self.grass2 = pygame.transform.scale(self.grass2,(self.block,self.block))
        self.grass3 = pygame.image.load(scenerypath+"grass-3.png").convert_alpha()
        self.grass3 = pygame.transform.scale(self.grass3,(self.block,self.block))
        self.grass4 = pygame.image.load(scenerypath+"grass-4.png").convert_alpha()
        self.grass4 = pygame.transform.scale(self.grass4,(self.block,self.block))
        self.grassi1 = pygame.image.load(scenerypath+"grass-i1.png").convert_alpha()
        self.grassi1 = pygame.transform.scale(self.grassi1,(self.block,self.block))
        self.grassi2 = pygame.image.load(scenerypath+"grass-i2.png").convert_alpha()
        self.grassi2 = pygame.transform.scale(self.grassi2,(self.block,self.block))
        self.grassi3 = pygame.image.load(scenerypath+"grass-i3.png").convert_alpha()
        self.grassi3 = pygame.transform.scale(self.grassi3,(self.block,self.block))
        self.grassi4 = pygame.image.load(scenerypath+"grass-i4.png").convert_alpha()
        self.grassi4 = pygame.transform.scale(self.grassi4,(self.block,self.block))
        
        self.grass_s = pygame.image.load(scenerypath+"grass-s.png").convert_alpha()
        self.grass_s = pygame.transform.scale(self.grass_s,(self.block,self.block))
        
        self.rock = pygame.image.load("textures/foliage/rocks/rock.png").convert_alpha()
        self.rock = pygame.transform.scale(self.rock,(self.block,self.block))
        self.rock2 = pygame.image.load("textures/foliage/rocks/rock2.png").convert_alpha()
        self.rock2 = pygame.transform.scale(self.rock2,(self.block,self.block))
        self.rock3 = pygame.image.load("textures/foliage/rocks/rock3.png").convert_alpha()
        self.rock3 = pygame.transform.scale(self.rock3,(self.block,self.block))
        
        self.tree = pygame.image.load("textures/foliage/tree.png").convert_alpha()
        self.tree = pygame.transform.scale(self.tree,(self.block*3,int(float(self.block)*3.75)))
        
        self.flower = pygame.image.load("textures/foliage/flower.png").convert_alpha()
        self.flower = pygame.transform.scale(self.flower,(self.block,self.block))
        
        self.tree = pygame.image.load("textures/foliage/tree.png").convert_alpha()
        self.tree = pygame.transform.scale(self.tree,(self.block*3,int(float(self.block)*3.75)))
        
        self.w.fill(pygame.Color(0,0,0))
        for e in pygame.event.get():
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_ESCAPE:
                        sys.exit(2)
                if e.key == pygame.K_w or e.key == pygame.K_UP:
                    if self.starty > 0:
                        if self.bos < 5:
                            self.starty -= 1
                        else:
                            self.starty -= 5
                if e.key == pygame.K_s or e.key == pygame.K_DOWN:
                    if self.bos < 5:
                        self.starty += 1
                    else:
                        self.starty += 5
                if e.key == pygame.K_a or e.key == pygame.K_LEFT:
                    if self.startx > 0:
                        if self.bos < 5:
                            self.startx -= 1
                        else:
                            self.startx -= 5
                if e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                    if self.bos < 5:
                        self.startx += 1
                    else:
                        self.startx += 5
                if e.key == pygame.K_MINUS:
                    if self.bos < 5:
                        self.bos += 1
                    else:
                        self.bos += 5
                if e.key == pygame.K_EQUALS:
                    if self.bos > 5:
                        self.bos -= 5
                    elif self.bos > 1:
                        self.bos -= 1
                if e.key == pygame.K_f:
                    if self.showFoliage:
                        self.showFoliage = False
                    else:
                        self.showFoliage = True
                if e.key == pygame.K_1 or e.key == pygame.K_KP1:
                    self.newTex = "s"
                if e.key == pygame.K_2 or e.key == pygame.K_KP2:
                    self.newTex = "g"
                if e.key == pygame.K_3 or e.key == pygame.K_KP3:
                    self.newTex = "w"
                if e.key == pygame.K_6 or e.key == pygame.K_KP6:
                    self.newTex = "t"
                if e.key == pygame.K_7 or e.key == pygame.K_KP7:
                    self.newTex = "r"
                if e.key == pygame.K_8 or e.key == pygame.K_KP8:
                    self.newTex = "grass"
                if e.key == pygame.K_9 or e.key == pygame.K_KP9:
                    self.newTex = "f"
                if e.key == pygame.K_0 or e.key == pygame.K_KP0:
                    self.newTex = "n"
                
            if e.type == pygame.MOUSEBUTTONUP:
                pos = list(pygame.mouse.get_pos())
                x = (pos[0] / self.block) + (self.startx)
                y = (pos[1] / self.block) + (self.starty)
                self.saveTile(x,y,self.newTex)
            if e.type == pygame.QUIT:
                sys.exit(2)
        startx = self.startx
        starty = self.starty
        for y in range(starty,starty + self.bh + 5):
            for x in range(startx,startx + self.bos + 5):
                try:
                    if self.map[y][x] == "g":
                        tex = self.grass
                        bottom = False
                        top = False
                        left = False
                        right = False
                        br = False
                        bl = False
                        tl = False
                        tr = False
                        try:
                            if y != 0:
                                if self.map[y+1][x] != "g":
                                    top = self.map[y+1][x]
                                if self.map[y-1][x] != "g":
                                    bottom = self.map[y-1][x]
                            if x != 0:
                                if self.map[y][x+1] != "g":
                                    left = self.map[y][x+1]
                                if self.map[y][x-1] != "g":
                                    right = self.map[y][x-1]
                            if x != 0 and y != 0:
                                if self.map[y+1][x+1] != "g":
                                    bl = self.map[y+1][x+1]
                                if self.map[y+1][x-1] != "g":
                                    br = self.map[y+1][x-1]
                                if self.map[y-1][x+1] != "g":
                                    tl = self.map[y-1][x+1]
                                if self.map[y-1][x-1] != "g":
                                    tr = self.map[y-1][x-1]
                            if bottom != False and right == False and left == False and top == False:
                                self.w.blit(self.getTexture(bottom),((x-startx)*self.block,(y-starty)*self.block))
                                tex = self.grassb
                            elif top != False and right == False and left == False and bottom == False:
                                self.w.blit(self.getTexture(top),((x-startx)*self.block,(y-starty)*self.block))
                                tex = self.grasst
                            elif left != False and right == False and bottom == False and top == False:
                                self.w.blit(self.getTexture(left),((x-startx)*self.block,(y-starty)*self.block))
                                tex = self.grassl
                            elif right != False and bottom == False and left == False and top == False:
                                self.w.blit(self.getTexture(right),((x-startx)*self.block,(y-starty)*self.block))
                                tex = self.grassr
                            if bottom != False and right != False and left == False and top == False:
                                self.w.blit(self.getTexture(bottom),((x-startx)*self.block,(y-starty)*self.block))
                                tex = self.grass4
                            elif top != False and right != False and left == False and bottom == False:
                                self.w.blit(self.getTexture(right),((x-startx)*self.block,(y-starty)*self.block))
                                tex = self.grass1
                            elif left != False and right == False and bottom != False and top == False:
                                self.w.blit(self.getTexture(left),((x-startx)*self.block,(y-starty)*self.block))
                                tex = self.grass3
                            elif right == False and bottom == False and left != False and top != False:
                                self.w.blit(self.getTexture(left),((x-startx)*self.block,(y-starty)*self.block))
                                tex = self.grass2
                            if right != False and bottom != False and left != False and top != False:
                                self.w.blit(self.getTexture(right),((x-startx)*self.block,(y-starty)*self.block))
                                tex = self.grass_s
                            if bottom == False and right == False and left == False and top == False and bl != False:
                                self.w.blit(self.getTexture(bl),((x-startx)*self.block,(y-starty)*self.block))
                                tex = self.grassi2
                            elif bottom == False and right == False and left == False and top == False and tl != False:
                                self.w.blit(self.getTexture(tl),((x-startx)*self.block,(y-starty)*self.block))
                                tex = self.grassi3
                            elif bottom == False and right == False and left == False and top == False and br != False:
                                self.w.blit(self.getTexture(br),((x-startx)*self.block,(y-starty)*self.block))
                                tex = self.grassi1
                            elif bottom == False and right == False and left == False and top == False and tr != False:
                                self.w.blit(self.getTexture(tr),((x-startx)*self.block,(y-starty)*self.block))
                                tex = self.grassi4
                        except IndexError:
                            pass
                    if self.map[y][x] == "w":
                        tex = self.water
                    elif self.map[y][x] == "s":
                        tex = self.sand
                        bottom = False
                        top = False
                        left = False
                        right = False
                        br = False
                        bl = False
                        tl = False
                        tr = False
                        try:
                            if y != 0:
                                if self.map[y+1][x] == "w":
                                    top = True
                                if self.map[y-1][x] == "w":
                                    bottom = True
                            if x != 0:
                                if self.map[y][x+1] == "w":
                                    left = True
                                if self.map[y][x-1] == "w":
                                    right = True
                            if x != 0 and y != 0:
                                if self.map[y+1][x+1] == "w":
                                    bl = True
                                if self.map[y+1][x-1] == "w":
                                    br = True
                                if self.map[y-1][x+1] == "w":
                                    tl = True
                                if self.map[y-1][x-1] == "w":
                                    tr = True
                            if bottom == True and right == False and left == False and top == False:
                                tex = self.sandb
                            elif top == True and right == False and left == False and bottom == False:
                                tex = self.sandt
                            elif left == True and right == False and bottom == False and top == False:
                                tex = self.sandl
                            elif right == True and bottom == False and left == False and top == False:
                                tex = self.sandr
                            if bottom == True and right == True and left == False and top == False:
                                tex = self.sand4
                            elif top == True and right == True and left == False and bottom == False:
                                tex = self.sand1
                            elif left == True and right == False and bottom == True and top == False:
                                tex = self.sand3
                            elif right == False and bottom == False and left == True and top == True:
                                tex = self.sand2
                            if bottom == False and right == False and left == False and top == False and bl == True:
                                tex = self.sandi2
                            elif bottom == False and right == False and left == False and top == False and tl == True:
                                tex = self.sandi3
                            elif bottom == False and right == False and left == False and top == False and br == True:
                                tex = self.sandi1
                            elif bottom == False and right == False and left == False and top == False and tr == True:
                                tex = self.sandi4
                            else:
                                text = self.sand
                        except IndexError:
                            pass
                    self.w.blit(tex,((x-startx)*self.block,(y-starty)*self.block))
                    if self.showFoliage == True:
                        if tex == self.grass:
                            if self.fmap[y][x] == "f":
                                self.w.blit(self.flower,((x-startx)*self.block,(y-starty)*self.block))
                            elif self.fmap[y][x] == "r":
                                self.w.blit(self.rock,((x-startx)*self.block,(y-starty)*self.block))
                            elif self.fmap[y][x] == "x":
                                self.w.blit(self.rock2,((x-startx)*self.block,(y-starty)*self.block))
                            elif self.fmap[y][x] == "z":
                                self.w.blit(self.rock3,((x-startx)*self.block,(y-starty)*self.block))
                            elif self.fmap[y][x] == "q":
                                self.w.blit(self.grassm1,((x-startx)*self.block,(y-starty)*self.block))
                            elif self.fmap[y][x] == "w":
                                self.w.blit(self.grassm2,((x-startx)*self.block,(y-starty)*self.block))
                            elif self.fmap[y][x] == "e":
                                self.w.blit(self.grassm3,((x-startx)*self.block,(y-starty)*self.block))
                        if self.fmap[y][x] == "t":
                            self.w.blit(self.tree,(((x-startx)*self.block) - self.block,int(((y-starty)*self.block))-(self.block * 3.75)+(self.block)))
                except IndexError:
                    self.w.blit(self.water,((x-startx)*self.block,(y-starty)*self.block))
        if self.newTex == "r":
            text = self.font.render("Rock",1,(255,255,255))
        elif self.newTex == "w":
            text = self.font.render("Water",1,(255,255,255))
        elif self.newTex == "g":
            text = self.font.render("Grass",1,(255,255,255))
        elif self.newTex == "s":
            text = self.font.render("Sand",1,(255,255,255))
        elif self.newTex == "t":
            text = self.font.render("Tree",1,(255,255,255))
        elif self.newTex == "grass":
            text = self.font.render("Grass Decoration",1,(255,255,255))
        elif self.newTex == "f":
            text = self.font.render("Flower",1,(255,255,255))
        elif self.newTex == "n":
            text = self.font.render("Remove",1,(255,255,255))
        self.w.blit(text,(5,5))
        return True
        
if __name__ == "__main__":
    s = Scene()
    while True:
        s.render()
        pygame.display.flip()
        time.sleep(0.01)
        
