# Swimming with the fishes (Array Assignment)
# Contributor(s): Trevor Du
# Last Modified: May 1, 2020
#
# Mr. Fish goes to the school (ahahahaaha)
#
# This project uses the Boids algorithm as described here:
# https://www.red3d.com/cwr/boids/

import tkinter
import math
import time
import random


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    def normalize(self):
        return Vec2(self.x / self.magnitude(), self.y / self.magnitude())
    def scale(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)
    
    def normalize_(self):
        magnitude = self.magnitude()
        self.x /= magnitude
        self.y /= magnitude
    def scale_(self, scalar):
        self.x *= scalar
        self.y *= scalar
    
    def __add__(self, vec):
        return Vec2(self.x + vec.x, self.y + vec.y)
    def __sub__(self, vec):
        return Vec2(self.x - vec.x, self.y - vec.y)

    def __repr__(self):
        return "Vec2(" + str(self.x) + ", " + str(self.y) + ")"


class Screen(tkinter.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def draw_polygon(self, polygon, translation = [0, 0], rotation = 0):
        # Draw function that can apply translations and rotations.
        kwargs, vertices = polygon[0], polygon[1]
        
        # Apply translation and rotation.
        transformed_vertices = []
        for i in range(0, len(vertices), 2):
            transformed_x = vertices[i]*math.cos(rotation) - vertices[i + 1]*math.sin(rotation) + translation[0]
            transformed_y = vertices[i]*math.sin(rotation) + vertices[i + 1]*math.cos(rotation) + translation[1]
            transformed_vertices.extend([transformed_x, transformed_y])
        
        return self.create_polygon(*transformed_vertices, **kwargs)

# UTILITY FUNCTIONS
def clamp(n, minimum, maximum ):
    # Clamps n to be between maximum and minimum.
    return min(max(n, minimum), maximum)


# CONSTANTS
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

BOID = [{"fill": "coral", "outline": "black"}, [0, -4, 6, 0, 0, 4, -12, 0, -16, 4, -16, -4, -12, 0]]
N_BOIDS = 50
BOID_SPEED = 3                  # pixels/frame
BOID_MAX_SPEED = 6              # pixels/frame
SENSE_RADIUS = 50               # pixels
REGION_WIDTH = 100              # pixels

N_REGIONS_ACROSS = SCREEN_WIDTH // REGION_WIDTH
N_REGIONS_ALONG = SCREEN_HEIGHT // REGION_WIDTH

BOUND_X1 = 50                     # pixels
BOUND_Y1 = 270                    # pixels
BOUND_X2 = SCREEN_WIDTH - 50      # pixels
BOUND_Y2 = SCREEN_HEIGHT - 135    # pixels

DESIRED_SEPARATION = 10        # pixels
BOUND_REPULSION = 2.75         # How much being past the boundaries affects a boid's velocity.
AIR_FACTOR = 3                 # Multiplication factor for BOUND_REPULSION if fish is outside of water.

# Scale factors for boid rules.
SEPARATION_SCALE = 0.1
COHESION_SCALE = 0.01
ALIGNMENT_SCALE = 0.15

N_KELP = 8

root = tkinter.Tk()
screen = Screen(master = root, height = SCREEN_HEIGHT, width = SCREEN_WIDTH, background = "#06aeac")
screen.pack()

# DRAW STATIC OBJECTS

# Sky
screen.create_rectangle(0, 0, SCREEN_WIDTH + 5, 250, fill = "sky blue", outline = "#02aa9f")

# Waves
circle_x = 0
radius = 40
while circle_x <= SCREEN_WIDTH:
    screen.create_oval(circle_x - radius, 250 - 20, circle_x + radius, 250 + 20, fill = "sky blue", outline = "sky blue")
    circle_x += 2*radius

# Background Kelp
leaf_colours = [
    ["#446c22", "#316730", "#438b36"],
    ["#546c22", "#416730", "#538b36"],
    ["#6f7b0c", "#586110", "#638215"]
]

kelps_x = [
    [], # Layer 1
    [], # Layer 2
    [] # Layer 3
]
for _ in range(N_KELP):
    kelp_x = random.randint(0, SCREEN_WIDTH)
    kelps_x[min(random.randint(0, 4), 2)].append(kelp_x)

# Seabed

# Layer 1
for kelp_x in kelps_x[0]:
    top_y = 400 + random.randint(2, 40)
    
    y1 = SCREEN_HEIGHT
    while y1 > top_y:
        y2 = clamp(y1 - 12, top_y, SCREEN_HEIGHT)
        screen.create_polygon(kelp_x - random.randint(10, 24), (y1 + y2) / 2, kelp_x, y1, kelp_x + random.randint(10, 24), (y1 + y2) / 2, kelp_x, y2, fill = random.choice(leaf_colours[0]))
        y1 -= random.randint(4, 8)
    
    screen.create_line(kelp_x, SCREEN_HEIGHT, kelp_x, top_y, width = 4, fill = "#316556")

# Layer 2
screen.create_polygon(0, SCREEN_HEIGHT - 120,  700, SCREEN_HEIGHT - 150, SCREEN_WIDTH + 5, SCREEN_HEIGHT - 100, SCREEN_WIDTH + 5, SCREEN_HEIGHT, 0, SCREEN_HEIGHT, fill = "#889b84")
for kelp_x in kelps_x[1]:
    top_y = 350 + random.randint(2, 40)
    
    y1 = SCREEN_HEIGHT
    while y1 > top_y:
        y2 = clamp(y1 - 12, top_y, SCREEN_HEIGHT)
        screen.create_polygon(kelp_x - random.randint(10, 24), (y1 + y2) / 2, kelp_x, y1, kelp_x + random.randint(10, 24), (y1 + y2) / 2, kelp_x, y2, fill = random.choice(leaf_colours[1]))
        y1 -= random.randint(4, 8)
    
    screen.create_line(kelp_x, SCREEN_HEIGHT, kelp_x, top_y, width = 4, fill = "#435747")

screen.create_polygon(0, SCREEN_HEIGHT, 0, SCREEN_HEIGHT - 120, 200, SCREEN_HEIGHT - 135, SCREEN_WIDTH + 5, SCREEN_HEIGHT, fill = "#9ea97f")
screen.create_polygon(0, SCREEN_HEIGHT - 100, 400, SCREEN_HEIGHT - 120, SCREEN_WIDTH + 5, SCREEN_HEIGHT - 80, SCREEN_WIDTH + 5, SCREEN_HEIGHT, 0, SCREEN_HEIGHT, fill = "#decc92")

# Layer 3
# This layer is different: it will be drawn in front of the fish.
# All polygon and line vertices will be stored in arrays.
fg_kelp_leaves = []
fg_kelp_stalks = []
fg_kelp_drawn = []
for kelp_x in kelps_x[2]:
    top_y = 300 + random.randint(2, 40)
    base_y = SCREEN_HEIGHT - random.randint(10, 50)
    
    y1 = base_y - random.randint(10, 20)
    while y1 > top_y:
        y2 = clamp(y1 - 12, top_y, SCREEN_HEIGHT)
        fg_kelp_leaves.append([[kelp_x - random.randint(10, 24), (y1 + y2) / 2, kelp_x, y1, kelp_x + random.randint(10, 24), (y1 + y2) / 2, kelp_x, y2], random.choice(leaf_colours[2])])
        y1 -= random.randint(4, 8)
    
    fg_kelp_stalks.append([kelp_x, base_y, kelp_x, top_y])


# 2D array that stores info on which region a boid is in.
# A region is a REGION_WIDTH x REGION_WIDTH square in the screen.
# A point (x, y) is contained within the region regions[i][j] if 
# floor(x / REGION_WIDTH) = j
# floor(y / REGION_WIDTH) = i

# The coordinates of the top-left corner of the region regions[i][j] is (x, y) where
# x = j*REGION_WIDTH
# y = i*REGION_WIDTH

# Individual boids are identified by a unique integer between 0 and N_BOIDS.
# Each boid's integer is the index for their values in the arrays boids_pos, boids_angle.
regions = [[[] for _ in range(SCREEN_WIDTH // REGION_WIDTH)] for _ in range(SCREEN_HEIGHT // REGION_WIDTH)]

boids_pos = []
boids_velocity = []
boids_region = []
boids = []

# Initialize arrays with starting values.
for boid in range(N_BOIDS):
    boid_angle = math.radians(random.randint(0, 359))

    boids_pos.append(Vec2(random.randint(0, SCREEN_WIDTH - 1), random.randint(250, SCREEN_HEIGHT - 100)))
    boids_velocity.append(Vec2(math.cos(boid_angle), math.sin(boid_angle)).scale(BOID_SPEED))
    boids.append(0)

    boid_region_j = boids_pos[boid].x // REGION_WIDTH
    boid_region_i = boids_pos[boid].y // REGION_WIDTH

    boids_region.append([boid_region_i, boid_region_j])
    regions[boid_region_i][boid_region_j].append(boid)


for _ in range(10000):
    # Update boid velocity according to boid rules.
    # Boid Rules:
    #   - Separation: Avoid nearby boids.
    #   - Cohesion: Steer towards the average direction of nearby boids.
    #   - Alignment: Move towards average position of nearby boids.
    for boid in range(N_BOIDS):
        boid_pos = boids_pos[boid]

        # Finding all boids in sensing radius.
        nearby_boids = []
        for i in range(len(regions)):
            for j in range(len(regions[i])):
                if len(regions[i][j]) > 0:
                    # Find the distance between the boid and the closest point (point P) on the rectangle.
                    region_x1 = j*REGION_WIDTH
                    region_y1 = i*REGION_WIDTH

                    # Calculate the closest point on the perimetre of the region.
                    P = Vec2(
                        clamp(boid_pos.x, region_x1, region_x1 + REGION_WIDTH),
                        clamp(boid_pos.y, region_y1, region_y1 + REGION_WIDTH)
                    )

                    if (boid_pos - P).magnitude() < SENSE_RADIUS:
                        for nearby_boid in regions[i][j]:
                            if nearby_boid != boid and (boids_pos[nearby_boid] - boid_pos).magnitude() < SENSE_RADIUS:
                                nearby_boids.append(nearby_boid)
        
        # Update velocity with boid rules.
        separation = Vec2(0, 0)
        cohesion = Vec2(0, 0)
        alignment = Vec2(0, 0)
        bound_avoidance = Vec2(0, 0)

        # 1. Separation
        for nearby_boid in nearby_boids:
            if (boid_pos - boids_pos[nearby_boid]).magnitude() < DESIRED_SEPARATION:
                separation += boid_pos - boids_pos[nearby_boid]
        
        # 2. Cohesion
        if len(nearby_boids) > 0:
            avg_pos = Vec2(0, 0)
            for nearby_boid in nearby_boids:
                avg_pos = avg_pos + boids_pos[nearby_boid]
            avg_pos.scale_(1/len(nearby_boids))
            cohesion = avg_pos - boid_pos
        
        # 3. Alignment
        if len(nearby_boids) > 0:
            avg_velocity = Vec2(0, 0)
            for nearby_boid in nearby_boids:
                avg_velocity = avg_velocity + boids_velocity[nearby_boid]
            avg_velocity.scale_(1/len(nearby_boids))
            alignment = avg_velocity
        
        # A fourth vector that changes the velocity 
        # so that boids move away from the boundaries.
        if boid_pos.x < BOUND_X1:
            bound_avoidance.x = BOUND_REPULSION
        elif boid_pos.x > BOUND_X2:
            bound_avoidance.x = -BOUND_REPULSION
        if boid_pos.y < BOUND_Y1:
            bound_avoidance.y = BOUND_REPULSION * AIR_FACTOR
        elif boid_pos.y > BOUND_Y2:
            bound_avoidance.y = -BOUND_REPULSION
        
        # Scale vectors
        separation.scale_(SEPARATION_SCALE)
        cohesion.scale_(COHESION_SCALE)
        alignment.scale_(ALIGNMENT_SCALE)

        # Update velocity with separation, cohesion, and alignment.
        boids_velocity[boid] = boids_velocity[boid] + separation + cohesion + alignment + bound_avoidance
        if boids_velocity[boid].magnitude() == 0:
            # In case we get unlucky and the boid rules makes the velocity's magnitude go to zero.
            boids_velocity[boid] = Vec2(0,-0.1) # Fish floats upwards

        boids_velocity[boid] = boids_velocity[boid].normalize().scale(clamp(boids_velocity[boid].magnitude(), 0.1, BOID_MAX_SPEED))

    # Loop through boids and update positions.
    for boid in range(N_BOIDS):
        boid_pos = boids_pos[boid]
        boid_velocity = boids_velocity[boid]
        prev_boid_region = boids_region[boid]
        boid_angle = math.atan2(boid_velocity.y, boid_velocity.x)

        boids[boid] = screen.draw_polygon(BOID, translation = [boid_pos.x, boid_pos.y], rotation = boid_angle)

        # Update boid position.
        boids_pos[boid] = boid_pos + boid_velocity

        # Check if boid has entered a new region.
        boid_region_i = clamp(int(boid_pos.y / REGION_WIDTH), 0, N_REGIONS_ACROSS - 1)
        boid_region_j = clamp(int(boid_pos.x / REGION_WIDTH), 0, N_REGIONS_ALONG - 1)
        if prev_boid_region != [boid_region_i, boid_region_j]:
            regions[prev_boid_region[0]][prev_boid_region[1]].remove(boid)
            regions[boid_region_i][boid_region_j].append(boid)
            boids_region[boid] = [boid_region_i, boid_region_j]
    
    # Draw foreground kelp
    for polygon, leaf_colour in fg_kelp_leaves:
        fg_kelp_drawn.append(screen.create_polygon(*polygon, fill = leaf_colour))
    for line in fg_kelp_stalks:
        fg_kelp_drawn.append(screen.create_line(*line, fill = "#3a3f2c", width = 5))

    screen.update()
    time.sleep(0.03)
    screen.delete(*boids)
    screen.delete(*fg_kelp_drawn)

    fg_kelp_drawn.clear()

root.mainloop()
