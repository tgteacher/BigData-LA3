import sys
import os
sys.path.insert(0, os.path.join('.', 'answers'))
from answer import interests

def test_interests():
    a = interests(os.path.join('.', 'data', 'plants.data'), 15, 0.1, 0.3)
    assert(a==open(os.path.join('.', 'tests', 'interests.txt'),"r").read())
