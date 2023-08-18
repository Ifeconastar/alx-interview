#!/usr/bin/python3

import importlib

minOperations = importlib.import_module("0-minoperations").minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
