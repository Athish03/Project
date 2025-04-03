import numpy as np
import pyswarms as py
# validation 0 and 6
def float_input(x):
    while True:
        try:
            return float(input(x))
        except ValueError:
            print("Invalid input. Please enter a valid float value")
 
#validation 1 , 2 , 4 
def valid_input(x,y):
    while True:
        min_value= float_input(x)
        max_value= float_input(y)
        if (max_value > min_value) and (max_value>0 and min_value>0):
            return min_value , max_value
        else:
            print(f"The minimum value of parameter {min_value} must be lesser than maximum value of the parameter {max_value}.Both the values must be positive. Please try again")
            
#validation 3 , 5           
def valid_seed(x, min_value, max_value):
    while True:
        seed = float_input(x)
        if (0 < seed <= max_value or 0 < seed <= (max_value-min_value)/2):
            return seed
        else:
            print(f"Seed value must be between {min_value} and {max_value} and value must be between 0 and {(max_value-min_value)/2}")
#validation 7
def valid_fos(x,y):
    while True:
        min_fos=float_input(x)
        max_fos=float_input(y)
        if (max_fos> min_fos) and (max_fos>0 and min_fos>0):
            return min_fos , max_fos
        else:
            print(f'The minimum value of fos {min_fos} must be lesser than maximum value of the paramter {max_fos} . Both the Values must be positive. Please try again')
    
min_w , max_w = valid_input("Enter the minimum width: " , "Enter the maximum width: ")

min_h , max_h = valid_input("Enter the minimum height: ", "Enter the maximum height: ")

min_b , max_b = valid_input("Enter the minimum breadth: ", "Enter the maximum breadth: ")

min_l , max_l = valid_input("Enter the minimum lenght: ", "Enter the maximum lenght: ")

min_fos,max_fos = valid_fos("Enter the minimum FOS: ","Enter the maximum FOS: ")

seed_w =valid_seed("Enter the seed value for width: ", min_w, max_w)
seed_h =valid_seed("Enter the seed value for height: ", min_h, max_h)
seed_b =valid_seed("Enter the seed value for breadth: ", min_b, max_b)
seed_l =valid_seed("Enter the seed value for length: ", min_l, max_l)
count=0
for w in np.arange(min_w, max_w, seed_w):
    for h in np.arange(min_h, max_h, seed_h):
        for b in np.arange(min_b, max_b, seed_b):  
            for l in np.arange(min_l, max_l,seed_l):
                formula = (w +(h/b)*l)/2
                count+=1
                if min_fos <= formula <= max_fos:
                    print ('The design is safe')
                    print(f'Value  {round(formula,5)} , width {round(w,3)}, height {round(h,3)}, breadth {round(b,3)}, length {round(l,3)}')
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break
else:
    print('The design is not safe')
    print(formula)

print('The no of iterations is :',count)
