# Assignment instructions

## Preliminaries

With this assignment you will get a practical hands-on of frequent
itemsets and clustering algorithms in Spark. Before starting, you may
want to review the following definitions and algorithms:
1. Market-basket model, association rules, confidence, interest.
2. kmeans clustering algorithm and its Spark implementation.

Important preliminary notes:

* The requested tasks, described below, are all evaluated with a test
  run with [pytest](http://pytest.org). Your assignment will be graded
  directly from the result of those tests, see details
  [here](./README.md). You may want to get familiar with pytest before
  you start.
  
* The tests contain examples of expected outputs that you may want to
  check in case the instruction below are unclear. Every detail in
  your answer counts! In particular, you should pay attention to the
  exact syntax of the expected output: add quotes around your answer
  and the tests won't pass!

* Your answers to the tasks below *must* be located in directory `answers`. 

## Dataset

We will use the dataset at
https://archive.ics.uci.edu/ml/datasets/Plants, extracted from the
[USDA plant dataset](https://plants.usda.gov/java). This dataset lists
the plants found in US and Canadian states.

The dataset is available in `data/plants.data`, in CSV format. Every
line in this file contains a tuple where the first element is the name
of a plant, and the remaining elements are the states in which the
plant is found. State abbreviations are in `data/stateabbr.txt` for
your information. 

## 1. Frequent itemsets

Here we will seek to identify association rules between states to
associate them based on the plants that they contain. For instance,
"[A, B] => C" will mean that "plants found in states A and B are
likely to be found in state C". We adopt a market-basket model where
the baskets are the plants and the items are the states. This example
intentionally uses the market-basket model outside of its traditional
scope to show how frequent itemset mining can be used in a variety of
contexts.

### Data preparation

#### Task

Write a script that prints the first `<n>` rows of a DataFrame with the following columns:
1. `<id>`: the id of the basket in the data file, i.e., its line number - 1 (ids start at 0).
2. `<plant>`: the name of the plant associated to basket.
3. `<items>`: the items (states) in the basket, ordered as in the data file. 

#### Test

`tests/test_data_frame.py`

### Frequent itemsets

#### Task

Using the FP-Growth algorithm from the ML library (see
[here](http://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html)),
write a script that prints the first `<n>` frequent itemsets obtained
using min support `<s>` and min confidence `<c>` (parameters of the
FP-Growth model), sorted by (1) descending itemset size, and (2)
descending frequency. The FP-Growth model should be applied to the DataFrame computed in the previous task.

#### Test

`tests/test_frequent_items.py`

### Association rules

#### Task

Using the same FP-Growth algorithm,
write a script that prints the first `<n>` association rules obtained
using min support `<s>` and min confidence `<c>` (parameters of the
FP-Growth model), sorted by (1) descending antecedent size in association rule, and (2)
descending confidence.

#### Test

`tests/test_association_rules.py`

### Rule interests

#### Task

Using the same FP-Growth algorithm,
write a script that computes the interest of association rules (interest = |confidence - frequency(consequent)|; note the absolute value)  obtained
using min support `<s>` and min confidence `<c>` (parameters of the
FP-Growth model), and prints the first `<n>` rules sorted by (1) descending antecedent size in association rule, and (2) descending interest.

#### Required syntax

`interests.py <data_file> <n> <s> <c>`

#### Test

`tests/test_interests.py`

## 2. Clustering

We will now cluster the states based on the plants that they contain,
using the kmeans algorithm that we will re-implement. States will be
represented by a vector of binary components (0/1) of dimension `D`,
where `D` is the number of plants in the data file. Coordinate `i`
in a state vector will be 1 if and only if the `ith` plant in the
dataset was found in the state (plants are ordered alphabetically, as
in the dataset). For simplicity, we will initialize the kmeans
algorithm randomly.

### Data preparation

#### Task

Creates an RDD in which every element is a tuple with the state as first element and a dictionary representing a vector of plant as a second element:
(name of the state, {dictionary})

The dictionary should contains the plant names as a key.
The corresponding value should be 1 if the plant occurs in the state of the tuple and 0 otherwise.

You are strongly encouraged to use the RDD created here in the remainder of the assignment.

#### Test

`tests/test_data_preparation.py`

### Distance function

#### Task

Write a script that computes the squared Euclidean
distance between two states. 

#### Test

`tests/test_distance.py`

### Initialization 

#### Task

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

#### Test

`tests/test_init_centroids.py`

### First iteration

#### Task

Assigns each state that appears to its 'closest' class where 'closest'
means 'the class corresponding to the centroid closest to the state
according to the distance defined in the distance function task'. Centroids
must be initialized as in the previous task.

This function should return a dictionary with `k` entries:
- The key is one of the states choosen as a centroid.
- The value is a list of states that are the closest to the centroid. The list should be alphabetically sorted.

#### Test

`tests/test_first_iter.py`

### Complete kmeans

#### Task

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

#### Test

`tests/test_kmeans.py`

### Visualization

Here is a visualization of the clustering obtained in the previous
task, obtained with R's 'maps' package (Canadian provinces, Alaska and
Hawaii couldn't be represented and a different seed than used in the tests was used). The classes seem to make sense from a
geographical point of view!

![kmeans result](https://users.encs.concordia.ca/~tglatard/teaching/big-data/winter-2018/images/states.png)
