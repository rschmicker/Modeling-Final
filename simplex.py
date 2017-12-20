#!/usr/bin/env python
import numpy as np
from scipy.optimize import linprog

objective = np.array([-30, -50])
less_than_values = np.array([1000, 4000, 100])
constraints = np.array([[40, 20], [50, 150], [1, 5]])

res = linprog(	c = objective, 
				A_ub = constraints, 
				b_ub = less_than_values,
				bounds=(0, None)
			)

print('Optimal value:\t' +  str(res.fun) + '\nX:\t\t' + str(res.x))
