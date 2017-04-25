import sys, pygame
from random import randint
from time import time
from math import floor

pygame.init()

size = width, height = 800, 600
speed = [2, 2]
white = 255, 255, 255

screen = pygame.display.set_mode(size)

ground = 600 - 200

class Player(object):
    left_key = None
    right_key = None
    jump_key = None
    crouch_key = None
    punch_key = None
    kick_key = None
    sprite = None

    def __init__(self, x, y):
        self.image = None
        self.rect = None

        self.x = x
        self.y = y

        self.vx = 0
        self.vy = 0

        self.sprite_xscale = 1
        self.sprite_yscale = 1

        self.gravity = 0.01
        self.speed = 2

    def initialize(self):
        self.image = pygame.image.load(self.sprite)
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.image_stands = [pygame.image.load("sprites/stand1.png"),
                            pygame.image.load("sprites/stand2.png"),
                            pygame.image.load("sprites/stand3.png")]
        self.image_walks = [pygame.image.load("sprites/walk1.png"),
                            pygame.image.load("sprites/walk2.png")]
        self.image_punch = pygame.image.load("sprites/punch1.png")
        self.image_kick = pygame.image.load("sprites/kick1.png")


        self.rect = self.image.get_rect()

    def process_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[self.left_key]:
            self.x -= self.speed
            self.sprite_xscale = 1
        if keys[self.right_key]:
            self.x += self.speed
            self.sprite_xscale = -1
        if keys[self.jump_key]:
            if self.y + 50 <= ground and self.y + 50 + 4 >= ground:
                self.vy = -2
        if keys[self.crouch_key]:
            self.image = pygame.transform.scale(self.image, (100, 100))

    def step(self):
        # Process step
        self.x += self.vx
        self.y += self.vy

        self.vy += self.gravity

        # Process collisions
        if self.y + 50 > ground:
            self.y = ground - 50
            self.vy = 0

        # Update rectangle
        self.rect.center = (self.x, self.y)
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        keys = pygame.key.get_pressed()

        # Draw body
        if keys[self.left_key] or keys[self.right_key]:
            t = time()
            i = floor((t - floor(t)) * 18) % 2
            image = self.image_walks[i]
        else:
            t = time()
            i = floor((t - floor(t)) * 18) % 3
            image = self.image_stands[i]

        rect = image.get_rect()
        rect.x = self.x
        rect.y = self.y

        image = pygame.transform.flip(image,
                                      self.sprite_xscale < 0,
                                      self.sprite_yscale < 0)
        screen.blit(image, rect)

        # Draw head
        image = player.image
        rect = image.get_rect()
        rect.x = self.x
        rect.y = self.y

        if keys[self.crouch_key]:
            image = pygame.transform.scale(self.image, (100, 50))
            rect.y += image.get_size()[1]

        image = pygame.transform.flip(image,
                                      self.sprite_xscale < 0,
                                      self.sprite_yscale < 0)

        screen.blit(image, rect)

class Lam(Player):
    def __init__(self, x, y):
        Player.__init__(self, x, y)
        self.left_key = pygame.K_LEFT
        self.right_key = pygame.K_RIGHT
        self.jump_key = pygame.K_UP
        self.crouch_key = pygame.K_DOWN
        self.punch_key = pygame.K_z
        self.kick_key = pygame.K_x
        self.sprite = "sprites/lam.png"
        self.initialize()

class Richard(Player):
    def __init__(self, x, y):
        Player.__init__(self, x, y)
        self.left_key = pygame.K_LEFT
        self.right_key = pygame.K_RIGHT
        self.jump_key = pygame.K_UP
        self.crouch_key = pygame.K_DOWN
        self.punch_key = pygame.K_z
        self.kick_key = pygame.K_x
        self.sprite = "sprites/richard.png"
        self.initialize()

class Rhett(Player):
    def __init__(self, x, y):
        Player.__init__(self, x, y)
        self.left_key = pygame.K_LEFT
        self.right_key = pygame.K_RIGHT
        self.jump_key = pygame.K_UP
        self.crouch_key = pygame.K_DOWN
        self.punch_key = pygame.K_z
        self.kick_key = pygame.K_x
        self.sprite = "sprites/rhett.png"
        self.initialize()

class Christian(Player):
    def __init__(self, x, y):
        Player.__init__(self, x, y)
        self.left_key = pygame.K_LEFT
        self.right_key = pygame.K_RIGHT
        self.jump_key = pygame.K_UP
        self.crouch_key = pygame.K_DOWN
        self.punch_key = pygame.K_z
        self.kick_key = pygame.K_x
        self.sprite = "sprites/christian.png"
        self.initialize()

players = [
        Rhett(100, 300),
        Lam(200, 300),
        Richard(300, 300),
        Christian(400, 300)
        ]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #elif event.type == pygame.KEYDOWN:
    for player in players:
        player.process_inputs()

    # Step
    for player in players:
        player.step()

    # Draw
    screen.fill(white)
    for player in players:
        player.draw(screen)

    # Render
    pygame.display.flip()
