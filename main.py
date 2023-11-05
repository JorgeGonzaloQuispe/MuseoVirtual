from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController(speed=150, position=(50, 0, 50), scale=9)  # Nueva posición del jugador
Sky()

def input(key):
    if key == 'escape':
        quit()

# Crear el suelo del museo
platform = Entity(model="cube", collider="box", texture="piso", scale=(3000, 1, 3000), position=(0, 0, 0))

# Pared derecha
wall_1 = Entity(model='cube', scale=(1000, 1000, 10), color=color.white, texture = "wall4.jpg", collider='box')
wall_1.x = 0  # Ubicar la tercera pared
wall_1.z = -500
wall_1.y = 0

# Pared izquierda
wall_2 = Entity(model='cube', scale=(1000, 1000, 10), color=color.white, texture = "wall4.jpg", collider='box')
wall_2.x = 0  # Ubicar la tercera pared
wall_2.z = 500
wall_2.y = 0

# Pared enfrente
wall_2 = Entity(model='cube', scale=(10, 1000, 1000), color=color.white, texture = "wall4.jpg", collider='box')
wall_2.x = -500  # Ubicar la tercera pared
wall_2.z = 0
wall_2.y = 0

# Techo del museo
ceiling = Entity(model='cube', scale=(1000, 10, 1000), color=color.white, texture = "wall1", collider='box')
ceiling.y = 500  # Ubicar el techo
ceiling.z = 0
ceiling.x = 0

#Colocar aqui sus cambios 

app.run()
