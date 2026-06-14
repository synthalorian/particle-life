import pygame
import numpy as np
from particles import ParticleArray, SPECIES

class PygameRenderer:
    def __init__(self, width: int = 800, height: int = 600, fps: int = 60):
        pygame.init()
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("PARTICLE LIFE — v1")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 14)

    def draw(self, particles: ParticleArray, show_stats: bool = True):
        self.screen.fill((10, 10, 15))

        # Draw particles as small circles
        for i in range(particles.n):
            if not particles.active[i]:
                continue
            x = int(particles.x[i])
            y = int(particles.y[i])
            sp = particles.species[i]
            color = SPECIES[sp].color
            radius = max(2, int(SPECIES[sp].radius))
            pygame.draw.circle(self.screen, color, (x, y), radius)

        if show_stats:
            stats = [
                f"Particles: {particles.n}",
                f"FPS: {int(self.clock.get_fps())}",
                f"Species: {len(SPECIES)}",
            ]
            y_off = 5
            for line in stats:
                surf = self.font.render(line, True, (200, 200, 200))
                self.screen.blit(surf, (5, y_off))
                y_off += 16

        pygame.display.flip()

    def tick(self):
        self.clock.tick(self.fps)

    def running(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_r:
                    return "randomize"
        return True

    def quit(self):
        pygame.quit()
