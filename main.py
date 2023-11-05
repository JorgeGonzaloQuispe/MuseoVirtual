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

# Pared derecha
wall_1 = Entity(model='cube', scale=(1000, 1000, 10), color=color.white, texture = "wall4.jpg", collider='box')
wall_1.x = 0  
wall_1.z = -500
wall_1.y = 0

# Pared izquierda
wall_2 = Entity(model='cube', scale=(1000, 1000, 10), color=color.white, texture = "wall4.jpg", collider='box')
wall_2.x = 0  
wall_2.z = 500
wall_2.y = 0

# Pared enfrente
wall_2 = Entity(model='cube', scale=(10, 1000, 1000), color=color.white, texture = "wall4.jpg", collider='box')
wall_2.x = -500  
wall_2.z = 0
wall_2.y = 0

# Techo del museo
ceiling = Entity(model='cube', scale=(1000, 10, 1000), color=color.white, texture = "wall1", collider='box')
ceiling.y = 500  
ceiling.z = 0
ceiling.x = 0

#Colocando la estatua
estatua = Entity(model="esta.glb", scale=(50,50,50), collider='box')
def update():
    estatua.rotation_y += 1

#Funcion para movimientos horizontales
persona = Entity(model="persona.glb", scale=(10,10,10), collider='box', position=(300, 21, 20))
def update():
    persona.rotation_y += 1 #Solo seria sobre su propio radio

Entity(model="vicuna_peru.glb", collider='box', position=(1000, 0, 1000))

#Colocar aqui sus cambios 
app.run()
