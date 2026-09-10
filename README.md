# PARTICLE LIFE

> Emergent artificial life from simple rules.

## What Is This?

A real-time artificial life simulator where thousands of particles of different species interact through attraction and repulsion forces. No top-down behavior is programmed—flocking, predation, symbiosis, and stable structures emerge purely from the distance-based physics rules.

## Why It's Cool

- **Emergence**: Complex behaviors arise from simple pairwise interactions.
- **Tunable Ecosystems**: Adjust the attraction matrix and watch species form orbits, chase, flee, or cluster.
- **Visual**: A living canvas of color and motion. Each species paints its own trajectory.
- **Fast**: NumPy vectorized math + Numba JIT for smooth simulation at scale.

## Stack

- **Python 3.10+**
- **NumPy** — vectorized particle math
- **Numba** — JIT acceleration for the hot loop
- **pygame** — initial renderer
- **moderngl** — optional GPU-accelerated renderer for higher particle counts

## How to Run

```bash
cd particle-life
pip install -r requirements.txt
python main.py
```

## Screenshot

```
[screenshot_placeholder: emergent_orbits.png]
```

## Dependencies

```
numpy>=1.24
numba>=0.58
pygame>=2.5
moderngl>=5.8  # optional, for v2+ renderer
```

## License

Apache-2.0

---

## ☕ Support the Developer

If this project saved you time, solved a problem, or just made your day a little more neon, you can fuel the next one:

[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://buymeacoffee.com/synthalorian)
