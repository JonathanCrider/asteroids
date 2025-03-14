import pygame
import sys
import os
from config import config
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from main import main

# Initialize pygame
pygame.init()
assets_path = os.path.join(os.path.dirname(__file__), "assets")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (20, 20, 20)
YELLOW = (255, 255, 0)
HOVER_COLOR = (200, 200, 50)
MAIN_FONT_FACE = "menlo"
FONT = pygame.font.SysFont(MAIN_FONT_FACE, 48)
TEST_FONT = pygame.font.SysFont(MAIN_FONT_FACE, 12)

# Screen Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")

# Load Background
bg = pygame.image.load(f"{assets_path}/images/bg.jpg").convert()
bg.set_alpha(120)


def toggle_env():
  """Toggle between TEST and PROD environment."""
  config.ENV = config.TEST if config.ENV == config.PROD else config.PROD
  print(f"ENV switched to: {config.ENV}")
  print(f"Score modifier: {config.SCORE_THRESHOLD_MODIFIER}")


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
  test_hovered = False

  while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Button Coordinates
    BUTTON_WIDTH = 300
    BUTTON_HEIGHT = 50
    start_rect = pygame.Rect(SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, BUTTON_WIDTH, BUTTON_HEIGHT)
    quit_rect = pygame.Rect(SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, SCREEN_HEIGHT // 2 - 20, BUTTON_WIDTH, BUTTON_HEIGHT)
    test_rect = pygame.Rect(SCREEN_WIDTH - (BUTTON_WIDTH // 3) - 50, SCREEN_HEIGHT - 50, BUTTON_WIDTH // 3, BUTTON_HEIGHT // 3)

    start_hovered = start_rect.collidepoint(mouse_x, mouse_y)
    quit_hovered = quit_rect.collidepoint(mouse_x, mouse_y)
    test_hovered = test_rect.collidepoint(mouse_x, mouse_y)

    pygame.draw.rect(screen, HOVER_COLOR if start_hovered else WHITE, start_rect, border_radius=10)
    pygame.draw.rect(screen, HOVER_COLOR if quit_hovered else WHITE, quit_rect, border_radius=10)
    pygame.draw.rect(screen, HOVER_COLOR if test_hovered else GREY, test_rect, border_radius=10)

    draw_text("Start Game", FONT, BLACK, start_rect.centerx, start_rect.centery)
    draw_text("Quit", FONT, BLACK, quit_rect.centerx, quit_rect.centery)
    draw_text(config.ENV, TEST_FONT, BLACK, test_rect.centerx, test_rect.centery)

    # Display Controls
    control_font_face="menlo"
    control_font = pygame.font.SysFont(control_font_face, 36)
    draw_text("Controls:", control_font, YELLOW, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
    draw_text("Move: W A S D  or  \u2191 \u2193 \u2190 \u2192", control_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 140)
    draw_text("Strafe: A / D", control_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 180)
    draw_text("Fire: Space  or  Enter", control_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 220)
      
    # ↑ "\u2191"
    # ↓ "\u2193"
    # ← "\u2190"
    # → "\u2192"

    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return "quit"
      if event.type == pygame.MOUSEBUTTONDOWN:
        if start_hovered:
          return "play"
        if quit_hovered:
          return "quit"
        if test_hovered:
          toggle_env()

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
