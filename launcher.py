import pygame
import sys
import os
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from main import main

# Initialize pygame
pygame.init()
assets_path = os.path.join(os.path.dirname(__file__), "assets")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
HOVER_COLOR = (200, 200, 50)
FONT = pygame.font.Font(None, 48)

# Screen Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")

# Load Background
bg = pygame.image.load(f"{assets_path}/bg.jpg").convert()
bg.set_alpha(120)


def draw_text(text, font, color, x, y):
    """Helper function to draw text centered on the screen."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def launcher_menu():
    """Display the launcher menu and handle navigation."""
    clock = pygame.time.Clock()
    running = True
    start_hovered = False
    quit_hovered = False

    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Button Coordinates
        start_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 50)
        quit_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20, 200, 50)

        start_hovered = start_rect.collidepoint(mouse_x, mouse_y)
        quit_hovered = quit_rect.collidepoint(mouse_x, mouse_y)

        pygame.draw.rect(screen, HOVER_COLOR if start_hovered else WHITE, start_rect, border_radius=10)
        pygame.draw.rect(screen, HOVER_COLOR if quit_hovered else WHITE, quit_rect, border_radius=10)

        draw_text("Start Game", FONT, (0, 0, 0), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 25)
        draw_text("Quit", FONT, (0, 0, 0), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 45)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_hovered:
                    return "play"
                if quit_hovered:
                    return "quit"

        clock.tick(30)


def main_launcher():
    """Handle switching between launcher and game."""
    while True:
      choice = launcher_menu()
      if choice == "play":
        choice = main()  # Directly launch the game in the same window
      if choice == "quit":
        pygame.quit()
        sys.exit()
      else:
        continue
      

if __name__ == "__main__":
    main_launcher()
