#sprite
import pygame
import random

FPS = 60
WHITE = (255,255,255)
WIDTH = 500
HEIGHT = 600
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)


#遊戲的初始化 and 視窗創建
pygame.init()
scree = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("射擊遊戲")
clock = pygame.time.Clock() #時間物件


#玩家sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT -10
        self.speedx = 8

    def update(self):
        key_pressed = pygame.key.get_pressed() #回傳布林值 白話文鍵盤每個按鍵有沒有按下去
        if key_pressed[pygame.K_d]: #判斷右鍵有沒有按下去D鍵
            self.rect.x += self.speedx
        if key_pressed[pygame.K_a]: #判斷左鍵有沒有按下去A鍵
            self.rect.x -= self.speedx   
        
        if self.rect.right >WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet) #把子彈加入群組          

#石頭sprite
class Rock(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(2,10) #降落速度
        self.speedx = random.randrange(-3,3) #水平速度
        
    def update(self):
       self.rect.y += self.speedy
       self.rect.x += self.speedx 
       if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(0,WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(2,10) #降落速度
            self.speedx = random.randrange(-3,3) #水平速度

#子彈sprite
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y): #傳入飛船的x,y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
       self.rect.y += self.speedy
       if self.rect.bottom < 0:     #判斷子彈底部小於0的時候 表示出了上面的視窗
           self.kill() #從有sprite群組裡的子彈全部刪除



all_sprites = pygame.sprite.Group()
player = Player()    
all_sprites.add(player)
for i in range(8): #利用for迴圈創建多顆石頭
    r = Rock()
    all_sprites.add(r)



#遊戲的迴圈 
running = True
while running:
    clock.tick(FPS)  # 一秒鐘之列最多執行10次(FPS) 
    #取得輸入
    for event in pygame.event.get(): #回傳列表
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: #按下鍵盤建
            if event.key == pygame.K_SPACE: #按下鍵盤鍵再一次做判斷
                player.shoot()


    #更新遊戲
    all_sprites.update()
    pygame.sprite.groupcollide(rocks, bullets,True,True)


    # 畫面顯示
    scree.fill(BLACK)
    all_sprites.draw(scree)
    pygame.display.update()  #畫面更新  

pygame.quit()                      