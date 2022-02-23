import turtle
import math

xam = turtle.Turtle()
xam.speed(500)

window = turtle.Screen()
window.bgcolor("#000000")
xam.color("yellow")

Xam2 = 20

xam.left(90)
xam.penup()
xam.goto(-7 * Xam2, 0)
xam.pendown()

for a in range(-7 * Xam2, -3 * Xam2, 1):
    x = a / Xam2
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    xam.goto(a, y * Xam2)

for a in range(-3 * Xam2, -1 * Xam2 - 1, 1):
    x = a / Xam2
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    xam.goto(a, y * Xam2)

xam.goto(-1 * Xam2, 3 * Xam2)
xam.goto(int(-0.5 * Xam2), int(2.2 * Xam2))
xam.goto(int(0.5 * Xam2), int(2.2 * Xam2))
xam.goto(1 * Xam2, 3 * Xam2)
print("Batman Logo with Python Turtle")
for a in range(1 * Xam2 + 1, 3 * Xam2 + 1, 1):
    x = a / Xam2
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    xam.goto(a, y * Xam2)

for a in range(3 * Xam2 + 1, 7 * Xam2 + 1, 1):
    x = a / Xam2
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    xam.goto(a, y * Xam2)

for a in range(7 * Xam2, 4 * Xam2, -1):
    x = a / Xam2
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    xam.goto(a, y * Xam2)

for a in range(4 * Xam2, -4 * Xam2, -1):
    x = a / Xam2
    rel = math.fabs(x)
    y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
    xam.goto(a, y * Xam2)

for a in range(-4 * Xam2 - 1, -7 * Xam2 - 1, -1):
    x = a / Xam2
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    xam.goto(a, y * Xam2)

xam.penup()
xam.goto(300, 300)
turtle.done()