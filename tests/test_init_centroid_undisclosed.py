import sys
sys.path.insert(0, './answers')
from answer import init_centroids

def test_init_centroids():
    res = ["nb", "in", "ab", "hi"]
    a = init_centroids(4, 1234)
    assert(a == res)
