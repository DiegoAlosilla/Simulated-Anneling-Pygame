import sys, pygame
from Coordinates import Coordinates
from PointsAdmin import PointsAdmin
from SimulatedAnnealing import SimulatedAnnealing


#Inicializamos pygame
pygame.init()
size = (1600,900)
sizeBackGrounbd = (1600,1000)
#Creamos una nueva ventana
screen = pygame.display.set_mode(size)

#Cambiamos el titulo de la ventana
pygame.display.set_caption("Simulated Anneling")

#Inicializamos el sonido de fondo
pygame.mixer.music.load("resources/music/tema.mp3")
pygame.mixer.music.play(-1)

#Cambiamos el fondo de la ventana
backGround = pygame.image.load("resources/img/mapa.png")
backGround = pygame.transform.scale(backGround,sizeBackGrounbd)

#Creamos el arreglo de puntosAdmin
pointsA = PointsAdmin()

#Inicalizamos fuente de texto
fuente = pygame.font.SysFont("Arial",20)
#Color
rgb = (115, 198, 182)

#Funcion de tiempo
time_aux = 1

#Funcion para pintar ciculos
def drawPoints():
    coordinates = Coordinates(x_mouse, y_mouse)
    pointsA.add_coordinates(coordinates)
    for i in range(0,pointsA.get_size()):
        pygame.draw.circle(screen,rgb,Coordinates.get_coordinates(pointsA.get_coordinates(i)),7)

#Función para pintar lineas
#color = pygame.Color(70,80,150)
def drawLine():
    if pointsA.get_size() > 1:
        for i in range(1,pointsA.get_size()):
            temp = i-1
            pygame.draw.line(screen,rgb,Coordinates.get_coordinates(pointsA.get_coordinates(i)),
            Coordinates.get_coordinates(pointsA.get_coordinates(temp)),
            3)
            #pygame.time.delay(1000)
            if i == pointsA.get_size()-1 :
                pygame.draw.line(screen,rgb,Coordinates.get_coordinates(pointsA.get_coordinates(i)),
                Coordinates.get_coordinates(pointsA.get_coordinates(0)),
                3)
                #pygame.time.delay(1000)



#Comenzamos el bucle del juego
run = True
boolTime = True
boolDrawLine = False
screen.blit(backGround,(0,0))
flat =False
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
                drawPoints()
        #Evento con el que capturamos si se presiono un boton del teclado
        if event.type == pygame.KEYDOWN:
            #Aplicamos el algoritmo SimulatedAnnealing
            if event.key == pygame.K_SPACE:

                flat =True
                rgb = (133, 193, 233)
                sa = SimulatedAnnealing(pointsA, 10000, 0.003)
                sa.run()
                for i in range(pointsA.get_size()):
                    pointsA.set_coordinates(i,sa.points.get_coordinates(i))
                screen.blit(backGround,(0,0))
                boolTime = False
                drawLine()

        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(backGround,(0,0))
    if pointsA.get_size()>0:
        drawPoints()
        drawLine()
    #imprimir tiempo en pantalla
    if boolTime:
        time = pygame.time.get_ticks()/1000
        if time_aux == time:
            time_aux+=1
    screen.blit((fuente.render("Tiempo: "+str(time)+ " mseg",0,(240, 243, 244))),(100,700))
    if flat:
        screen.blit((fuente.render("Distancia: "+str(sa.points.get_distance())+ " Km",0,(240, 243, 244))),(100,740))
    screen.blit((fuente.render("Clic para crear puntos(coordenadas) y Espacio para encotrar posibles rutas",0,(240, 243, 244))),(100,100))
    pygame.display.update()
    #Pinto el fondo
    pygame.display.flip()


#Salgo de pygame
pygame.quit()
