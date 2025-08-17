import pygame
import sys
import random
import time


class Game2:
    def __init__(self):
        pygame.init()
        self.window_width = 800
        self.window_height = 600
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Let Us Play Pong")
        self.clock = pygame.time.Clock()
        self.player1 = Player1(self, 775, 490)
        self.player2 = Player2(self, 10, 490)
        self.ball = Ball(self, 400, 300)
        self.score = Score()
        self.run()

    def run(self):
        running = True
        start_time = time.time()  # Timer

        pygame.mixer.music.load("Eisenfunk - Pong.mp3")
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(.3)

        while running:
            elapsed_time = time.time() - start_time
            if elapsed_time >= 180:
                # print("Zeit ist um!")  # ggf game over screen
                running = False  # bis hier

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            self.delta_time = self.clock.tick(60) / 1000
            self.window.fill((25, 25, 25))
            self.player1.update()
            self.player2.update()
            self.ball.checkCollision(self.player1, self.player2, self.score)
            self.ball.update()
            self.score.draw(self.window)
            pygame.display.update()

class Player1:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.surface = game.window
        self.rect = pygame.Rect(self.x, self.y, 15, 100)

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 15, 100)
        self.movement(300)
        self.draw()

    def draw(self):
        pygame.draw.rect(self.surface, "green", self.rect)

    def movement(self, speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.y += speed * self.game.delta_time
        elif keys[pygame.K_UP]:
            self.y -= speed * self.game.delta_time
        if self.y < 0:
            self.y = 0
        elif self.y > self.game.window.get_height() - 100:
            self.y = self.game.window.get_height() - 100

class Player2:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.surface = game.window
        self.rect = pygame.Rect(self.x, self.y, 15, 100)

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 15, 100)
        self.movement()
        self.draw()

    def draw(self):
        pygame.draw.rect(self.surface, "red", self.rect)

    def movement(self):

        if self.y < self.game.ball.y - 10:                              #dat hier
            self.y += 200 * self.game.delta_time
        elif self.y > self.game.ball.y + 10:
            self.y -= 200 * self.game.delta_time


        if random.random() < 0.1:                               # 10%
            self.y += random.choice([-20, 20])            # oben unten

        if self.y < 0:
            self.y = 0
        elif self.y > self.game.window.get_height() - 100:
            self.y = self.game.window.get_height() - 100

class Score:
    counterP1 = 0
    counterP2 = 0

    def draw(self, screen):
        score_pl1 = pygame.font.SysFont("comicsansms", 40).render(str(self.counterP1), True, (57, 255, 20))
        score_pl2 = pygame.font.SysFont("comicsansms", 40).render(str(self.counterP2), True, (57, 255, 20))

        screen.blit(score_pl1, (screen.get_width() * 0.25, 70))
        screen.blit(score_pl2, (screen.get_width() * 0.75, 70))

class Ball:
    def __init__(self, game, x, y, yDir=True, xDir=True):
        self.x = x
        self.y = y
        self.yDir = yDir
        self.xDir = xDir
        self.game = game
        self.surface = game.window
        self.rect = pygame.Rect(self.x, self.y, 15, 15)

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 15, 15)
        self.movement(300)
        self.draw()

    def draw(self):
        pygame.draw.rect(self.surface, "green", self.rect)

    def movement(self, speed):
        if self.xDir:
            self.x += 3
        else:
            self.x -= 3

        if self.yDir:
            self.y += 3
        else:
            self.y -= 3

    def checkCollision(self, player1, player2, score):
        if self.y <= 0 or self.y >= self.game.window.get_height() - 15:
            self.yDir = not self.yDir

        if self.rect.colliderect(player1.rect):
            self.xDir = False

        if self.rect.colliderect(player2.rect):
            self.xDir = True

        if self.x < 0:
            score.counterP2 += 1
            self.x = 400
            self.y = 300
            self.xDir = True

        if self.x > self.game.window.get_width():
            score.counterP1 += 1
            self.x = 400
            self.y = 300
            self.xDir = False

#game = Game2()
pygame.quit()
