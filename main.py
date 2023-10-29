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
app.run()
