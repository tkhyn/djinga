import os
from importlib import import_module

from django.utils.unittest import TestSuite


def load_tests(loader, standard_tests, pattern):
    suite = TestSuite()
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    for d in os.listdir(cur_dir):
        if os.path.exists(os.path.join(cur_dir, d, '__init__.py')):
            mod = import_module('.'.join(('tests', d)))
            suite.addTests(loader.loadTestsFromModule(mod))
    return suite


def load_all(loader, mod_name, init_file_path):
    # imports all the test cases in a module and its submodules

    suite = TestSuite()

    cur_dir = os.path.dirname(os.path.abspath(init_file_path))
    for m in os.listdir(cur_dir):
        if m.endswith('.py') and m != '__init__.py':
            m = m[:-3]
        elif not os.path.isdir(os.path.join(cur_dir, m)) or m == '__pycache__':
            continue
        mod = import_module('.'.join((mod_name, m)))
        suite.addTests(loader.loadTestsFromModule(mod))

    return suite
