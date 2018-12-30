import sys
sys.path.insert(0, './answers')
from answer import first_iter

def test_first_iter():
    res = {'nb': ['dengl', 'fraspm', 'lb', 'me', 'mn', 'nb', 'nf', 'nh', 'ns', 'nu', 'on', 'qc', 'ri', 'vt'], 'in': ['al', 'ar', 'ct', 'dc', 'de', 'fl', 'ga', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'mi', 'mo', 'ms', 'nc', 'ne', 'nj', 'ny', 'oh', 'ok', 'pa', 'sc', 'tn', 'tx', 'va', 'wi', 'wv'], 'ab': ['ab', 'ak', 'az', 'bc', 'ca', 'co', 'id', 'mb', 'mt', 'nd', 'nm', 'nt', 'nv', 'or', 'sd', 'sk', 'ut', 'wa', 'wy', 'yt'], 'hi': ['hi', 'pr', 'vi']}
    a = first_iter("./data/plants.data", 4, 1234)
    assert(a == res)
