import time
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from brute_force import BruteForceSimulation
from barnes_hut import BarnesHutSimulation

def Bodies(t,y):
    f = np.zeros(12)
    f[0] = y[6]
    f[1] = y[7]
    f[2] = y[8]
    f[3] = y[9]
    f[4] = y[10]
    f[5] = y[11]
    
    f[6] = -(y[0]-y[2])/(((y[0]-y[2])**2+(y[1]-y[3])**2)**(3/2)) \
           -(y[0]-y[4])/(((y[0]-y[4])**2+(y[1]-y[5])**2)**(3/2))
           
    f[7] = -(y[1]-y[3])/(((y[0]-y[2])**2+(y[1]-y[3])**2)**(3/2)) \
           -(y[1]-y[5])/(((y[0]-y[4])**2+(y[1]-y[5])**2)**(3/2))
                     
    f[8] = -(y[2]-y[0])/(((y[2]-y[0])**2+(y[3]-y[1])**2)**(3/2)) \
           -(y[2]-y[4])/(((y[2]-y[4])**2+(y[3]-y[5])**2)**(3/2))
           
    f[9] = -(y[3]-y[1])/(((y[2]-y[0])**2+(y[3]-y[1])**2)**(3/2)) \
           -(y[3]-y[5])/(((y[2]-y[4])**2+(y[3]-y[5])**2)**(3/2))
                     
    f[10]= -(y[4]-y[0])/(((y[4]-y[0])**2+(y[5]-y[1])**2)**(3/2)) \
           -(y[4]-y[2])/(((y[4]-y[2])**2+(y[5]-y[3])**2)**(3/2))
          
    f[11]= -(y[5]-y[1])/(((y[4]-y[0])**2+(y[5]-y[1])**2)**(3/2)) \
           -(y[5]-y[3])/(((y[4]-y[2])**2+(y[5]-y[3])**2)**(3/2))    
           
    return(f)

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

    """
    Comparison of the two methods
    """
    run_simulations()

    """
    Highligting chaotic behaviour
    """
    y0 = [
        -0.500004,#x1
        0,#y1
        0.5 ,#x2
        0,#y2
        0,#x3
        0,#y3
        0,#vx1
        1,#vy1
        0,#vx2
        -1,#vy2
        0,#vx3
        0#vy3
    ] 

    N = 10000
    T = 0.001 #N*T=10

    t = np.linspace(0,N*T,N)
    solution = solve_ivp(Bodies,[0,800],y0,t_eval=t,rtol=1e-13)

    # Évolution des positions
    plt.plot(solution.y[0],solution.y[1],'-g') #Corps 1
    plt.plot(solution.y[2],solution.y[3],'-r') #Corps 2
    plt.plot(solution.y[4],solution.y[5],'-b') #Corps 3
    plt.ylabel("Position(y)")
    plt.xlabel("Position(x)")
    plt.show()

    plt.plot(t,solution.y[6])
    plt.ylabel("Position (x)")
    plt.xlabel("Temps")
    plt.show()
