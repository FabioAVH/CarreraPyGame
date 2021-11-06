import pygame, sys, random

   
#----------- CLASS RUNNER -----------------
class Runner():
       
    def __init__(self, x=0,y=0, vestidoA='red'):
        self.vestido = pygame.image.load("images/runner_{}.png".format(vestidoA))
        self.position = [x,y]
        self.name = vestidoA
        
    def avanzar(self):
        self.position[0] += random.randint(1,6)
        
        
#----------- CLASS RUNNER -----------------      
class Game():
    runners = []
    __posY = (160, 200, 240, 280)
    __vestidos = ('red','yellow','green','blue')
    __startline = 3
    __finishline = 610
    
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de Bichos")
        self.background = pygame.image.load("images/background.png")
        
        #Crea los corredores
        for i in range(4):
            runnerA = Runner(self.__startline, self.__posY[i],self.__vestidos[i])
            runnerA.name = self.__vestidos[i]
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
                
            #modo 1
            for i in range(len(self.runners)): 
                self.runners[i].avanzar()
                
                if self.runners[i].position[0] >= self.__finishline:
                    print('{} ha ganado'.format(self.runners[i].name))
                    hayGanador = True
            
            
            self.__screen.blit(self.background, (0,0)) #renderizar la pantalla
            
            #modo 2
            for runnerB in self.runners: 
                self.__screen.blit(runnerB.vestido, runnerB.position)
            
            
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
        
        
        
