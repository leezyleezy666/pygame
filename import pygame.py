import pygame
import random

FPS = 60
HEIGHT = 600
WIDTH = 500

WHITE = (255,255,255)
RED = (255,0,0)

#游戏初始化   create 视窗
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("first_mini_game")
clock = pygame.time.Clock()

# sprites 建立
class Player(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill((RED))
        # self.rect = self.image.get_rect()
        self.rect = ((WIDTH / 2), (HEIGHT - 10)) 
        self.speedx = 8
        
    # def update(self):          
    #     key_pressed = pygame.get_pressed()      #移动
    #     if key_pressed[pygame.K_RIGHT or pygame.K_d]:
    #         self.rect.x += self.speedx
    #     if key_pressed[pygame.K_LEFT or pygame.K_a]:
    #         self.rect.x += self.speedx
            
    #     if self.rect.right > WIDTH:    #限制住不让它超出画面
    #         self.rect.right = WIDTH
    #     if self.rect.left < 0:    
    #         self.rect.left = 0  

# class Rock(pygame.sprite.Sprite):
#     def _init_(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((30,40))
#         self.image.fill(RED)
#         self.rect = self.image.get_rect()
#         self.rect.x = random.randrange(0, WIDTH - self.rect.width) 
#         self.rect.y = random.randrange(-100, -40)
#         self.speedy = random.randrange(2,10)
#         self.speedx = random.randrange(-3,3)
        
#     def update(self):          
#         self.rect.y += self.speedy
#         self.rect.x += self.speedx
#         if self.rect.y > HEIGHT:
#             self.rect.y = 0
 
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# for i in range (8):
#     rock = Rock()
#     all_sprites.add(rock)

#game 廻圈
running = True

while running:
    clock.tick(FPS)
    # get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #frame update
    all_sprites.update()
    
    # 画面
    screen.fill(WHITE)
    all_sprites.draw(screen)  #把全部sprite画出来
    pygame.display.update()

pygame.quit