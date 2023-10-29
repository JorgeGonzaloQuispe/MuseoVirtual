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

#Cubo
Entity(model="cube", collider="mesh", texture="holi", scale=250,position=(250, 250, 0))#pared derecha
Entity(model="cube", collider="mesh", texture="holi", scale=250,position=(500, 250, 0))#pared derecha

app.run()

