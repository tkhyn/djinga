import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

from django.core.management import execute_from_command_line


if __name__ == '__main__':

    default_labels = ['tests']

    argv = ['manage.py', 'test'] + sys.argv[1:]
    for a in sys.argv:
        if [x for x in default_labels if a.startswith(x)]:
            break
    else:
        argv += default_labels

    sys.exit(execute_from_command_line(argv))
