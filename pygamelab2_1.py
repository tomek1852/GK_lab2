import pygame
import math

# Inicjalizacja Pygame
pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Octagon Transformation")

# Kolory
BIALY = (255, 255, 255)
CZERWONY = (255, 0, 0)

# Funkcja do rysowania foremnego ośmiokąta
def draw_octagon(surface, center, size, angle=0, scale_x=1, scale_y=1, shear_x=0, shear_y=0):
    points = []
    for i in range(8):
        theta = math.radians(45 * i + angle)
        x = math.cos(theta) * size * scale_x
        y = math.sin(theta) * size * scale_y
        x += shear_x * y  # Pochylenie w lewo lub prawo
        y += shear_y * x  # Pochylenie w górę lub w dół
        points.append((center[0] + x, center[1] + y))
    pygame.draw.polygon(surface, CZERWONY, points, 2)

# Parametry początkowe
center = (300, 300)
size = 100
angle = 20
scale_x = 1
scale_y = 1
shear_x = 0
shear_y = 0

run = True
while run:
    win.fill(BIALY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                size = max(10, size - 20)  # Zmniejszenie ośmiokąta
            elif event.key == pygame.K_2:
                angle = 45  # Obrót o 45 stopni
                shear_x = 0  # Resetowanie pochylenia
                shear_y = 0
            elif event.key == pygame.K_3:
                angle = 180+20  # Obrót o 180 stopni
                scale_x = 0.5  # Zwężenie w poziomie
                scale_y = 1  # Resetowanie skali w pionie
                shear_x = 0  # Resetowanie pochylenia
                shear_y = 0
            elif event.key == pygame.K_4:
                shear_x = 0.5  # Pochylenie w lewo
                angle = 20  # Resetowanie obrotu
                scale_x = 1  # Resetowanie skali
                scale_y = 1
                shear_y = 0
            elif event.key == pygame.K_5:
                center = (300, 150)  # Przesunięcie w górę
                scale_y = 0.5  # Zwężenie w pionie
                scale_x = 1  # Skala w poziomie bez zmian
            elif event.key == pygame.K_6:
                angle = 90+20  # Obrót o 90 stopni
                shear_y = -0.5  # Odchylenie w osi pionowej w lewo
            elif event.key == pygame.K_7:
                angle = 180+20  # Obrót o 180 stopni
                scale_x = 0.5  # Zwężenie w poziomie
                scale_y = 1  # Wysokość bez zmian
                shear_x = 0  # Resetowanie pochylenia
                shear_y = 0
                center = (600 - center[0], center[1])  # Lustro względem środka
            elif event.key == pygame.K_8:
                scale_x = 1.5  # Rozciągnięcie
                scale_y = 1.5
                angle = 30+20  # Obrót o 30 stopni
                center = (200, 400)  # Przesunięcie do lewego rogu
            elif event.key == pygame.K_9:
                scale_x = -scale_x  # Lustro względem osi pionowej
                shear_x = 0.5  # Pochylenie w lewo
                center = (480, center[1])  # Przesunięcie w prawo
            elif event.key == pygame.K_r:
                angle = 20  # Reset
                scale_x = 1
                scale_y = 1
                size = 100
                shear_x = 0
                shear_y = 0
                center = (300, 300)  # Resetowanie pozycji

    draw_octagon(win, center, size, angle, scale_x, scale_y, shear_x, shear_y)
    pygame.display.update()

pygame.quit()
