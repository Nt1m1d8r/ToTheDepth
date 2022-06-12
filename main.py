import pygame

width = 1200
height = 700
white = (255, 255, 255)
blockSize = 50 #Set the size of the grid block
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('To the Depths!')
icon = pygame.image.load('Spudd_Button.png')
pygame.display.set_icon(icon)
pygame.init()


def drawGrid():
    for x in range(50, (width - 50), blockSize):
        for y in range(50, (height - 2 * blockSize), blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(window, white, rect, 1)


class Player():
    def __init__(self, x, y, Pwidth, Pheight, color):
        self.x = x
        self.y = y
        self.width = Pwidth
        self.height = Pheight
        self.color = color
        self.rect = (x, y, Pwidth, Pheight)
        self.step = blockSize

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            if (self.x - self.step) >= 0:
                self.x -= self.step
        #if key_input[pygame.K_UP]:
        #    if (self.y - self.step) >= 0:
        #        self.y -= self.step
        #if key_input[pygame.K_RIGHT]:
        #    if (self.x + self.step) < width:
        #        self.x += self.step
        #if key_input[pygame.K_DOWN]:
        #    if (self.y + self.step) < height:
        #        self.y += self.step
        self.rect = (self.x, self.y, self.width, self.height)


def redrawWindow(window, player):

    window.fill((0, 0, 0))
    drawGrid()
    player.draw(window)
    pygame.display.update()


def main():
    run = True
    p = Player((width / 2), (height / 2), 50, 50, (128, 128, 64))
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
