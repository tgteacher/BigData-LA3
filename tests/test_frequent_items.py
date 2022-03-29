import sys
import os
sys.path.insert(0, os.path.join('.', 'answers'))
from answer import frequent_itemsets

def test_frequent_items():
    a = frequent_itemsets(os.path.join('.', 'data', 'plants.data'), 15, 0.1, 0.3)
    assert(a==open(os.path.join('.', 'tests', 'frequent_items.txt'),"r").read())
