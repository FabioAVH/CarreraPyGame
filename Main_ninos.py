#peque;o juego para los ninos

import pygame, sys, random

   
#----------- CLASS RUNNER -----------------
class Runner():
       
    def __init__(self, x=0,y=0, vestidoA='red'):
        self.vestido = pygame.image.load("images/runner_{}.png".format(vestidoA))
        self.position = [x,y]
        self.name = vestidoA
        
        
        
#----------- CLASS RUNNER -----------------      
class Game():
    runners = []
    __posY = (180, 260)
    __vestidos = ('red','yellow')
    __startline = 3
    __finishline = 610
    
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de Bichos")
        self.background = pygame.image.load("images/background.png")
        
        #Crea los corredores
        
        runnerA = Runner(self.__startline, self.__posY[0],self.__vestidos[0])
        runnerA.name = self.__vestidos[0]
        self.runners.append(runnerA)

        runnerA = Runner(self.__startline, self.__posY[1],self.__vestidos[1])
        runnerA.name = self.__vestidos[1]
        self.runners.append(runnerA)


    def CloseGame(self):
        pygame.quit()
        sys.exit()

    
    def competir(self):
        
        hayGanador = False
        
        while not hayGanador:
        
        #comprbacion enventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.runners[0].position[0] = self.runners[0].position[0] + 15
                    if event.key == pygame.K_p:
                        self.runners[1].position[0] = self.runners[1].position[0] + 15
                else:
                    pass
                
            #modo 1
            for i in range(2): 
                                
                if self.runners[i].position[0] >= self.__finishline:
                    print('{} ha ganado'.format(self.runners[i].name))
                    hayGanador = True
            
            
            self.__screen.blit(self.background, (0,0)) #renderizar la pantalla
            
            self.__screen.blit(self.runners[0].vestido, self.runners[0].position)
            self.__screen.blit(self.runners[1].vestido, self.runners[1].position)
                        
            pygame.display.flip() #refrescar

        # cierra el programa una vez finalizada la carrera, cuando se presiona la X
        #while True es un bucle infinito, lo termino a las malas
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.CloseGame()
        
                        
        
        
                       
                
#----------- 'MAIN' -----------------
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
        
        
        
