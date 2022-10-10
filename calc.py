from ast import Or
import pygame as pg
import math

pg.init()

LGRAY = (160, 160, 160)
DGRAY = (49, 49, 49)
ORANGE = (246, 153, 6)
WHITE = (255, 255, 255)

TFONT = pg.font.SysFont(None, 128)
BFONT = pg.font.SysFont(None, 64)


class Button:
    def __init__(self, value: str, x: int, y: int, color: tuple[int, int, int]):
        self.value = value
        self.x = x
        self.y = y
        self.radius = 45
        self.color = color

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        font = BFONT.render(str(self.value), True, WHITE)
        screen.blit(
            font,
            (
                self.x - (font.get_rect().width / 2),
                self.y - (font.get_rect().height / 2),
            ),
        )


def click(buttons: list[Button], mouse_pos: pg.Vector2):
    for b in buttons:
        if (mouse_pos.x - b.x) ** 2 + (mouse_pos.y - b.y) ** 2 < b.radius**2:
            return b
    return None


def render(screen, buttons, total):
    for b in buttons:
        b.draw(screen)
    font = TFONT.render(str(total), True, WHITE)
    screen.blit(font, (0, 250))


if __name__ == "__main__":
    buttons: list[Button] = []
    values = [
        ["AC", "+/-", "%", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", "pi", ".", "="],
    ]
    colors = [
        [LGRAY, LGRAY, LGRAY, ORANGE],
        [DGRAY, DGRAY, DGRAY, ORANGE],
        [DGRAY, DGRAY, DGRAY, ORANGE],
        [DGRAY, DGRAY, DGRAY, ORANGE],
        [DGRAY, DGRAY, DGRAY, ORANGE],
    ]
    for y in range(5):
        for x in range(4):
            buttons.append(
                Button(
                    values[y][x],
                    ((x * 90) + 10) + 55,
                    ((y * 90) + 10) + 370,
                    colors[y][x],
                )
            )

    ##########################################################################################
    total = 0

    screen = pg.display.set_mode((400, 800))

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            keys = pg.key.get_pressed()
            if keys[pg.K_LCTRL]:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                MousePos = pg.Vector2(*pg.mouse.get_pos())
                clicked = click(buttons, MousePos)
                if clicked is not None:
                    print(clicked.value)

        screen.fill((0, 0, 0))

        render(screen, buttons, total)

        pg.display.flip()
