import pygame

class Game():
    
    corredores = []
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption('Carrera de Bichos')
        self.background = pygame.image.load('images/background.png')

if __name__ == '__main__':
    pygame.init()
    game = Game()
        
        
