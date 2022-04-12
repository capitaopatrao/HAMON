# Script that executes all the tests.

from pathlib import Path
import os

main_path = Path.cwd()
hamonPath = main_path.parent / 'HAMON.py'
eaConfigPath = main_path / 'ea_config_ex_1.py'
optiConfigPath = main_path / 'opti_config_ex_1.py'
n_o = '/single_objective/'


command = 'cd %s;python %s -ea %s -c %s' % (main_path,hamonPath, eaConfigPath, optiConfigPath)
os.system(command)
