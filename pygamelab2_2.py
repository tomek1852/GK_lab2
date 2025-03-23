import pygame

# Inicjalizacja Pygame
pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Litera Z z przekształceń")

# Kolory
BIALY = (255, 255, 255)
CZERWONY = (255, 0, 0)

# Funkcja do rysowania litery "Z"
def draw_z(surface):
    # Rozmiar i pozycja
    rect_width = 200
    rect_height = 10

    # Górna linia
    pygame.draw.rect(surface, CZERWONY, (200, 100, rect_width, rect_height))

    # Przekątna
    diagonal_surface = pygame.Surface((rect_width + 82, rect_height), pygame.SRCALPHA)
    pygame.draw.rect(diagonal_surface, CZERWONY, (0, 0, rect_width + 82, rect_height))
    rotated_surface = pygame.transform.rotate(diagonal_surface, 45)
    surface.blit(rotated_surface, (200, 100))

    # Dolna linia
    pygame.draw.rect(surface, CZERWONY, (200, 300, rect_width, rect_height))

# Pętla programu
run = True
while run:
    win.fill(BIALY)  # Czyszczenie ekranu

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Rysowanie litery "Z"
    draw_z(win)

    pygame.display.update()

pygame.quit()
