import sys
sys.path.insert(0, './answers')
from answer import frequent_itemsets

def test_frequent_items():
    a = frequent_itemsets("./data/plants.data", 17, 0.2, 0.4)
    assert(a==open("tests/frequent_items_undisclosed.txt","r").read())
