import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2   
    
    updatables  = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (bullets,updatables, drawables )
    
    asteroid_field = AsteroidField()
    player = Player(x,y)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatables.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
                
            for bullet in bullets:
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    asteroid.split()
        
        screen.fill('black')
        
        for obj in drawables:
            obj.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
    
if __name__ ==  "__main__":
    main()