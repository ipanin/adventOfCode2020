# AoC 2020. Day
import collections
import math
import re
import os
import util
from asm import Asm


def test1(fname, expected):
    # asm = Asm(fname)
    data = util.load_str_lines_list(fname)
    result = 0
    util.assert_equal(result, expected)


# data = util.load_str_lines_list('input.txt')

# print("Part 1.")
# test1('input.txt', 0)

