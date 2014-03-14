import pygame,os,sys,platform,time,datetime
import json
from random import randrange

LINUXPATH = os.path.expanduser('~')+"/.lotf.save"
WINDOWSPATH = os.path.expanduser('~/lotf.save')

class Scene():
    def __init__(self,window,fonts,wm):
        self.title = 'Main Game!'
        self.backgroundMusic = ""
        self.maxtime = -1
        self.w = window
        self.f = fonts
        self.wm = wm
        self.p = {'pos':[6,10],'stage':0,'inventory':{}}
        self.piggy = {'pos':[6,4]}
        self.fmap = []
        self.map = []
        self.bos = 30
        self.oldStage = -1
        self.oldSeq = -1
        self.block = wm.width / self.bos
        self.bh = wm.height / self.block
        
        scenerypath = "textures/scenery/"
        
        self.water = pygame.image.load(scenerypath+"water.png").convert()
        self.water = pygame.transform.scale(self.water,(self.block,self.block))
        
        self.grass = pygame.image.load(scenerypath+"grass.png").convert()
        self.grass = pygame.transform.scale(self.grass,(self.block,self.block))
        
        self.grassm1 = pygame.image.load(scenerypath+"grass/grass1.png").convert()
        self.grassm1 = pygame.transform.scale(self.grassm1,(self.block,self.block))
        self.grassm2 = pygame.image.load(scenerypath+"grass/grass2.png").convert()
        self.grassm2 = pygame.transform.scale(self.grassm2,(self.block,self.block))
        self.grassm3 = pygame.image.load(scenerypath+"grass/grass3.png").convert()
        self.grassm3 = pygame.transform.scale(self.grassm3,(self.block,self.block))
        
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
        
        self.grass_s = pygame.image.load(scenerypath+"grass-s.png").convert_alpha()
        self.grass_s = pygame.transform.scale(self.grass_s,(self.block,self.block))
        
        self.ralphT = pygame.image.load("textures/people/ralph/front.png").convert_alpha()
        self.ralphT = pygame.transform.scale(self.ralphT,(self.block,self.block))
        self.piggyT = pygame.image.load("textures/people/piggy/front.png").convert_alpha()
        self.piggyT = pygame.transform.scale(self.piggyT,(self.block,self.block))
        
        self.items = {}
        
        self.story = self.loadJ("data/main.sd")
        
        for item in os.listdir("items/"):
            if "~" not in item:
                data = self.loadJ("items/"+item)
                self.texture = pygame.image.load("textures/items/"+data['texture']).convert()
                self.texture = pygame.transform.scale(self.texture,(self.block,self.block))
                self.items[data['name']] = [data,self.texture]
                
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
      
        self.load()
        
        try:
            self.cstage = self.p['stage']
        except:
            self.cstage = 0
            self.p['stage'] = 0
        self.cseq = 0
        
    def getSavePath(self):
        if platform.system().lower() == "linux":
            path = LINUXPATH
        elif platform.system().lower() == "windows":
            path = WINDOWSPATH
        return path
        
    def save(self):
        path = self.getSavePath()
        with open(path, 'w') as outfile:
            data = {"player":self.p,"piggy":self.piggy}    
            json.dump(data, outfile)
            
    def loadJ(self,path):
        with open(path) as outfile:   
            data = json.load(outfile)
        return data
        
    def load(self):
        path = self.getSavePath()
        if os.path.exists(path):
            data = self.loadJ(path)
            self.p = data['player']
            self.piggy = data['piggy']
            if "inventory" not in self.p:
                self.p['inventory'] = {}
            
    def quit(self,code):
        self.save()
        sys.exit(code)
       
    def getTexture(self,i):
        if i == "g":
            return self.grass
        elif i == "s":
            return self.sand
        elif i == "w":
            return self.water
        
    def Timestamp(self):
        return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000) 
        
    def render(self,keys = True,canMove = True,story = True,eventOveride = False):
        self.w.fill(pygame.Color(0,0,0))
        if story:
            if self.cstage != self.oldStage:
                self.cseq = 0
                self.oldStage = self.cstage
            if self.cseq != self.oldSeq:
                if self.cseq == 0 and self.cstage == 0:
                    self.p['pos'] = [6,10]
                if self.cseq == len(self.story[self.cstage]['sequence']):
                    self.cstage += 1
                    self.oldStage = self.cstage
                    self.p['stage'] = self.cstage
                    self.cseq = 0
                self.oldSeq = self.cseq
                data = self.story[self.cstage]['sequence'][self.cseq]
                setype = data['type']
                if setype == "dialog":
                    print "DIALOG"
                    if "from" in data:
                        text = data['from'].title() + ": "
                    elif "to" in data:
                        text = "You: "
                    else:
                        text = ""
                    self.wm.dialog(text+data['message'],2000,self)
                    self.cseq += 1
                elif setype == "delay":
                    print "DELAY"
                    start = self.Timestamp()
                    while float(self.Timestamp()) - float(start) < (float(data['time']) * 1000.0):
                        self.render(canMove = data['canMove'],story=False)
                        pygame.display.update()
                    self.cseq += 1
                elif setype == "move":
                    print "MOVE"
                    start = self.p['pos']
                    if "x" in data:
                        axis = 0
                        final = self.p['pos'][axis] - data['x']
                    elif "y" in data:
                        axis = 1
                        final = self.piggy['pos'][axis] - data['y']
                    done = False
                    self.cseq = self.cseq + 1
                    while done == False:
                        if data['who'] == 'ralph':
                            if final < self.p['pos'][axis]:
                                self.p['pos'][axis] -= 1
                            elif final > self.p['pos'][axis]:
                                self.p['pos'][axis] += 1
                            else:
                                done = True
                        if data['who'] == 'piggy':
                            if final < self.piggy['pos'][axis]:
                                self.p['pos'][axis] -= 1
                            elif final > self.piggy['pos'][axis]:
                                self.p['pos'][axis] += 1
                            else:
                                done = True
                        self.render(canMove=data['canMove'],story = False)
                        pygame.display.update()
                        time.sleep(0.15)
                elif setype == "gather":
                    print "GATHER"
                    self.wm.dialog(data['message'],3000,self)
                elif setype == "setPos":
                    if data['player'] == "piggy":
                        self.piggy['pos'] = [data['x'],data['y']]
                    elif data['player'] == "player":
                        self.player['pos'] = [data['x'],data['y']]
        try:
            canMove = self.story[self.cstage]['sequence'][self.cseq]['canMove']
        except:
            pass
        
        if eventOveride == False:
            for e in pygame.event.get():
                if keys and canMove:
                    if e.type == pygame.KEYUP:
                        try:
                            if e.key == pygame.K_w or e.key == pygame.K_UP:
                                if self.p['pos'][1] != 0 and self.fmap[self.p['pos'][1]-1][self.p['pos'][0]] != "t" and self.map[self.p['pos'][1]-1][self.p['pos'][0]] != "w":
                                    self.p['pos'][1] -= 1
                            if e.key == pygame.K_s or e.key == pygame.K_DOWN:
                                if self.p['pos'][1] != len(self.map) - 1 and self.fmap[self.p['pos'][1]+1][self.p['pos'][0]] != "t" and self.map[self.p['pos'][1]+1][self.p['pos'][0]] != "w":
                                    self.p['pos'][1] += 1
                            if e.key == pygame.K_a or e.key == pygame.K_LEFT:
                                if self.p['pos'][0] != 0 and self.fmap[self.p['pos'][1]][self.p['pos'][0]-1] != "t" and self.map[self.p['pos'][1]][self.p['pos'][0]-1] != "w":
                                    self.p['pos'][0] -= 1
                            if e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                                if self.p['pos'][0] != len(self.map[0])-1 and self.fmap[self.p['pos'][1]][self.p['pos'][0]+1] != "t" and self.map[self.p['pos'][1]][self.p['pos'][0]+1] != "w":
                                    self.p['pos'][0] += 1
                        except:
                            print "Error With Keys"
                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_ESCAPE:
                        options = ["Cancel",'Return to Menu',"Quit to Desktop"]
                        result = self.wm.menu("Game Paused",options,self)
                        if result == 1:
                            self.save()
                            return 'title'
                        elif result == 2:
                            self.quit(2)
                        if e.key == pygame.K_m:
                            self.wm.dialog("Welcome To The Game",3000,self)
                if e.type == pygame.QUIT:
                    self.quit(code)
            
        py = self.p['pos'][1]
        px = self.p['pos'][0]
        if px > (self.wm.width / self.block) / 2:
            if px > len(self.map[0]) - ((self.wm.width / self.block) / 2):
                startx = len(self.map[0]) - ((self.wm.width / self.block))
            else:
                startx = px - (self.wm.width / self.block) / 2
        else:
            startx = 0
        if py > self.bh / 2:
            if py > len(self.map) - (self.bh / 2):
                starty = len(self.map) - (self.bh)
            else:
                starty = py - self.bh / 2

        else:
            starty = 0
        for y in range(starty,starty + self.bh + 10):
            for x in range(startx,startx + self.bos + 10):
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
                    if y == py and x == px:
                        self.w.blit(self.ralphT,((x-startx)*self.block,(y-starty)*self.block))
                    if y == self.piggy['pos'][1] and x == self.piggy['pos'][0]:
                        self.w.blit(self.piggyT,((x-startx)*self.block,(y-starty)*self.block))
                    if self.fmap[y][x] == "t":
                        self.w.blit(self.tree,(((x-startx)*self.block) - self.block,int(((y-starty)*self.block))-(self.block * 3.75)+(self.block)))
                    
                except IndexError:
                    self.w.blit(self.water,((x-startx)*self.block,(y-starty)*self.block))
        return True
        
        
if __name__ == "__main__":
    if sys.argv[1] == "genmap":
        m=[]
        with open('../data/terrain.md') as mapdata:
            for l in mapdata.read().split("\n"):
                row = []
                for x in l.split(' '):
                    row.append(x)
                m.append(row)
            m = m[0:len(m)-1]
        with open('../data/'+sys.argv[2]+".md",'w') as new:
            for y in m:
                a = (sys.argv[3]+" ")*(len(y))
                new.write(a[0:-1]+"\n")
    elif sys.argv[1] == 'randfol':
        m=[]
        with open('../data/terrain.md') as mapdata:
            for l in mapdata.read().split("\n"):
                row = []
                for x in l.split(' '):
                    row.append(x)
                m.append(row)
            m = m[0:len(m)-1]
        fm=[]
        for y in range(0,len(m)):
            row = []
            for x in range(0,len(m[0])):
                if m[y][x] == "g":
                    number = randrange(32)
                    if number == 3:
                        row.append("t")
                    elif number == 2:
                        num = randrange(3)
                        if num == 1:
                            row.append("r")
                        elif number == 2:
                            row.append("x")
                        elif number == 3:
                            row.append("z")
                    elif number == 7 or number == 8:
                        row.append("f")
                    elif number == 30 or number == 20:
                        row.append("q") 
                    elif number == 31 or number == 21:
                        row.append("w")
                    elif number == 32 or number == 22:
                        row.append("e")
                    else:
                        row.append("n")
                else:
                    row.append("n")
            fm.append(row)
        with open('../data/foliage.md','w') as new:
            for y in range(0,len(m)):
                for x in range(0,len(m[0])):
                    new.write(fm[y][x])
                    if x != len(fm[y]) - 1:
                        new.write(" ")
                if y != len(fm) - 1:
                    new.write("\n")
    elif sys.argv[1] == "clearmap":
        s = int(sys.argv[2])
        m = []
        for y in range(0,s+1):
            row = []
            for x in range(0,s+1):
                if y in [0,1,s,s-1]:
                    row.append("w")
                elif x in [0,1,s,s-1]:
                    row.append("w")
                elif y in [2,3,4,5,s-2,s-3,s-4,s-5]:
                    if x in [2,3,4,5,s-2,s-3,s-4,s-5]:
                        row.append("s")
                    else:
                        row.append("s")
                elif x in [2,3,4,5,s-2,s-3,s-4,s-5]:
                    row.append("s")
                else:
                    row.append("g")
            m.append(row)
        with open('../data/terrain.md','w') as new:
            for y in range(0,len(m)):
                for x in range(0,len(m[0])):
                    new.write(m[y][x])
                    if x != len(m[y]) - 1:
                        new.write(" ")
                if y != len(m) - 1:
                    new.write("\n")
