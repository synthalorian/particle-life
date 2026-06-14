# SCOPE: PARTICLE LIFE

## v1 — Core Physics

- [ ] Particle array: positions, velocities, species tags
- [ ] Attraction matrix: per-species pairwise force rules
- [ ] 5 species with distinct colors
- [ ] Distance-based force kernel (linear or inverse-square falloff)
- [ ] pygame renderer: 2D canvas, species-colored dots
- [ ] Basic emergent behavior demo

## v2 — Scale & Tuning

- [ ] Numba JIT acceleration for the force loop
- [ ] Expand to 20+ species
- [ ] Spatial hashing (grid) for neighbor lookups — O(n) → O(1) per particle
- [ ] Parameter tuning UI: live-edit attraction matrix, species count, force params
- [ ] moderngl renderer for 10k+ particles at 60fps

## v3 — Ecosystem Simulation

- [ ] Food/energy system: particles consume energy to move
- [ ] Reproduction: energy threshold → spawn offspring
- [ ] Death: energy depletion → particle removal
- [ ] Carrying capacity and population dynamics
- [ ] Recording: export frames as GIFs for sharing

## Architecture

```
particle-life/
├── main.py              # entry point, render loop
├── particles.py         # Particle array + species definitions
├── physics.py           # Force kernel, spatial hashing
├── renderer.py          # pygame / moderngl backends
├── matrix.py            # Attraction matrix + parameter editor
├── ecosystem.py           # v3: energy, reproduction, death
└── utils.py             # GIF recording, profiling
```

### Key Data Structures

- **Particle Array**: `N x 5` float32 array (x, y, vx, vy, species)
- **Attraction Matrix**: `S x S` float32 matrix (species A → species B force)
- **Spatial Grid**: hash map from grid cell → particle indices for fast neighbor queries

## Milestones

| Day | Target |
|-----|--------|
| 1 | Basic physics: particles move, attract, repel |
| 3 | Emergent behavior: orbits, chasing, clustering |
| 7 | Polish, parameter tuning, record GIFs |

## Deferred / Future

- 3D simulation
- WebGL export (pyodide / wasm)
- Multi-threaded CPU fallback (OpenMP / Cython)
