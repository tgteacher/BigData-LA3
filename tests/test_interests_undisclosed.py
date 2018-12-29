import sys
sys.path.insert(0, './answers')
from answer import interests

def test_interests():
    a = interests("./data/plants.data", 17, 0.2, 0.4)
    assert(a==open("tests/interests_undisclosed.txt","r").read())
