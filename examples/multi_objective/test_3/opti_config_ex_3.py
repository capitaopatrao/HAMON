##============================ opti_config_ex_3.py ================================

# Config file for the minimization of f1(x) and f2(x) of the ZDT 1 function[1]:
# f1(x) = x_1
# f2(x) = g(x)[1-sqrt(x_1/g(x))]
# g(x) = 1+9(sum^30_{i=2} x_i)/29
# 30 variables all in the range of [0, 1]

# References:
# [1] - Zitzler, E., Deb, K., and Thiele, L., “Comparison of Multiobjective Evolutionary Algorithms:
#       Empirical Results,” Evolutionary Computation, Vol. 8, No. 2, 2000

print('Minimizing both f1(x) and f2(x) of the ZDT 1 function\n')

n_of = 2
n_var = 30
var_range = [[0, 1]]*30
n_lim = 0
any_int_var = False
int_var_indexes = []
project_name = 'ex_3'
var_names = []
of_names = ['f1(x)', 'f2(x)']
lim_var_names = []
lim_range_orig = [('greater', 0.0)]
range_gen = 0
mod_lim_range = []
max_min = ['min', 'min']
analytical_funcs = True
working_directory = '.'
plotting = True
true_pareto = True

def getFunctionsAnalytical():
    def of1(*vars):
        return vars[0]

    def of2(*vars):
        g = 1 + 9 * (sum(vars[1:])) / (len(vars) - 1)
        return g * (1 - (vars[0] / g) ** 0.5)

    return [of1, of2]
