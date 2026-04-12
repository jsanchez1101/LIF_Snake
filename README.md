# Biologically-Inspired Neural Controller for Snake

A from-scratch implementation of a spiking neural network (SNN) using leaky integrate-and-fire (LIF) neurons, being built to control a snake game agent's decision-making in Python/Pygame.

**Status: In Progress**

## What This Is

Rather than using standard ML libraries, the neural network is implemented at the individual neuron level. Each LIF neuron accumulates input current, fires when it crosses a voltage threshold, and decays over time — mimicking biological neural dynamics.

The goal is to explore what a neuroscience-based learning model could look like compared to conventional approaches.

## Current Progress

- **Snake game environment** — a complete Pygame snake game with grid-based movement, collision detection, food spawning, and score tracking.
- **LIF neuron model** — a single neuron class implementing voltage accumulation, threshold firing, post-fire reset, membrane leak, and a refractory (cooldown) period.
- **Next up** — synaptic connections between neurons to form a network that takes game state as input and outputs movement decisions.

## Project Structure

```
├── snake_game.py      # Pygame snake game environment
├── lif_neuron.py      # Leaky integrate-and-fire neuron model
└── README.md
```

## LIF Neuron Model

The neuron follows a simplified LIF model:

- **Resting voltage:** -65 mV
- **Firing threshold:** -50 mV
- **Post-fire reset:** -70 mV
- **Membrane leak:** voltage decays toward resting potential each timestep
- **Refractory period:** neuron is unresponsive for a brief cooldown after firing

The voltage update rule per timestep:

```
dv = (resting_volt - current_volt + resistance * input_current) / leak_speed
```

When voltage crosses the threshold, the neuron fires (returns `True`), resets to the reset voltage, and enters cooldown.

## Running It

Requires Python 3 and Pygame.

```bash
pip install pygame matplotlib

# Play the snake game
python snake_game.py

# Run the LIF neuron demo (plots voltage over time)
python lif_neuron.py
```
