import os
import time
from pyspark.sql import DataFrame
from pyspark.rdd import RDD
from pyspark.sql.functions import desc, size
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.ml.fpm import FPGrowth
import pyspark
import random
import sys
import copy
from pathlib import Path
from statistics import mean

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
sc = spark.sparkContext

list_of_states = [ "ab", "ak", "ar", "az", "ca", "co", "ct", "de", "dc", "fl",
           "ga", "hi", "id", "il", "in", "ia", "ks", "ky", "la", "me", "md",
           "ma", "mi", "mn", "ms", "mo", "mt", "ne", "nv", "nh", "nj", "nm",
           "ny", "nc", "nd", "oh", "ok", "or", "pa", "pr", "ri", "sc", "sd",
           "tn", "tx", "ut", "vt", "va", "vi", "wa", "wv", "wi", "wy", "al",
           "bc", "mb", "nb", "lb", "nf", "nt", "ns", "nu", "on", "qc", "sk",
           "yt", "dengl", "fraspm" ]

def toCSVLineRDD(rdd):
    a = rdd.map(lambda row: ",".join([str(elt) for elt in row]))\
           .reduce(lambda x,y: "\n".join([x,y]))
    return a + "\n"
def toCSVLine(data):
    if isinstance(data, RDD):
        if data.count() > 0:
            return toCSVLineRDD(data)
        else:
            return ""
    elif isinstance(data, DataFrame):
        if data.count() > 0:
            return toCSVLineRDD(data.rdd)
        else:
            return ""
    return None

def data_frame(filename, n):
    '''
    Write a function that prints the first `<n>` rows of a DataFrame with the following columns:
    1. `<id>`: the id of the basket in the data file, i.e., its line number - 1 (ids start at 0).
    2. `<plant>`: the name of the plant associated to basket.
    3. `<items>`: the items (states) in the basket, ordered as in the data file.

    This function should return a CSV string.
    Using the function toCSVLine on the right dataframe should return the correct answer.
    Test file: tests/test_data_frame.py
    '''
    return "\n"

def frequent_itemsets(filename, n, s, c):
    '''
    Using the FP-Growth algorithm from the ML library (see
    [here](http://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html)),
    write a function that prints the first `<n>` frequent itemsets obtained
    using min support `<s>` and min confidence `<c>` (parameters of the
    FP-Growth model), sorted by (1) descending itemset size, and (2)
    descending frequency. The FP-Growth model should be applied to the DataFrame computed in the previous task.
    This function should return a CSV string. As before, using toCSVLine may help you printing your structure.
    Test file: tests/test_frequent_items.py
    '''
    return "\n"

def association_rules(filename, n, s, c):
    '''
    Using the same FP-Growth algorithm,
    write a script that prints the first `<n>` association rules obtained
    using min support `<s>` and min confidence `<c>` (parameters of the
    FP-Growth model), sorted by (1) descending antecedent size in association rule, and (2)
    descending confidence.
    This function should return a CSV string.
    Test file: tests/test_association_rules.py
    '''
    return "\n"

def interests(filename, n, s, c):
    '''
    Using the same FP-Growth algorithm,
    write a script that computes the interest of association rules (interest = |confidence - frequency(consequent)|; note the absolute value)  obtained
    using min support `<s>` and min confidence `<c>` (parameters of the
    FP-Growth model), and prints the first `<n>` rules sorted by (1) descending antecedent size in association rule, and (2) descending interest.
    This function should return a CSV string.
    Test file: tests/test_interests.py
    '''
    return "\n"

def data_preparation(filename, plant, state):
    '''
    Creates an RDD in which every element is a tuple with the state as first element and a dictionary representing a vector of plant as a second element:
    (name of the state, {dictionary})

    The dictionary should contains the plant names as a key.
    The corresponding value should be 1 if the plant occurs in the state of the tuple and 0 otherwise.

    You are strongly encouraged to use the RDD created here in the remainder of the assignment.

    This function should return True if the plant occurs in the state and False otherwise.
    Test file: tests/test_data_preparation.py
    '''
    return False

def distance2(filename, state1, state2):
    '''
    Write a script that computes the squared Euclidean
    distance between two states.
    This function should return an integer.
    Test file: tests/test_distance.py
    '''
    return 42

def init_centroids(k, seed):
    '''
    This function should randomly picks `<k>` states from the array in `answers/all_states.py` (you
    may import or copy this array to your code) using the random seed passed as
    argument and Python's `random.sample` function.

    In the remainder, the centroids of the kmeans algorithm must be
    initialized using the method implemented here, perhaps using a line
    such as: `centroids = rdd.filter(lambda x: x['name'] in
    init_states).collect()`, where `rdd` is the RDD created in the data
    preparation task.

    Note that if your array of states have all the states, but not in the same
    order as the array in `answers/all_states.py` you may fail the test case or
    have issues in the next questions.

    This function should return a list of `k` states.
    Test file: tests/test_init_centroids.py
    '''
    return []

def first_iter(filename, k, seed):
    '''
    Assigns each state that appears to its 'closest' class where 'closest'
    means 'the class corresponding to the centroid closest to the state
    according to the distance defined in the distance function task'. Centroids
    must be initialized as in the previous task.

    This function should return a dictionary with `k` entries:
    - The key is one of the states choosen as a centroid.
    - The value is a list of states that are the closest to the centroid. The list should be alphabetically sorted.

    Test file: tests/test_first_iter.py
    '''
    return {}

def kmean(filename, k, seed):
    '''
    Write a function that:
    1. Initializes `k` centroids.
    2. Assigns states to these centroids as in the previous task.
    3. Updates the centroids based on the assignments in 2.
    4. Goes to step 2 if the assignments have not changed since the previous iteration.
    5. Return the `k` classes.

    Note: You should use the list of states provided in all_states.py to ensure the same initialisation is made.
    This function should return a list of list where each sub-list contains all states (alphabetically sorted) of one class.
    Example: [["qc", "on"], ["az", "ca"]]
    In this example, there is two classes, one containing the states "qc" and "on", another one containing the states "az" and "ca".
    Test file: tests/test_kmeans.py
    '''

    return []
