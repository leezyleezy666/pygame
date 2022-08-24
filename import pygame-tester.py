import pygame 

FPS = 60
WIDTH = 500
HEIGHT = 600

GREEN = (0,255,0)

pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption('JESUS')
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(GREEN)
        self.rect = self.image.get.rect()
        self.rect.x = 200
        self.rect.y = 200
        
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True 

#廻圈
while running:
    # 取得input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # update
    
    
    # screen
    all_sprites.draw(screen)
    pygame.display.update()
            
    
pygame.quit()