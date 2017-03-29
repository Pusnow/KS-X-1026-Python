# -*- coding: utf-8 -*-
"""
Tests for sorting
"""
from __future__ import unicode_literals
from ksx1026 import normalization, sorting
import unittest
import itertools
import six


class SortingTest(unittest.TestCase):
    def setUp(self):
        self.syllable = list(
            six.unichr(x) for x in range(int("AC00", 16), int("D7A3", 16) + 1))

        lchar = list(
            six.unichr(x) for x in range(int("1100", 16), int("1112", 16) + 1))
        vchar = [""] + list(
            six.unichr(x) for x in range(int("1161", 16), int("1175", 16) + 1))
        tchar = [""] + list(
            six.unichr(x) for x in range(int("11A8", 16), int("11C2", 16) + 1))
        self.lvt = itertools.product(lchar, vchar, tchar)

    def test_lvt(self):
        for l, v, t in self.lvt:
            lvt = "".join((l, v, t))

            s = normalization.composeHangul(lvt)
            self.assertEqual(sorting.sortKey(lvt), sorting.sortKey(s))


if __name__ == '__main__':
    unittest.main()
