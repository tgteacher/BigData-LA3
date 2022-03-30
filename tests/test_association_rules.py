import sys
import os
sys.path.insert(0, os.path.join('.', 'answers'))
from answer import association_rules

def test_association_rules():
    a = association_rules(os.path.join('.', 'data', 'plants.data'), 15, 0.1, 0.3)
    assert(a==open(os.path.join('.', 'tests', 'association_rules.txt'),"r").read())

    # assert(a==open("tests/association_rules.txt","r").read())
