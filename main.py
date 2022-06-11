import pygame, sys

width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('To the Depths!')

pygame.init()


class Player():
    def __init__(self, x, y, Pwidth, Pheight, color):
        self.x = x
        self.y = y
        self.width = Pwidth
        self.height = Pheight
        self.color = color
        self.rect = (x, y, Pwidth, Pheight)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            self.x -= self.vel
        if key_input[pygame.K_UP]:
            self.y -= self.vel
        if key_input[pygame.K_RIGHT]:
            self.x += self.vel
        if key_input[pygame.K_DOWN]:
            self.y += self.vel
        self.rect = (self.x, self.y, self.width, self.height)


def redrawWindow(window, player):

    window.fill((255, 128, 255))
    player.draw(window)
    pygame.display.update()


def main():
    run = True
    p = Player(50, 50, 100, 100, (128, 128, 64))
    clock = pygame.time.Clock()
    # Event loop
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(window, p)


if __name__ == '__main__':
    main()
