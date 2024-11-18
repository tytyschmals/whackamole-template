import pygame
import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_location = (0, 0)
        running = True
        while running:
            screen.fill("light green")
            for i in range(32, 640, 32):
                pygame.draw.line(screen, 000000, (i, 0), (i, 512))
            for j in range(32, 512, 32):
                pygame.draw.line(screen, 000000, (0, j), (640, j))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_location[0], mole_location[1])))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (mole_location[0] + 32) >= event.pos[0] >= (mole_location[0]) and (mole_location[1] + 32) >= event.pos[1] >= (mole_location[1]):
                        mole_location = (random.randrange(0, 19) * 32, random.randrange(0, 15) * 32)
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
