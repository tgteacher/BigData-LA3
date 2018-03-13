# Assignment instructions

## Preliminaries

With this assignment you will get a practical hands-on of frequent
itemsets and clustering algorithms in Spark. Before starting, you may
want to review the following definitions and algorithms:
1. Market-basket model, association rules, confidence, interest.
2. kmeans algorithm

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
associate them based on their plants. For instance, "[A, B] => C" will
mean that "Plants found in states A and B are likely to be found in
state C". We adopt a market-basket model where the baskets are the
plants and the items are the states. 

### Data preparation

#### Task

Write a script that prints the first <n> rows of a DataFrame with the following columns:
1. <id>: the id of the basket in the data file, i.e., the line number - 1 (ids start at 0)
2. <plant>: the name of the plant associated with the basket.
3. <items>: the items (states) in the basket, ordered as in the data file. 

#### Required syntax

`data_frame.py <data_file> <n>`

#### Test

`tests/test_data_frame.py`

### Frequent itemsets

#### Task

Using the FP-Growth algorithm from the ML library (see
[here](http://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html)),
write a script that prints the first <n> frequent itemsets obtained
using min support <s> and min confidence <c> (parameters of the
FP-Growth model), sorted by (1) descending itemset size, and (2)
descending frequency. The FP-Growth model should be applied to the DataFrame computed in the previous task.

#### Required syntax

`frequent_itemsets.py <data_file> <n> <s> <c>`

#### Test

`tests/test_frequent_items.py`

### Association rules

#### Task

Using the same FP-Growth algorithm,
write a script that prints the first <n> association rules obtained
using min support <s> and min confidence <c> (parameters of the
FP-Growth model), sorted by (1) descending antecedent size in association rule, and (2)
descending confidence.

#### Required syntax

`association_rules.py <data_file> <n> <s> <c>`

#### Test

`tests/test_association_rules.py`

### Rule interests

#### Task

Using the same FP-Growth algorithm,
write a script that computes the interest of association rules (interest = |confidence - frequency(consequent)|)  obtained
using min support <s> and min confidence <c> (parameters of the
FP-Growth model), and prints the first <n> rules sorted by (1) descending antecedent size in association rule, and (2) descending interest.

#### Required syntax

`interests.py <data_file> <n> <s> <c>`

#### Test

`tests/test_interests.py`
