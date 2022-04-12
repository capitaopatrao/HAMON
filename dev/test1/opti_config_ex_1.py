##============================ opti_config_ex_1.py ================================

# Config file for the minimization of the De Jong’s fifth function or Shekel’s foxholes[1]:
# f(x) = (0.002 + sum^25_{i=1} 1/(i + (x_1 - a_1i)^6+(x_2-a_2i)^6))^(-1)
# where a = [-32 -16   0  16  32 -32 ...  0 16 32
#            -32 -32 -32 -32 -32 -16 ... 32 32 32]

# References:
# [1] - Molga, M., & Smutnicki, C. Test functions for optimization needs (2005)
# [2] - https://www.sfu.ca/~ssurjano/dejong5.html

print('Minimizing Bukin function n.6. The minimum value is around 0 at (-10,1)\n')

var_range = [[-15, -5], [-3, 3]]
project_name = 'bukin6'
var_names = ['x1', 'x2']
of_names = ['of_1']
max_min = ['min']
analytical_funcs = True
working_directory = '.'
plotting = True


def getFunctionsAnalytical():
    #Bukin function n.6
    def of(x1, x2):
        y  = (100 * (abs(x2 - 0.01 * x1**2))**0.5) + (0.01 * abs(x1 + 10))
        return y
    return [of]
