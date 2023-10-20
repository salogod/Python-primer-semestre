import turtle
import math
import random

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Pac-Man")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Desactivar actualizaciones automáticas

# Crear el personaje Pac-Man
pacman = turtle.Turtle()
pacman.shape("circle")
pacman.color("yellow")
pacman.penup()
pacman.speed(0)
pacman.goto(0, -250)
pacman.direction = "stop"

# Crear puntos (comida)
comida = turtle.Turtle()
comida.shape("circle")
comida.color("white")
comida.penup()
comida.speed(0)
comida.goto(random.randint(-290, 290), random.randint(-290, 290))

# Lista de fantasmas
fantasmas = []

# Función para mover a Pac-Man
def move():
    if pacman.direction == "up":
        y = pacman.ycor()
        pacman.sety(y + 20)
    if pacman.direction == "down":
        y = pacman.ycor()
        pacman.sety(y - 20)
    if pacman.direction == "left":
        x = pacman.xcor()
        pacman.setx(x - 20)
    if pacman.direction == "right":
        x = pacman.xcor()
        pacman.setx(x + 20)

# Funciones para cambiar la dirección de Pac-Man
def go_up():
    pacman.direction = "up"

def go_down():
    pacman.direction = "down"

def go_left():
    pacman.direction = "left"

def go_right():
    pacman.direction = "right"

# Conectar las teclas a las funciones de movimiento
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Función para colisión entre Pac-Man y comida
def colision(comida, pacman):
    distancia = math.sqrt((comida.xcor() - pacman.xcor())**2 + (comida.ycor() - pacman.ycor())**2)
    if distancia < 20:
        return True
    else:
        return False

# Función principal del juego
while True:
    wn.update()

    # Mover Pac-Man
    move()

    # Comprobar colisión con comida
    if colision(comida, pacman):
        comida.goto(random.randint(-290, 290), random.randint(-290, 290))

    # Crear y mover fantasmas
    for _ in range(len(fantasmas)):
        fantasma = fantasmas[_]
        x = fantasma.xcor()
        x += random.randint(-5, 5)
        fantasma.setx(x)

        if fantasma.xcor() > 290:
            fantasma.setx(290)
        if fantasma.xcor() < -290:
            fantasma.setx(-290)

# Cerrar la ventana al hacer clic en la "X"
wn.bye()

