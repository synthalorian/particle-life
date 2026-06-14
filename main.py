from particles import ParticleArray
from physics import step_physics
from matrix import AttractionMatrix
from renderer import PygameRenderer

def main():
    # Config
    N = 400
    WIDTH, HEIGHT = 1200, 800
    SPECIES_COUNT = 5

    particles = ParticleArray(N, bounds=(WIDTH, HEIGHT))
    matrix = AttractionMatrix(SPECIES_COUNT, seed=42)
    renderer = PygameRenderer(WIDTH, HEIGHT, fps=60)

    print("PARTICLE LIFE v1")
    print("R = randomize attraction matrix | ESC = quit")

    running = True
    while running:
        result = renderer.running()
        if result is False:
            running = False
            break
        if result == "randomize":
            matrix.randomize()
            print("Attraction matrix randomized.")

        step_physics(particles, matrix, dt=0.15, friction=0.88)
        renderer.draw(particles)
        renderer.tick()

    renderer.quit()

if __name__ == "__main__":
    main()
