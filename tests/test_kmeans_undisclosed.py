import sys
sys.path.insert(0, './answers')
from answer import kmean

def compare(r1, r2):
    if len(r1) != len(r2):
        print(str(len(r1)) + " - " + str(len(r2)))
    assert(len(r1) == len(r2))
    for i in range(len(r1)):
        for j in range(len(r2)):
            res_list = r1[i]
            a_list = r2[j]
            if res_list == a_list:
                list_found = True
                break
        if not list_found:
            print(r2[j])
        assert(list_found)
def test_case1():
    res = [["ab", "ak", "dengl", "fraspm", "ia", "lb", "mb", "me", "mi", "mn", "nb", "nd", "ne", "nf", "nh", "ns", "nt", "nu", "on", "qc", "ri", "sd", "sk", "vt", "wi", "yt"], \
    ["al", "ar", "ct", "dc", "de", "fl", "ga", "il", "in", "ks", "ky", "la", "ma", "md", "mo", "ms", "nc", "nj", "ny", "oh", "ok", "pa", "sc", "tn", "tx", "va", "wv"], \
    ["az", "bc", "ca", "co", "id", "mt", "nm", "nv", "or", "ut", "wa", "wy"], \
    ["hi", "pr", "vi"]]
    a = kmean("./data/plants.data", 4, 1234)
    compare(a,res)
def test_case2():
    res = [['ab', 'ak', 'dengl', 'fraspm', 'hi', 'lb', 'mb', 'nb', 'nd', 'ne', 'nf', 'ns', 'nt', 'nu', 'pr', 'sd', 'sk', 'vi', 'yt'], ['az', 'bc', 'ca', 'co', 'id', 'mt', 'nm', 'nv', 'or', 'ut', 'wa', 'wy'], ['ct', 'dc', 'de', 'ia', 'ma', 'md', 'me', 'mi', 'mn', 'nh', 'nj', 'ny', 'oh', 'on', 'pa', 'qc', 'ri', 'vt', 'wi', 'wv'], ['tx'], ['ar', 'il', 'in', 'ky', 'mo', 'tn', 'va'], ['al', 'fl', 'ga', 'ms', 'nc', 'sc'], ['ks', 'la', 'ok']]
    a = kmean("./data/plants.data", 7, 418937)
    compare(a,res)
def test_case3():
    res = [['al', 'ar', 'dc', 'de', 'fl', 'ga', 'il', 'in', 'ks', 'ky', 'la', 'md', 'mo', 'ms', 'nc', 'ok', 'sc', 'tn', 'tx', 'va', 'wv'], ['ab', 'ak', 'bc', 'dengl', 'fraspm', 'hi', 'lb', 'mb', 'nd', 'nf', 'nt', 'nu', 'pr', 'sk', 'vi', 'yt'], ['az', 'ca', 'co', 'id', 'mt', 'ne', 'nm', 'nv', 'or', 'sd', 'ut', 'wa', 'wy'], ['ct', 'ia', 'ma', 'me', 'mi', 'mn', 'nb', 'nh', 'nj', 'ns', 'ny', 'oh', 'on', 'pa', 'qc', 'ri', 'vt', 'wi']]
    a = kmean("./data/plants.data", 4, 820)
    compare(a,res)
def test_case4():
    res = [['bc', 'ca', 'id', 'or', 'wa'], ['dengl', 'fraspm', 'lb', 'mb', 'nf'], ['ak', 'nt', 'nu', 'yt'], ['pr', 'vi'], ['az', 'co', 'nm', 'ut'], ['ab', 'mt', 'nd', 'ne', 'nv', 'sd', 'sk', 'wy'], ['al', 'fl', 'ms'], ['hi'], ['md', 'nj', 'ny', 'pa'], ['me', 'nb', 'nh', 'ns', 'on', 'qc', 'vt'], ['ga', 'nc', 'sc', 'va'], ['ar', 'ky', 'mo', 'ok', 'tn', 'wv'], ['ia', 'il', 'in', 'ks', 'mi', 'mn', 'oh', 'wi'], ['la', 'tx'], ['ct', 'dc', 'de', 'ma', 'ri']]
    a = kmean("./data/plants.data", 15, 9872)
    compare(a,res)
