import pygame as pg

# You can edit this file entirely except variables: vec2, vec3 and CENTER

# Screen resolution
RES = WIDTH, HEIGHT = 1366, 768

# Don't edit vec2, vec3 and CENTER!!
vec2 = pg.math.Vector2
vec3 = pg.math.Vector3
CENTER = vec2(WIDTH // 2, HEIGHT // 2)

# Space mode colors
SPACE_COLORS = "red green blue orange purple cyan".split()
# Portal mode colors
PORTAL_COLORS = "blue cyan skyblue purple magenta".split()

# Alpha for portal mode
PORTAL_ALPHA = 30
# Z_Distance for portal mode
PORTAL_Z_DISTANCE = 140

# Alpha for space mode
SPACE_ALPHA = 120
# Z_Distance for space mode
SPACE_Z_DISTANCE = 40

# Num of stars
NUM_STARS = 2000

# There is a two mode: space and portal
MODE = 'portal'
