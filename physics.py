import numpy as np
from particles import ParticleArray
from matrix import AttractionMatrix

def compute_forces(particles: ParticleArray, matrix: AttractionMatrix,
                   min_dist: float = 5.0, max_dist: float = 100.0,
                   friction: float = 0.85) -> np.ndarray:
    """
    Brute-force O(n²) force computation.
    Returns acceleration array (n x 2).
    """
    n = particles.n
    pos = particles.pos
    species = particles.species
    acc = np.zeros((n, 2), dtype=np.float32)

    for i in range(n):
        si = species[i]
        # Vector from particle i to ALL particles
        dx = pos[:, 0] - pos[i, 0]
        dy = pos[:, 1] - pos[i, 1]
        dists = np.sqrt(dx * dx + dy * dy)

        # Avoid self-interaction and division by zero
        dists[i] = 1e6

        # Apply force kernel: linear falloff in [min_dist, max_dist]
        # 0 at min_dist, peak at ~30, 0 at max_dist
        forces = np.zeros(n, dtype=np.float32)
        mask = (dists > min_dist) & (dists < max_dist)
        if np.any(mask):
            # Normalized distance in [0, 1] for the kernel
            nd = (dists[mask] - min_dist) / (max_dist - min_dist)
            # Parabolic kernel: 1 at center, 0 at edges
            kernel = 1.0 - (2.0 * nd - 1.0) ** 2
            # Apply per-pair attraction matrix value
            sj = species[mask]
            forces[mask] = matrix.matrix[si, sj] * kernel * 0.5

        # Normalize direction vectors
        with np.errstate(divide='ignore', invalid='ignore'):
            ux = dx / dists
            uy = dy / dists
        ux[dists < 1e-5] = 0
        uy[dists < 1e-5] = 0

        acc[i, 0] = np.sum(forces * ux)
        acc[i, 1] = np.sum(forces * uy)

    return acc

def step_physics(particles: ParticleArray, matrix: AttractionMatrix,
                 dt: float = 0.1, friction: float = 0.85):
    """One physics step: compute forces, integrate velocities, update positions."""
    acc = compute_forces(particles, matrix, friction=friction)
    particles.vel += acc * dt
    particles.vel *= friction
    particles.integrate(dt)
