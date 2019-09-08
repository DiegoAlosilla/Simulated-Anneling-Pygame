import sys, pygame, Ciudad, TourAdmin, Tour, SimulatedAnnealing

#Inicializamos pygame
pygame.init()
size = (1600,900)
sizeBackGrounbd = (1600,1000)
#Creamos una nueva ventana
screen = pygame.display.set_mode(size)

#Cambiamos el titulo de la ventana
pygame.display.set_caption("Simulated Anneling")

#Inicializamos el sonido de fondo
#pygame.mixer.music.load("resources/img/mapa.png")

#Cambiamos el fondo de la ventana
backGround = pygame.image.load("resources/img/mapa.png")
backGround = pygame.transform.scale(backGround,sizeBackGrounbd)

#Funcion para pintar ciculos
def drawPints():
    pygame.draw.circle(screen,(34,153,84,255),(x_mouse, y_mouse),5)

#Función para pintar lineas
#color = pygame.Color(70,80,150)
#def drawLine():
#    pygame.draw.line(screen,color,(),())

#Comenzamos el bucle del juego
run = True
screen.blit(backGround,(0,0))
while run:
    #For para capturar eventos
    for event in pygame.event.get():
        #Evento con el que capturamos si se presiono un boton del mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            #si se presiono el boton izquierdo
            if event.button == 1:
                #obtiene la posicion del mouse dobde se presiono
                x_mouse,y_mouse=pygame.mouse.get_pos()
                #dibuja un circulo en la posion
                drawPints()
                drawPints2()
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    #Pinto el fondo
    pygame.display.flip()
    

#Salgo de pygame
pygame.quit()
