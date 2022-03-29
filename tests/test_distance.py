import sys
import os
sys.path.insert(0, os.path.join('.', 'answers'))
from answer import distance2

def test_distance():
    a = distance2(os.path.join('.', 'data', 'plants.data'), "qc", "on")
    assert(a == 1708)
    a = distance2(os.path.join('.', 'data', 'plants.data'), "ca", "az")
    assert(a == 10718)
