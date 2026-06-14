import numpy as np
from typing import Tuple

class AttractionMatrix:
    """
    S x S matrix where matrix[i, j] is the force species i feels from species j.
    Positive = attraction, negative = repulsion, zero = neutral.
    """

    def __init__(self, num_species: int, seed: int = None):
        self.num_species = num_species
        if seed is not None:
            np.random.seed(seed)
        # Random matrix in range [-1, 1] with some structure
        self.matrix = np.random.uniform(-1.0, 1.0, size=(num_species, num_species)).astype(np.float32)
        # Bias slightly toward attraction for prettier orbits
        self.matrix += 0.15
        # Self-attraction can be tuned separately
        np.fill_diagonal(self.matrix, np.random.uniform(-0.5, 0.5, size=num_species))

    def randomize(self):
        self.matrix = np.random.uniform(-1.0, 1.0, size=(self.num_species, self.num_species)).astype(np.float32)
        np.fill_diagonal(self.matrix, np.random.uniform(-0.5, 0.5, size=self.num_species))

    def set(self, i: int, j: int, value: float):
        self.matrix[i, j] = value

    def get(self, i: int, j: int) -> float:
        return self.matrix[i, j]
