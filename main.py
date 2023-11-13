from turtle import position
from ursina import *
import pygame
from pydub import AudioSegment
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Carga el archivo MP3
audio = AudioSegment.from_mp3("musica.mp3")

# Exporta el archivo a formato WAV
audio.export("flordelacanela.wav", format="wav")

# Carga el archivo WAV
file_path = "flordelacanela.wav"

# Inicializa el módulo de audio de pygame
pygame.mixer.init()

# Carga el archivo en pygame
pygame.mixer.music.load(file_path)

# Reproduce el archivo en un bucle (-1 para reproducir en bucle)
pygame.mixer.music.play(-1)

# Asegúrate de manejar la lógica de la aplicación Ursina y renderizar la ventana.
def update():
    pass


player = FirstPersonController(speed=150, position=(50, 0, 50), scale=15)  # Nueva posición del jugador
Sky()

def input(key):
    if key == 'escape':
        quit()

# Crear el suelo del museo
platform = Entity(model="cube", collider="box", texture="piso", scale=(3000, 1, 3000), position=(0, 0, 0))


##################################################################
# Pared izquierda cuarto principal

wall_1_1 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = -350/2
wall_1_1.z = -500
wall_1_1.y = 0

wall_1_1_1= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1_1.x = -425
wall_1_1_1.z = -500
wall_1_1_1.y = 370

wall_1_11 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_11.x = 325
wall_1_11.z = -500
wall_1_11.y = 0

wall_1_111= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_111.x = 75
wall_1_111.z = -500
wall_1_111.y = 370

# Cuarto 1 y 2 izquierdo

# pared izquierda 
wall_1_1_2 = Entity(model='cube', scale=(1000, 1000, 10), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_1_2.x = 0
wall_1_1_2.z = -1000 # mover a la derecha 
wall_1_1_2.y = 0


# pared de cuarto 1
wall_1_1_3 = Entity(model='cube', scale=(10, 1000, 500), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_1_3.x = -500 
wall_1_1_3.z = -750
wall_1_1_3.y = 0


# pared separador cuarto 1 y 2
wall_1_1_3 = Entity(model='cube', scale=(10, 1000, 500), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_1_3.x = 0 
wall_1_1_3.z = -750
wall_1_1_3.y = 0



# interior color cuartos 1 y 2 , cuartos izquierdos
wall_1_1 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_1.x = -350/2
wall_1_1.z = -505
wall_1_1.y = 0

wall_1_1_1= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_1_1.x = -425
wall_1_1_1.z = -505
wall_1_1_1.y = 370

wall_1_11 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_11.x = 325
wall_1_11.z = -505
wall_1_11.y = 0

wall_1_111= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_111.x = 75
wall_1_111.z = -505
wall_1_111.y = 370

##################################################################
# Pared derecha cuarto principal

wall_1_1 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = -350/2
wall_1_1.z = 500
wall_1_1.y = 0

wall_1_1_1= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1_1.x = -425
wall_1_1_1.z = 500
wall_1_1_1.y = 370

wall_1_11 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_11.x = 325
wall_1_11.z = 500
wall_1_11.y = 0

wall_1_111= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_111.x = 75
wall_1_111.z = 500
wall_1_111.y = 370

# Cuarto 1 y 2 izquierdo

# pared 
wall_1_1_2 = Entity(model='cube', scale=(1000, 1000, 10), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_1_2.x = 0
wall_1_1_2.z = 1000 # mover a la derecha 
wall_1_1_2.y = 0


# pared de cuarto 1
wall_1_1_3 = Entity(model='cube', scale=(10, 1000, 500), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_1_3.x = -500 
wall_1_1_3.z = 750
wall_1_1_3.y = 0


# pared separador cuarto 1 y 2
wall_1_1_3 = Entity(model='cube', scale=(10, 1000, 500), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_1_3.x = 0 
wall_1_1_3.z = 750
wall_1_1_3.y = 0
# interior color cuartos 1 y 2 , cuartos izquierdos
wall_1_1 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_1.x = -350/2
wall_1_1.z = 505
wall_1_1.y = 0

wall_1_1_1= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_1_1.x = -425
wall_1_1_1.z = 505
wall_1_1_1.y = 370

wall_1_11 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_11.x = 325
wall_1_11.z = 505
wall_1_11.y = 0

wall_1_111= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_111.x = 75
wall_1_111.z = 505
wall_1_111.y = 370

#######################################
# Pared enfrente
wall_2 = Entity(model='cube', scale=(10, 1000, 1000), color=color.white, texture = "wall4.jpg", collider='box')
wall_2.x = -500  
wall_2.z = 0
wall_2.y = 0

# Techo del museo
ceiling = Entity(model='cube', scale=(1000, 10, 2000), color=color.white, texture = "wall4_1.jpg", collider='box')
ceiling.y = 500  
ceiling.z =0
ceiling.x = 0

#Colocando la estatua
estatua = Entity(model="esta.glb", scale=(100,100,100), collider='box')
def update():
    estatua.rotation_y += 1

#Funcion para movimientos horizontales
persona = Entity(model="persona.glb", scale=(10,10,10), collider='box', position=(300, 21, 20))
def update():
    persona.rotation_y += 1 #Solo seria sobre su propio radio

Entity(model="vicuna_peru.glb", collider='box', position=(1000, 20, 1000))

#Colocar aqui sus cambios 
#Pared enfrente:
autor= Entity(model="cube",scale=(0,350,200), texture="Pancho.jpg",collider="box",position=(-490,250,-320))
cua1= Entity(model="cube",scale=(0,180,150), texture="cua1.jpg",collider="box",position=(-490,350,-80))
cua2= Entity(model="cube",scale=(0,180,150), texture="cua2.jpg",collider="box",position=(-490,130,-80))
cua3= Entity(model="cube",scale=(0,180,150), texture="cua3.jpg",collider="box",position=(-490,350,135))
cua4= Entity(model="cube",scale=(0,180,150), texture="cua4.jpg",collider="box",position=(-490,130,135))
cua5= Entity(model="cube",scale=(0,180,150), texture="cua5.jpg",collider="box",position=(-490,350,340))
cua6= Entity(model="cube",scale=(0,180,150), texture="cua6.jpg",collider="box",position=(-490,130,340))


# candelabros de los cuartos
cande = Entity(model="candelabro.glb", scale=(50,50,50), collider='box',position=(0,500,0))
def update():
    cande.rotation_y += 1 #Solo seria sobre su propio radio

# fachada
wall_2 = Entity(model='cube', scale=(1, 480, 400), color=color.white, texture = "MuseoFachada.jpg", collider='box',position=(505,140,0))
wall_2 = Entity(model='cube', scale=(10, 135, 400), color=color.white, texture = "wall4.jpg", collider='box',position=(505,430,0))
wall_2 = Entity(model='cube', scale=(30, 100, 300), color=color.white, texture = "nombre.jpg", collider='box',position=(524,410,0))
wall_2 = Entity(model='cube', scale=(10, 500, 805), color=color.white, texture = "wall4.jpg", collider='box',position=(505,250,595))
wall_2 = Entity(model='cube', scale=(10, 500, 805), color=color.white, texture = "wall4.jpg", collider='box',position=(505,250,-595))



# Cuarto de Gonzalo - Historia
# estatuas
Simon_Bolivar= Entity(model="SimonBolivar.glb", scale=(15,15,15), collider='box',position=(100,-90,-930));Simon_Bolivar.rotation_y = 180 
Jose_San_Martin=Entity(model="JoseSanMartin.glb", scale=(16,16,16), collider='box',position=(100,140,-1190));Jose_San_Martin.rotation_y=160

# pinturas
Ceviche_= Entity(model="cube",scale=(5,150,200), texture="ceviche.jpg",collider="box",position=(140,380,-996)); Ceviche_.rotation_y = 90; 
Adovo_= Entity(model="cube",scale=(5,150,200), texture="adobo.jpg",collider="box",position=(360,380,-996));Adovo_.rotation_y = 90
Chupecamarones_=Entity(model="cube",scale=(5,150,200), texture="chupecamarones.jpg",collider="box",position=(502,380,-856))
Secocordero_=Entity(model="cube",scale=(5,150,200), texture="secocordero.jpg",collider="box",position=(502,380,-636))
Anticucho_=Entity(model="cube",scale=(5,150,200), texture="anticucho.jpg",collider="box",position=(502,210,-856))
Tacutacu_=Entity(model="cube",scale=(5,150,200), texture="tacutacu.jpg",collider="box",position=(502,210,-636))
app.run()