# N-Body Simulation

This project contains two implementations of an N-body simulation, which models the dynamics of particles in space under gravitational forces. It includes both a Brute Force algorithm and a more efficient Barnes-Hut algorithm.

Some results are presents in the results folder.

## Features

- **Brute Force Simulation**: Directly computes gravitational interactions between every pair of bodies.
- **Barnes-Hut Simulation**: Utilizes a quadtree to approximate distant interactions, significantly improving performance.

## Getting Started

### Prerequisites

- Python 3.x
- NumPy

### Installation

Clone the repository:

```bash
git clone https://github.com/marius-verdier/simulation-n-corps.git
cd simulation-n-corps
```
### Running the simulation

Execute the main script to run both simulations and compare their performances:

```bash
python main.py
```

## Usage

The project is structured as follows
- **brute_force.py** Implementation of the brute force N-body simulation,
- **barnes_hut.py** Implementation of the Barnes-Hut algorithm for N-body simulation,
- **main.py** Script to run both simulations and compare their performance,
- **utils.py** Contains utility functions used in the simulations.

## Contributing

Contributions are welcome. Please fork the repository and create a pull request with your enhancements.