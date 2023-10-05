import pygame
def main():
    pygame.init()

    width = 800
    height = 600

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill((255, 255, 255))

        pygame.display.flip()


    pygame.quit()


if __name__ == '__main__':
    main()
