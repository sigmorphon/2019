#!/usr/bin/env python
"""
Official Evaluation Script for the SIGMORPHON 2019 Shared Task.
Returns accuracy and mean Levenhstein distance.

Author: Arya McCarthy
Last Update: 2019-12-21

Based on a previous version of this file by Ryan Cotterell
"""

import numpy as np


def distance(str1, str2):
    """Simple Levenshtein implementation for evalm."""
    m = np.zeros([len(str2)+1, len(str1)+1])
    for x in range(1, len(str2) + 1):
        m[x][0] = m[x-1][0] + 1
    for y in range(1, len(str1) + 1):
        m[0][y] = m[0][y-1] + 1
    for x in range(1, len(str2) + 1):
        for y in range(1, len(str1) + 1):
            if str1[y-1] == str2[x-1]:
                dg = 0
            else:
                dg = 1
            m[x][y] = min(m[x-1][y] + 1, m[x][y-1] + 1, m[x-1][y-1] + dg)
    return int(m[len(str2)][len(str1)])


def read(fname):
    """ read file name """
    D = {}
    with open(fname, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            lemma, word, tag = line.split("\t")
            if lemma not in D:
                D[lemma] = {}
            D[lemma][tag] = word
    return D


def read_input(fname):
    """ read in the uncovered file to ignore paradigm slots """
    ignore = set()
    with open(fname, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            lemma, word, tag = line.split("\t")
            if word != u"":
                ignore.add((lemma, tag))
    return ignore


def eval_form(gold, guess, ignore=set()):
    """ compute average accuracy and edit distance for task 1 """
    correct, dist, total = 0., 0., 0.
    for lemma, D in gold.items():
        for tag, str1 in D.items():
            if (lemma, tag) in ignore:
                continue
            
            str2 = u"" # empty string if no guess
            if lemma in guess and tag in guess[lemma]:
                str2 = guess[lemma][tag]
            if str1 == str2:
                correct += 1
            dist += distance(str1, str2)
            total += 1
    return (round(correct/total*100, 2), round(dist/total, 2))

              
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-r", "--reference", help="Gold standard", required=True, type=str)
    parser.add_argument("-o", "--output", help="Model output", required=True, type=str)
    args = parser.parse_args() 

    D_gold = read(args.reference)
    D_guess = read(args.output)

    print("acccuracy:\t{0:.2f}\tlevenshtein:\t{1:.2f}".format(*eval_form(D_gold, D_guess)))
