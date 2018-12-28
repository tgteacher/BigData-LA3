import sys
sys.path.insert(0, './answers')
from answer import association_rules

def test_association_rules():
    a = association_rules("./data/plants.data", 17, 0.2, 0.4)
    assert(a==open("tests/association_rules_undisclosed.txt","r").read())
