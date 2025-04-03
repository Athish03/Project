import random
import numpy as np
from tkinter import messagebox


class sample():
    def __init__(self,position):
        self.position=position
        self.velocity=np.zeros_like(position)
        self.best_position=position
        self.best_fitness=float('inf')
        
def pso(objf,pop_size,d,maxt):
    swarm_best_position=None
    swarm_best_fitness=float('inf')
    particles=[]
    
    position=np.random.uniform(size=(pop_size,d))
    particle=sample(position)
    particles.append(particle)
    
    fitness=objf(position)
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
        
pop_size=200
maxt=100
d=4
        
def f2(x):
    width, breadth, height, length = x
    return (width + (breadth / height) * length) / 2

objective_function={'f2':f2}
        
for funname,objf in objective_function.items():
    output='running function = ' + funname +'\n'
    best_position ,best_fitness =pso(objf,pop_size,d,maxt)
    output+='best position' + str(best_position)+'\n'
    output+='best fitness' + str(best_fitness) + '\n'
    output+= '\n'
    
    
    print(output)
    #messagebox.showinfo('pso result',output)"""
            
#Particle swarm code
import random
import numpy as np
from tkinter import messagebox

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
    def __init__(self,position):
        self.position=position
        self.velocity=np.zeros_like(position)
        self.best_position=position
        self.best_fitness=float('inf')
        
def pso(objf,pop_size,d,maxt):
    swarm_best_position=None
    swarm_best_fitness=float('inf')
    particles=[]
    
    position=np.random.uniform(size=(pop_size, d))
    particle=sample(position)
    particles.append(particle)
    
    fitness=objf(position)
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
        
pop_size=float_input('Enter the swarm size')
maxt=valid_it('Enter the max iterations')
d=valid_it('enter the no of parameters used in the function')
        
def f2(x):
    width, breadth, height, length = x
    return (width + (breadth / height) * length) / 2

objective_function={'f2':f2}
        
for funname,objf in objective_function.items():
    output='running function = ' + funname +'\n'
    best_position ,best_fitness =pso(objf,pop_size,d,maxt)
    output+='best position' + str(best_position)+'\n'
    output+='best fitness' + str(best_fitness) + '\n'
    output+= '\n'
    
    messagebox.showinfo('pso result',output)


def calculate_formula(width, height, breadth, length):
    return (width + (height / breadth) * length) / 2

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid float value.")

def get_valid_seed(prompt, min_value, max_value):
    while True:
        seed = get_float_input(prompt)
        if min_value <= seed <= max_value:
            return seed
        else:
            print(f"Seed value must be between {min_value} and {max_value}.")

# Get min and max values for each parameter
min_width = get_float_input("Enter the minimum width: ")
max_width = get_float_input("Enter the maximum width: ")

min_height = get_float_input("Enter the minimum height: ")
max_height = get_float_input("Enter the maximum height: ")

min_breadth = get_float_input("Enter the minimum breadth: ")
max_breadth = get_float_input("Enter the maximum breadth: ")

min_length = get_float_input("Enter the minimum length: ")
max_length = get_float_input("Enter the maximum length: ")

# Get valid seed values for each parameter
seed_width = get_valid_seed("Enter the seed value for width: ", min_width, max_width)
seed_height = get_valid_seed("Enter the seed value for height: ", min_height, max_height)
seed_breadth = get_valid_seed("Enter the seed value for breadth: ", min_breadth, max_breadth)
seed_length = get_valid_seed("Enter the seed value for length: ", min_length, max_length)

# Get min and max FOS values
min_fos = get_float_input("Enter the minimum FOS: ")
max_fos = get_float_input("Enter the maximum FOS: ")

# Initialize the result
result = 0
found_result = False

# Nested loops using the seed values as the step values
for w in range(int(min_width), int(max_width), int(seed_width)):
    for h in range(int(min_height), int(max_height), int(seed_height)):
        for b in range(int(min_breadth), int(max_breadth), int(seed_breadth)):  # Avoid division by zero
            for l in range(int(min_length), int(max_length), int(seed_length)):
                result = calculate_formula(w, h, b, l)
                # Check if result is within the FOS range
                if min_fos <= result <= max_fos:
                    print(f"Result {result} is within the FOS range [{min_fos}, {max_fos}]")
                    found_result = True
                    break  # Break out of the innermost loop
            if found_result:
                break  # Break out of the middle loop
        if found_result:
            break  # Break out of the outer loop
    if found_result:
        break  # Break out of the outermost loop

# Print a message if no result was found within the FOS range
if not found_result:
    print(f"No result found within the FOS range [{min_fos}, {max_fos}]")
    
