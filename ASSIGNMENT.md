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

#### Required syntax

`data_frame.py <data_file> <n>`

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

#### Required syntax

`frequent_itemsets.py <data_file> <n> <s> <c>`

#### Test

`tests/test_frequent_items.py`

### Association rules

#### Task

Using the same FP-Growth algorithm,
write a script that prints the first `<n>` association rules obtained
using min support `<s>` and min confidence `<c>` (parameters of the
FP-Growth model), sorted by (1) descending antecedent size in association rule, and (2)
descending confidence.

#### Required syntax

`association_rules.py <data_file> <n> <s> <c>`

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
where `D` is the number of plants in the data file. The `i` coordinate
in a state vector will be 1 if and only if the `ith` plant in the
dataset is present in the state (plants are ordered alphabetically, as
in the dataset). For simplicity, we will initialize the kmeans
algorithm randomly.

### Data preparation

#### Task

Write a script that:
1. creates an RDD in which every element is a dictionary representing a state with the following keys and values:
| Key    | Value |
|--------|:------:|
| `name` | abbreviation of the state|
| `<plant>` | 1 if `<plant>` occurs in the state, 0 otherwise|

2. Prints to file `<output_file>` the value associated with key `<key>` in the dictionary
representing state `<state>`.

You are strongly encouraged to use the RDD created here in the remainder of the assignment. 

#### Required syntax

`data_preparation.py <data_file> <key> <state> <output_file>`

#### Test

`tests/test_data_preparation.py`

### Distance function

#### Task

Write a script that computes the squared Euclidean
distance between two states. 

#### Required syntax

`distance2.py <data_file> <state1> <state2>`

#### Test

`tests/test_distance.py`

### Initialization 

#### Task

Write a script that:
1. randomly picks `<k>` states randomly from the
array in `answers/all_states.py` (you may import or copy this array to
your code) using the random seed passed as argument and Python's
`random.sample` function.
2. prints each selected state abbreviation on a different line.

In the remainder, the centroids of the kmeans algorithm must be
initialized using the method implemented here, perhaps using a line
such as: `centroids = rdd.filter(lambda x: x['name'] in
init_states).collect()`, where `rdd` is the RDD created in the data
preparation task.

#### Required syntax

`init.py <k> <random_seed>`

#### Test

`tests/test_init.py`

### First iteration

#### Task

Write a script that:
1. assigns each state to its 'closest' class where 'closest' means 'the class corresponding to the centroid closest to the state according to the distance defined in the distance function task'. Centroids must be initialized as
in the previous task.
2. prints the classes in alphabetical order: 
states must be ordered alphabetically within classes, and classes
must be sorted according to the alphabetical order of their first
state. Check `tests/first_iteration.txt` for formatting requirements.

#### Required syntax

`first_iter.py <data_file> <k> <random_seed>`

#### Test

`tests/test_first_iter.py`

### Complete kmeans

#### Task

Write a script that:
1. assigns states to classes as in the previous task.
2. updates the centroids based on the assignments in 1.
3. go to step 1 if the assignments have not changed since the previous iteration.
4. prints classes as in the previous task but in an output file.

#### Required syntax

`kmeans.py <data_file> <k> <random_seed> <output_file>`

#### Test

`tests/test_kmeans.py`

### Visualization

Here is a visualization of the clustering obtained in the previous
task, obtained with R's 'maps' package (Canadian provinces, Alaska and
Hawaii couldn't be represented). The classes seem to make sense from a
geographical point of view!

![kmeans result](https://users.encs.concordia.ca/~tglatard/teaching/big-data/winter-2018/images/states.png)
