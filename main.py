from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController(speed=80, position=(-80, 9, -240), scale=9)
Sky()

def input(key):
    if key == 'escape':
        quit()

# Piso
platform = Entity(model="cube", collider="box", texture="piso", scale=(3000, 0, 3000), position=(0, 10, 0))

Entity(model="cube", collider="mesh", texture="pared", scale=250,position=(250, 0, 0))#pared derecha
Entity(model="cube", collider="mesh", texture="techo", scale=250,position=(0, 250, 0))#techo
Entity(model="cube", collider="mesh", texture="pared", scale=250,position=(-250, 0, 0))# pared izquierda
Entity(model="cube", collider="mesh", texture="pared", scale=250,position=(0, 0, 250))
app.run()
