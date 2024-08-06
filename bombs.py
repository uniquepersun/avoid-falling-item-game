import pygame
import random

pygame.init()

# variables here
WIDTH, HEIGHT = 800, 600
DOT_SIZE = 20
OBSTACLE_SIZE = 30
OBSTACLE_SPEED = 5
DOT_SPEED = 10
NUM_OBSTACLES = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("avoid falling items!!")

def draw_objects(dot, obstacles):
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, dot)
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()


    dot = pygame.Rect(WIDTH // 2 - DOT_SIZE // 2, HEIGHT - DOT_SIZE - 10, DOT_SIZE, DOT_SIZE)

    obstacles = [pygame.Rect(random.randint(0, WIDTH - OBSTACLE_SIZE), random.randint(-HEIGHT, -OBSTACLE_SIZE), OBSTACLE_SIZE, OBSTACLE_SIZE) for _ in range(NUM_OBSTACLES)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and dot.left > 0:
            dot.x -= DOT_SPEED
        if keys[pygame.K_RIGHT] and dot.right < WIDTH:
            dot.x += DOT_SPEED

        for obstacle in obstacles:
            obstacle.y += OBSTACLE_SPEED

        # Check if obstacles are off screen or hit the dot
        for obstacle in obstacles[:]:
            if obstacle.top > HEIGHT:
                obstacles.remove(obstacle)
                new_obstacle = pygame.Rect(random.randint(0, WIDTH - OBSTACLE_SIZE), random.randint(-OBSTACLE_SIZE, -OBSTACLE_SIZE), OBSTACLE_SIZE, OBSTACLE_SIZE)
                obstacles.append(new_obstacle)
            if obstacle.colliderect(dot):
                print("Game Over!")
                running = False

        draw_objects(dot, obstacles)

        clock.tick(30)  # Limit to 30 frames per second

    pygame.quit()

if __name__ == "__main__":
    main()
