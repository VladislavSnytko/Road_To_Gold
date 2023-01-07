import pygame

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
purple = (255, 0, 255)
yellow = (255, 255, 0)


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x


def setupRoom(all_sprites_list):
    # Создание списка спрайтов для стен
    wall_list = pygame.sprite.RenderPlain()

    # Создание стен
    walls = [[0, 0, 8, 600],
             [0, 0, 600, 6],
             [0, 600, 606, 6],
             [600, 0, 6, 606],
             [300, 0, 6, 66],
             [60, 60, 186, 6],
             [360, 60, 186, 6],
             [60, 120, 66, 6],
             [60, 120, 6, 126],
             [180, 120, 246, 6],
             [300, 120, 6, 66],
             [480, 120, 66, 6],
             [540, 120, 6, 126],
             [120, 180, 126, 6],
             [120, 180, 6, 126],
             [360, 180, 126, 6],
             [480, 180, 6, 126],
             [180, 240, 6, 126],
             [180, 360, 246, 6],
             [420, 240, 6, 126],
             [240, 240, 42, 6],
             [324, 240, 42, 6],
             [240, 240, 6, 66],
             [240, 300, 126, 6],
             [360, 240, 6, 66],
             [0, 300, 66, 6],
             [540, 300, 66, 6],
             [60, 360, 66, 6],
             [60, 360, 6, 186],
             [480, 360, 66, 6],
             [540, 360, 6, 186],
             [120, 420, 366, 6],
             [120, 420, 6, 66],
             [480, 420, 6, 66],
             [180, 480, 246, 6],
             [300, 480, 6, 66],
             [120, 540, 126, 6],
             [360, 540, 126, 6]
             ]

    for item in walls:
        wall = Wall(item[0], item[1], item[2], item[3], purple)
        wall_list.add(wall)
        all_sprites_list.add(wall)

    # Список стен
    return wall_list


def setupDoor(all_sprites_list):
    door = pygame.sprite.RenderPlain()
    door.add(Wall(282, 242, 42, 2, white))
    all_sprites_list.add(door)
    return door


class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert()

        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x


class Monster(Player):
    def changespeed_monster(self):
        pass


# Расположение пакмена и монстров

width = 303 - 16  # Width
player_height = (7 * 60) + 19  # Pacman height
monster_height = (4 * 60) + 19  # Monster height
goblin_height = (3 * 60) + 19  # Binky height
Crow_width = 303 - 16 - 32  # Inky width
Agro_width = 303 + (32 - 16)  # Clyde width


def StartGame():
    # Создание спрайтов
    all_sprites_list = pygame.sprite.RenderPlain()

    monsta_list = pygame.sprite.RenderPlain()

    gnom_collide = pygame.sprite.RenderPlain()

    wall_list = setupRoom(all_sprites_list)

    door = setupDoor(all_sprites_list)

    # Создание монстров
    Gnom = Player(width, player_height, "images/Gnom.png")
    all_sprites_list.add(Gnom)
    gnom_collide.add(Gnom)

    Goblin = Monster(width, goblin_height, "images/goblin.png")
    monsta_list.add(Goblin)
    all_sprites_list.add(Goblin)

    Skeleton = Monster(width, monster_height, "images/Skeleton.png")
    monsta_list.add(Skeleton)
    all_sprites_list.add(Skeleton)

    Crow = Monster(Crow_width, monster_height, "images/Crow.png")
    monsta_list.add(Crow)
    all_sprites_list.add(Crow)

    Agro = Monster(Agro_width, monster_height, "images/Agro.png")
    monsta_list.add(Agro)
    all_sprites_list.add(Agro)

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        screen.fill(black)
        wall_list.draw(screen)
        door.draw(screen)
        all_sprites_list.draw(screen)
        monsta_list.draw(screen)

        pygame.display.flip()
        clock.tick(10)


running = True


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode([606, 656])

    pygame.display.set_caption('Road to gold')

    background = pygame.Surface(screen.get_size())

    background = background.convert()

    background.fill((139, 0, 0))

    clock = pygame.time.Clock()

    StartGame()
