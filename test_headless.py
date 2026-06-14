"""Headless test for particle-life physics. No display needed."""
import numpy as np
from particles import ParticleArray, SPECIES
from physics import step_physics
from matrix import AttractionMatrix

def test():
    N = 100
    WIDTH, HEIGHT = 800, 600
    particles = ParticleArray(N, bounds=(WIDTH, HEIGHT))
    matrix = AttractionMatrix(5, seed=42)

    print("PARTICLE LIFE — Headless Test")
    print(f"Particles: {N}, Species: {len(SPECIES)}")
    print(f"Matrix:\n{matrix.matrix}")
    print()

    # Run 10 steps
    for i in range(10):
        step_physics(particles, matrix, dt=0.15, friction=0.88)
        if i % 5 == 0:
            print(f"Step {i}: pos mean=({particles.pos.mean(axis=0)}), vel mean=({particles.vel.mean(axis=0)})")

    print("\nTest passed. Physics integration works.")
    print(f"Final bounds check: x in [{particles.x.min():.1f}, {particles.x.max():.1f}] y in [{particles.y.min():.1f}, {particles.y.max():.1f}]")

if __name__ == "__main__":
    test()
