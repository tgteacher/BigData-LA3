import os

from answers.answer import init_centroids


def test_init_centroids():
    res = ["oh", "ab", "mi"]
    a = init_centroids(3, 124)
    assert a == res
