import math
from pathlib import Path

import pygame

# WINDOW
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# CIRCLE
circle_radius = 50
circle_pos = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  #Python draws circles from the center, and rectangles from the top left corner
circle_width = 3

# MOUSE
clicked = False
mouse_pos = 0,0

base_dir = Path(__file__).parent

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Window")

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        update(events)
        draw(screen)

def update(events):
    global mouse_pos, clicked

    mouse_pos = pygame.mouse.get_pos()
    clicked = getInputs(events)

    if clicked:
        if checkCollisions(mouse_pos):
            pygame.mixer.music.load(base_dir / "DtMF.mp3")
            pygame.mixer.music.play()
            clicked = False

def getInputs(events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return True
    return False

def checkCollisions(mouse_pos):
    dist = math.sqrt((mouse_pos[0] - circle_pos[0])**2 + (mouse_pos[1] - circle_pos[1])**2)
    return dist <= circle_radius

def draw(screen):
    screen.fill((0, 0, 0))  # Makes window black
    pygame.draw.circle(screen, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 50, 3)
    pygame.display.flip()  # Update display


if __name__ == "__main__":
    main()

pygame.quit()