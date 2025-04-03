import numpy as np
from pyswarm import pso
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
  
def get_input():
    print("Enter the minimum and maximum values for width, breadth, height, and length:")

    min_vals = []
    max_vals = []

    variables = ['width', 'breadth', 'height', 'length']

    for var in variables:
        min_val = float_input(f"Minimum {var}: ")
        max_val = float_input(f"Maximum {var}: ")
        if (max_val > min_val) and (max_val>0 and min_val>0):
            min_vals.append(min_val)
            max_vals.append(max_val)
            
        else:
            print(f"The minimum value of parameter {min_val} must be lesser than maximum value of the parameter {max_val}.Both the values must be positive. Please try again")

    return min_vals, max_vals

def float_input(x):
    while True:
        try:
            return float(input(x))
        except ValueError:
            print("Invalid input. Please enter a valid float value")
            
            
def formula(w,b,h,l):
    return (w + (b/ h) * l) / 2

def opt_pso(min_vals,max_vals,swarm_size,max_it,mins):
    bounds=(min_vals,max_vals)
    op={'c1': 0.5, 'c2': 0.3, 'w':0.9}
    optimizer = (ps.single.GlobalBestPSO(n_particles=swarm_size,dimensions=2,options=op,bounds=bounds))
    kwargs={"w": 1.0, "b": 1.0, 'h':1.0,'l':1}
    xopt,fopt=optimizer.optimize(formula,1000,**kwargs)
    return xopt,fopt

def valid_fos(x,y):
    while True:
        min_fos=float_input(x)
        max_fos=float_input(y)
        if (max_fos> min_fos) and (max_fos>0 and min_fos>0):
            return min_fos , max_fos
        else:
            print(f'The minimum value of fos {min_fos} must be lesser than maximum value of the paramter {max_fos} . Both the Values must be positive. Please try again')
    
def valid_it(x):
    while True:
        try:
            max_it=int(input(x))
            return max_it
        except ValueError:
            print('The value must be a integer')

def valid_step(x,max_vals):
    while True:
        step=float_input(x)
        if step<min(max_vals):
            return step
        else:
            print('The  minstep must be less than the Max value.Please Try again.')          
min_vals , max_vals = get_input()    
max_it=valid_it('Enter the max nummber of iterations:')
swarm_size=valid_it('Enter the swarm size:')
mins=valid_step('Enter the minstep:',max_vals)
min_fos,max_fos = valid_fos("Enter the minimum FOS: ","Enter the maximum FOS: ")

xopt , fopt = opt_pso(min_vals , max_vals,swarm_size ,max_it,mins)

print("\nOptimized values:")
print(f"Width: {xopt[0]}")
print(f"Breadth: {xopt[1]}")
print(f"Height: {xopt[2]}")
print(f"Length: {xopt[3]}")
print("\nMinimum objective function value:", fopt)

if min_fos<= fopt<=max_fos:
    print('The Design is Optimized')
else:
    print('The Design is not Optimized')