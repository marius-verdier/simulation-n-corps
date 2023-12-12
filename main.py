import time
from brute_force import BruteForceSimulation
from barnes_hut import BarnesHutSimulation

def run_simulations():
    # Common parameters
    G = 1.e-6
    theta = 0.7
    time_step = 1.e-2
    N_bodies = 100
    N_steps = 100

    # Brute Force Simulation
    print("Starting Brute Force Simulation...")
    start_time = time.time()
    bf_simulation = BruteForceSimulation(G, theta, time_step, N_bodies, N_steps)
    bf_positions, bf_momentums = bf_simulation.simulate()
    bf_duration = time.time() - start_time
    print(f"Brute Force Simulation completed in {bf_duration:.2f} seconds")

    # Barnes-Hut Simulation
    print("Starting Barnes-Hut Simulation...")
    start_time = time.time()
    bh_simulation = BarnesHutSimulation(theta, G, time_step, N_bodies)
    bh_simulation.run_simulation(N_steps)
    bh_duration = time.time() - start_time
    print(f"Barnes-Hut Simulation completed in {bh_duration:.2f} seconds")

    # Performance Comparison
    print("\nPerformance Comparison:")
    print(f"Brute Force: {bf_duration:.2f} seconds")
    print(f"Barnes-Hut: {bh_duration:.2f} seconds")

if __name__ == "__main__":
    run_simulations()
