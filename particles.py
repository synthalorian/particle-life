import numpy as np
from dataclasses import dataclass
from typing import Tuple

@dataclass
class SpeciesConfig:
    name: str
    color: Tuple[int, int, int]  # RGB
    radius: float = 2.0

SPECIES = [
    SpeciesConfig("Red",   (255, 60, 60)),
    SpeciesConfig("Green", (60, 255, 60)),
    SpeciesConfig("Blue",  (60, 60, 255)),
    SpeciesConfig("Cyan",  (60, 255, 255)),
    SpeciesConfig("Magenta", (255, 60, 255)),
]

class ParticleArray:
    """N x 5 float32 array: [x, y, vx, vy, species]"""

    def __init__(self, n: int, bounds: Tuple[float, float] = (800, 600)):
        self.n = n
        self.bounds = bounds
        self.pos = np.random.rand(n, 2).astype(np.float32) * np.array(bounds, dtype=np.float32)
        self.vel = np.zeros((n, 2), dtype=np.float32)
        self.species = np.random.randint(0, len(SPECIES), size=n, dtype=np.int32)
        self.active = np.ones(n, dtype=bool)

    def wrap(self):
        """Wrap-around world boundaries."""
        self.pos[:, 0] %= self.bounds[0]
        self.pos[:, 1] %= self.bounds[1]

    def integrate(self, dt: float = 0.1):
        """Euler integration."""
        self.pos += self.vel * dt
        self.wrap()

    @property
    def x(self) -> np.ndarray:
        return self.pos[:, 0]

    @property
    def y(self) -> np.ndarray:
        return self.pos[:, 1]

    @property
    def vx(self) -> np.ndarray:
        return self.vel[:, 0]

    @property
    def vy(self) -> np.ndarray:
        return self.vel[:, 1]
