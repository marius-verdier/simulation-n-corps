import numpy as np

class BruteForceSimulation:
    def __init__(self, G, theta, time_step, N_bodies, N_steps):
        self.G = G
        self.theta = theta
        self.time_step = time_step
        self.N_bodies = N_bodies
        self.N_steps = N_steps
        self.M = np.random.random(N_bodies) * 10
        self.position = np.random.random((2, N_bodies)) - 0.5
        self.momentum = np.random.random((2, N_bodies)) - 0.5
        self.forces = np.zeros((2, N_bodies, N_bodies))

    def compute_forces(self):
        n = self.position.shape[1]
        for i in range(n):
            for j in range(i):
                delta_pos = self.position[:, i] - self.position[:, j]
                inv_distance_cubed = 1.0 / (np.linalg.norm(delta_pos)**3 + 1)
                force = self.G * self.M[i] * self.M[j] * delta_pos * inv_distance_cubed
                self.forces[:, i, j] = force
                self.forces[:, j, i] = -force
    
    def update_momentum(self):
        force_sum = np.sum(self.forces, axis=2)
        self.momentum += self.time_step * force_sum
    
    def update_position(self):
        self.position += self.time_step * self.momentum / self.M

    def step(self):
        self.compute_forces()
        self.update_momentum()
        self.update_position()

    def simulate(self):
        for _ in range(self.N_steps):
            self.step()
        return self.position, self.momentum

# Usage example
G = 1.e-6
theta = 0.7
time_step = 1.e-2
N_bodies = 100
N_steps = 1000

simulation = BruteForceSimulation(G, theta, time_step, N_bodies, N_steps)
positions, momentums = simulation.simulate()