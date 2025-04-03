#Particle swarm code
import random
import numpy as np
from tkinter import messagebox
import pyswarms as ps


def float_input(x):
    while True:
        try:
            return float(input(x))
        except ValueError:
            print("Invalid input. Please enter a valid float value")
            

def valid_it(x):
    while True:
        try:
            max_it=int(input(x))
            return max_it
        except ValueError:
            print('The value must be a integer')
            
            
class sample():
    def __init__(self,bounds):
        self.position=np.array([np.random(low,high)for low,high in bounds])
        self.velocity=np.array([np.random(0, 1) for _ in bounds])
        self.best_position=self.position.copy()
        self.best_fitness=float('inf')
        
def pso(objf,pop_size,d,maxt):
    swarm_best_position=None
    swarm_best_fitness=float('inf')
    particles=[]
    
    position=np.random((low,high)for low,high in bounds)
    particle=sample(bounds)
    particles.append(particle)
    
    fitness=objf(bounds)
    if fitness<swarm_best_fitness:
        swarm_best_fitness=swarm_best_fitness
        swarm_best_position=position
        
        particle.best_position=position
        particle.best_fitness=fitness
        
    for itr in range(maxt):
        for particle in particles:
            w=0.8
            c1=1.2
            c2=1.2
            
            r1=random.random()
            r2=random.random()
            
            particle.velocity=(w*particle.velocity+c1*r1*(particle.best_position - particle.position)+c2*r1+(swarm_best_position - particle.position))
            
            particle.position+=particle.velocity
            
            fitness=objf(particle.position)
            
            if fitness<particle.best_fitness:
                particle.best_fitness=fitness
                particle.best_position=particle.position
                
            if fitness<swarm_best_fitness:
                swarm_best_fitness=fitness
                swarm_best_position=particle.position
                
            return swarm_best_position,swarm_best_fitness
        
pop_size=valid_it('Enter the swarm size')
maxt=valid_it('Enter the max iterations')
d=4
    
def f2(x):
    width, breadth, height, length = x
    return (width + (breadth / height) * length) / 2

objective_function={'f2':f2}

if __name__ == "__main__":
    # Get user input for the bounds of the parameters
    bounds = []
    for i in range(4):
        lower_bound = float(input(f"Enter the lower bound for parameter {i+1} (width, breadth, height, length): "))
        upper_bound = float(input(f"Enter the upper bound for parameter {i+1} (width, breadth, height, length): "))
        bounds.append((lower_bound, upper_bound))
              
    for funname,objf in objective_function.items():
        output='running function = ' + funname +'\n'
        best_position ,best_fitness =pso(objf,pop_size,d,maxt)
        output+='best position' + str(best_position)+'\n'
        output+='best fitness' + str(best_fitness) + '\n'
        output+= '\n'
    
        print(output)
        #messagebox.showinfo('pso result',output)