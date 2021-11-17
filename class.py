import pygame as pg
import random
import math
import settings


class Star:
    def __init__(self, app, COLORS, Z_DISTANCE):
        self.screen = app.screen
        self.Z_DISTANCE = Z_DISTANCE
        self.pos3d = self.get_pos3d()

        if settings.MODE == 'space':
            self.vel = random.uniform(0.05, 0.25)
        elif settings.MODE == 'portal':
            self.vel = random.uniform(0.45, 0.95)

        self.color = random.choice(COLORS)
        self.screen_pos = settings.vec2(0, 0)
        self.size = 10

    def get_pos3d(self, scale_pos=35):
        angle = random.uniform(0, 2 * math.pi)
        if settings.MODE == 'space':
            radius = random.randrange(settings.HEIGHT // scale_pos, settings.HEIGHT) * scale_pos
        elif settings.MODE == 'portal':
            radius = random.randrange(settings.HEIGHT // 4, settings.HEIGHT // 3) * scale_pos

        x = radius * math.sin(angle)
        y = radius * math.cos(angle)

        return settings.vec3(x, y, self.Z_DISTANCE)

    def update(self):
        self.pos3d.z -= self.vel
        self.pos3d = self.get_pos3d() if self.pos3d.z < 1 else self.pos3d
        self.screen_pos = settings.vec2(self.pos3d.x, self.pos3d.y) / self.pos3d.z  + settings.CENTER
        self.size = (self.Z_DISTANCE - self.pos3d.z) / (0.2 * self.pos3d.z)
        self.pos3d.xy = self.pos3d.xy.rotate(0.2)
        mouse_pos = settings.CENTER - settings.vec2(pg.mouse.get_pos())
        self.screen_pos += mouse_pos

    def draw(self):
        pg.draw.rect(self.screen, self.color, (*self.screen_pos, self.size, self.size))


class Starfield:
    def __init__(self, app, NUM_STARS, Z_DISTANCE, COLORS):
        self.stars = [Star(app, Z_DISTANCE, COLORS) for _ in range(NUM_STARS)]

    def run(self):
        for star in self.stars:
            star.update()

        self.stars.sort(key=lambda star: star.pos3d.z, reverse=True)

        for star in self.stars:
            star.draw()


class App:
    def __init__(self, NUM_STARS, ALPHA, Z_DISTANCE, COLORS):
        self.screen = pg.display.set_mode(settings.RES)
        self.alpha_surface = pg.Surface(settings.RES)
        self.alpha_surface.set_alpha(ALPHA)
        self.clock = pg.time.Clock()
        self.starfield = Starfield(self, NUM_STARS, Z_DISTANCE, COLORS)

    def run(self):
        while True:
            self.screen.blit(self.alpha_surface, (0, 0))
            self.starfield.run()

            pg.display.flip()
            [exit() for e in pg.event.get() if e.type == pg.QUIT]
            self.clock.tick(60)


def main():
    if settings.MODE == 'space':
        return App(settings.NUM_STARS, settings.SPACE_ALPHA, settings.SPACE_Z_DISTANCE, settings.SPACE_COLORS)

    elif settings.MODE == 'portal':      
        return App(settings.NUM_STARS, settings.PORTAL_ALPHA, settings.PORTAL_Z_DISTANCE, settings.PORTAL_COLORS)



if __name__ == '__main__':
    app = main()
    app.run()
