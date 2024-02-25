"""
https://www.codewars.com/kata/5c9d62cbf1613a001af5b067/train/python

Implement a function which creates a radix tree ( a space-optimized trie [prefix tree] )
in which each node that is the only child is merged with its parent ( unless a word from the input ends there )
from a given list of words
using dictionaries ( aka hash tables, hash maps, maps, or objects )
where:

The dictionary keys are the nodes.
Leaf nodes are empty dictionaries.
The value for empty input is an empty dictionary.
Words are all lowercase or empty strings.
Words can contain duplicates.

radix_tree("romane", "romanus", "romulus", "rubens", "rubicon", "rubicundus")
{"r": {"om": {"an": {"e": {}, "us": {}}, "ulus": {}},
       "ub": {"ens": {}, "ic": {"on": {}, "undus": {}}}}}

"""


def radix_tree(*words):
    if len(''.join(words)) == 0:
        return {}

    for i_main_l, main_l in enumerate(words[0]):
        print(all(map(lambda x: main_l == x[i_main_l], words[1:])))




print(radix_tree("romane", "romanus", "romulus", "rubens", "rubicon", "rubicundus"))
