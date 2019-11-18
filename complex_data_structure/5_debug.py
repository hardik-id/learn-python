import os


def get_path(filename):
    """Return file's path or empty string if no path."""
    head, tail = os.path.split(filename)
    return head


filename = __file__
import pdb; pdb.set_trace()
filename_path = get_path(filename)
print(f'path = {filename_path}')


# python -m pdb .\complex_data_structure\debug.py
# type c to continue
# type n to next step
# type q to quit