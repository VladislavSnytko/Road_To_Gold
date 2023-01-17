import pygame

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
purple = (255, 0, 255)
yellow = (255, 255, 0)


# Стенки
class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x


# Карта
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


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/coin.png').convert()

        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert()

        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.prev_x = x
        self.prev_y = y

    # Обновляет скорость игрока
    def prevdirection(self):
        self.prev_x = self.change_x
        self.prev_y = self.change_y

    # Меняет скорость игрока
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    # Находит местоположение игрока
    def update(self, walls, door):
        old_x = self.rect.left
        new_x = old_x + self.change_x
        prev_x = old_x + self.prev_x
        self.rect.left = new_x
        old_y = self.rect.top
        new_y = old_y + self.change_y
        prev_y = old_y + self.prev_y
        x_collide = pygame.sprite.spritecollide(self, walls, False)
        if x_collide:
            self.rect.left = old_x
        else:
            self.rect.top = new_y
            y_collide = pygame.sprite.spritecollide(self, walls, False)
            if y_collide:
                self.rect.top = old_y
        if door is not False:
            door_hit = pygame.sprite.spritecollide(self, door, False)
            if door_hit:
                self.rect.left = old_x
                self.rect.top = old_y


# Передвижение монстров
class Monster(Player):
    def changespeed_monster(self, list, monster, turn, steps, lst):
        try:
            z = list[turn][2]
            if steps < z:
                self.change_x = list[turn][0]
                self.change_y = list[turn][1]
                steps += 1
            else:
                if turn < lst:
                    turn += 1
                elif monster == "agro":
                    turn = 2
                else:
                    turn = 0
                self.change_x = list[turn][0]
                self.change_y = list[turn][1]
                steps = 0
            return [turn, steps]
        except IndexError:
            return [0, 0]


Skeleton_directions = [
    [0, -30, 4],
    [15, 0, 9],
    [0, 15, 11],
    [-15, 0, 23],
    [0, 15, 7],
    [15, 0, 3],
    [0, -15, 3],
    [15, 0, 19],
    [0, 15, 3],
    [15, 0, 3],
    [0, 15, 3],
    [15, 0, 3],
    [0, -15, 15],
    [-15, 0, 7],
    [0, 15, 3],
    [-15, 0, 19],
    [0, -15, 11],
    [15, 0, 9]
]

Goblin_directions = [
    [0, -15, 4],
    [15, 0, 9],
    [0, 15, 11],
    [15, 0, 3],
    [0, 15, 7],
    [-15, 0, 11],
    [0, 15, 3],
    [15, 0, 15],
    [0, -15, 15],
    [15, 0, 3],
    [0, -15, 11],
    [-15, 0, 3],
    [0, -15, 11],
    [-15, 0, 3],
    [0, -15, 3],
    [-15, 0, 7],
    [0, -15, 3],
    [15, 0, 15],
    [0, 15, 15],
    [-15, 0, 3],
    [0, 15, 3],
    [-15, 0, 3],
    [0, -15, 7],
    [-15, 0, 3],
    [0, 15, 7],
    [-15, 0, 11],
    [0, -15, 7],
    [15, 0, 5]
]

Crow_directions = [
    [30, 0, 2],
    [0, -15, 4],
    [15, 0, 10],
    [0, 15, 7],
    [15, 0, 3],
    [0, -15, 3],
    [15, 0, 3],
    [0, -15, 15],
    [-15, 0, 15],
    [0, 15, 3],
    [15, 0, 15],
    [0, 15, 11],
    [-15, 0, 3],
    [0, -15, 7],
    [-15, 0, 11],
    [0, 15, 3],
    [-15, 0, 11],
    [0, 15, 7],
    [-15, 0, 3],
    [0, -15, 3],
    [-15, 0, 3],
    [0, -15, 15],
    [15, 0, 15],
    [0, 15, 3],
    [-15, 0, 15],
    [0, 15, 11],
    [15, 0, 3],
    [0, -15, 11],
    [15, 0, 11],
    [0, 15, 3],
    [15, 0, 1],
]

Agro_directions = [
    [-30, 0, 2],
    [0, -15, 4],
    [15, 0, 5],
    [0, 15, 7],
    [-15, 0, 11],
    [0, -15, 7],
    [-15, 0, 3],
    [0, 15, 7],
    [-15, 0, 7],
    [0, 15, 15],
    [15, 0, 15],
    [0, -15, 3],
    [-15, 0, 11],
    [0, -15, 7],
    [15, 0, 3],
    [0, -15, 11],
    [15, 0, 9],
]

gl = len(Goblin_directions) - 1
sl = len(Skeleton_directions) - 1
crow_l = len(Crow_directions) - 1
al = len(Agro_directions) - 1

# Расположение монстров и игрока
width = 303 - 16  # положение по ширине
player_height = (7 * 60) + 19  # Высота гнома
monster_height = (4 * 60) + 19  # Высота монстра
goblin_height = (3 * 60) + 19  # Высота гоблина
Crow_width = 303 - 16 - 32  # Высота ворона
Agro_width = 303 + (32 - 16)  # Высота агро


def StartGame():
    # Создание спрайтов
    all_sprites_list = pygame.sprite.RenderPlain()

    monsta_list = pygame.sprite.RenderPlain()

    gnom_collide = pygame.sprite.RenderPlain()

    wall_list = setupRoom(all_sprites_list)

    door = setupDoor(all_sprites_list)

    coin_list = pygame.sprite.RenderPlain()

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

    # Заполнение поля монетами
    for row in range(19):
        for column in range(19):
            if (row == 7 or row == 8) and (column == 8 or column == 9 or column == 10):
                continue
            else:
                coin = Coin()
                coin.rect.x = (30 * column + 6) + 26
                coin.rect.y = (30 * row + 6) + 26

                # Проврка на столкновение спрайтов
                wall_collide = pygame.sprite.spritecollide(coin, wall_list, False)
                gnom_collide = pygame.sprite.spritecollide(coin, gnom_collide, False)
                if wall_collide:
                    continue
                elif gnom_collide:
                    continue
                else:
                    # COIN в список
                    coin_list.add(coin)
                    all_sprites_list.add(coin)

    # Для счетчика собранных монет
    coin_list_lenth = len(coin_list)

    score = 0
    game = False

    skel_turn = 0
    skel_steps = 0

    gobl_turn = 0
    gobl_steps = 0

    crow_turn = 0
    crow_steps = 0

    agro_turn = 0
    agro_steps = 0

    while game is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Gnom.changespeed(-30, 0)
                if event.key == pygame.K_RIGHT:
                    Gnom.changespeed(30, 0)
                if event.key == pygame.K_UP:
                    Gnom.changespeed(0, -30)
                if event.key == pygame.K_DOWN:
                    Gnom.changespeed(0, 30)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    Gnom.changespeed(30, 0)
                if event.key == pygame.K_RIGHT:
                    Gnom.changespeed(-30, 0)
                if event.key == pygame.K_UP:
                    Gnom.changespeed(0, 30)
                if event.key == pygame.K_DOWN:
                    Gnom.changespeed(0, -30)
        Gnom.update(wall_list, door)
        # Определение, каксается ли гном монеты
        coin_hit_list = pygame.sprite.spritecollide(Gnom, coin_list, True)

        # Реализация движения монстров
        returned = Skeleton.changespeed_monster(Skeleton_directions, False, skel_turn, skel_steps, gl)
        skel_turn = returned[0]
        skel_steps = returned[1]
        Skeleton.changespeed_monster(Skeleton_directions, False, skel_turn, skel_steps, gl)
        Skeleton.update(wall_list, False)

        returned = Goblin.changespeed_monster(Goblin_directions, False, gobl_turn, gobl_steps, sl)
        gobl_turn = returned[0]
        gobl_steps = returned[1]
        Goblin.changespeed_monster(Goblin_directions, False, gobl_turn, gobl_steps, sl)
        Goblin.update(wall_list, False)

        returned = Crow.changespeed_monster(Crow_directions, False, crow_turn, crow_steps, crow_l)
        crow_turn = returned[0]
        crow_steps = returned[1]
        Crow.changespeed_monster(Crow_directions, False, crow_turn, crow_steps, crow_l)
        Crow.update(wall_list, False)

        returned = Agro.changespeed_monster(Agro_directions, "agro", agro_turn, agro_steps, al)
        agro_turn = returned[0]
        agro_steps = returned[1]
        Agro.changespeed_monster(Agro_directions, "agro", agro_turn, agro_steps, al)
        Agro.update(wall_list, False)
        # Определение, каксается ли гном монстра
        monsta_hit_list = pygame.sprite.spritecollide(Gnom, monsta_list, False)
        # список взаимодействий
        if len(coin_hit_list) > 0:
            score += len(coin_hit_list)
        screen.fill(black)
        wall_list.draw(screen)
        door.draw(screen)
        all_sprites_list.draw(screen)
        monsta_list.draw(screen)
        # Счетчик монеток
        text = font.render("Score: " + str(score) + "/" + str(coin_list_lenth), True, red)
        screen.blit(text, [10, 616])

        if score == coin_list_lenth:
            doNext("Отчично, ты победил!", 145, all_sprites_list, coin_list, monsta_list, pacman_collide,
                   wall_list, door)
        if monsta_hit_list:
            doNext("Game Over", 235, all_sprites_list, coin_list, monsta_list, gnom_collide, wall_list, door)

        pygame.display.flip()
        clock.tick(10)

# экран выхода из игры или перезапуска игры
def doNext(message, left, all_sprites_list, block_list, monsta_list, pacman_collide, wall_list, gate):
    w = pygame.Surface((400, 200))
    w.set_alpha(300)
    w.fill((139, 0, 0))
    screen.blit(w, (100, 200))

    # Выиграл или проиграл
    text1 = font.render(message, True, white)
    screen.blit(text1, [left, 233])

    text2 = font.render("Для игры, нажмите ENTER.", True, white)
    screen.blit(text2, [135, 303])
    text3 = font.render("Для выхода ESCAPE.", True, white)
    screen.blit(text3, [165, 333])

    running = True

    while running:
        clock = pygame.time.Clock()
        pygame.display.flip()
        clock.tick(100)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RETURN:
                    del all_sprites_list
                    del block_list
                    del monsta_list
                    del pacman_collide
                    del wall_list
                    del gate
                    StartGame()
    pygame.quit()


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode([606, 656])

    pygame.display.set_caption('Road to gold')

    background = pygame.Surface(screen.get_size())

    background = background.convert()

    background.fill((139, 0, 0))

    pygame.font.init()
    font = pygame.font.Font("freesansbold.ttf", 24)

    clock = pygame.time.Clock()

    pygame.mixer.init()
    pygame.mixer.music.load('Music.mp3')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.01)

    StartGame()
