# Script that executes all the tests.

import os

examples_path, _ = os.path.split(os.path.abspath(__file__))
main_path = os.path.abspath(examples_path + '/../')
m_o = '/multi_objective/'
s_o = '/single_objective/'

i = 1

if i < 3:
    n_o = s_o
else:
    n_o = m_o
path = examples_path + n_o + ('test_%d/' % (i))
os.chdir(path)
command = 'python %s/HAMON.py -ea ea_config_ex_%d.py -c opti_config_ex_%d.py' % (main_path, i, i)
print('Executing command "%s" for test number %d' % (command, i))
os.system(command)
print('removing generated __pycache__ directory...')
os.system('rm -r __pycache__')
