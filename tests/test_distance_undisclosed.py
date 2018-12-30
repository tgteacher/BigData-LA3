import sys
sys.path.insert(0, './answers')
from answer import distance2

def test_distance():
    a = distance2("./data/plants.data", "qc", "ca")
    assert(a == 12284)
    a = distance2("./data/plants.data", "on", "vt")
    assert(a == 2267)
