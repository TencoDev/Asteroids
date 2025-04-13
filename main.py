import pygame
from constants import * 

def main():
    pygame.init()
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
        screen.fill('black')
    
        pygame.display.flip()
    
if __name__ ==  "__main__":
    main()