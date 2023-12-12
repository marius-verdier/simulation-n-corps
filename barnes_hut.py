from copy import deepcopy
from utils import distance
import numpy as np

class Node:
    """
    A Node represents a body in space.
    """
    def __init__(self, x, y, px, py, m):
        self.m = m
        self.pos = np.array([x, y])
        self.momentum = np.array([px, py])
        self.child = None
        # Additional attributes for quad-tree
        self.s = 1.0
        self.relpos = self.pos.copy()

    def next_quad(self):
        self.s = 0.5 * self.s
        return self.divide_quad(1) + 2 * self.divide_quad(0)

    def divide_quad(self, i):
        self.relpos[i] *= 2.0
        if self.relpos[i] < 1.0:
            quadrant = 0
        else:
            quadrant = 1
            self.relpos[i] -= 1.0
        return quadrant

    def reset_quad(self):
        self.s = 1.0
        self.relpos = self.pos.copy()

    def dist(self, other):
        return distance(self.pos, other.pos)

    def force_ap(self, other):
        d = self.dist(other)
        return (self.pos - other.pos) * (self.m * other.m / (d**3 + 1))

class BarnesHutSimulation:
    """
    Encapsulates the simulation of bodies in space using the Barnes-Hut algorithm.
    """
    def __init__(self, theta, g, dt, n_bodies):
        self.theta = theta
        self.g = g
        self.dt = dt
        self.n_bodies = n_bodies
        self.bodies = self.initialize_bodies()

    def initialize_bodies(self):
        np.random.seed(123)
        masses = np.random.random(self.n_bodies) * 10
        x0 = np.random.random(self.n_bodies)
        y0 = np.random.random(self.n_bodies)
        px0 = np.random.random(self.n_bodies) - 0.5
        py0 = np.random.random(self.n_bodies) - 0.5
        return [Node(x, y, px, py, m) for x, y, px, py, m in zip(x0, y0, px0, py0, masses)]

    def add_body(self, body, node):
        new_node = body if node is None else None
        min_quad_size = 1.e-5
        if node is not None and node.s > min_quad_size:
            if node.child is None:
                new_node = deepcopy(node)
                new_node.child = [None for _ in range(4)]
                quad = node.next_quad()
                new_node.child[quad] = node
            else:
                new_node = node

            new_node.m += body.m
            new_node.pos += body.pos
            quad = body.next_quad()
            new_node.child[quad] = self.add_body(body, new_node.child[quad])
        return new_node

    def force_on(self, body, node):
        if node.child is None:
            return node.force_ap(body)

        if node.s < node.dist(body) * self.theta:
            return node.force_ap(body)

        return sum(self.force_on(body, c) for c in node.child if c is not None)

    def apply(self):
        for body in self.bodies:
            force = self.g * self.force_on(body, self.root)
            body.momentum += self.dt * force
            body.pos += self.dt * body.momentum / body.m

    def step(self):
        self.root = None
        for body in self.bodies:
            body.reset_quad()
            self.root = self.add_body(body, self.root)
        self.apply()

    def run_simulation(self, n_steps):
        for _ in range(n_steps):
            self.step()

# Usage example
Theta = 0.7
G = 1.e-6
dt = 1.e-2
N_bodies = 100
N_steps = 1000

simulation = BarnesHutSimulation(Theta, G, dt, N_bodies)
simulation.run_simulation(N_steps)
