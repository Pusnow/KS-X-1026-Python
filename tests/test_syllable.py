# -*- coding: utf-8 -*-
"""
Tests for modern syllable
"""
from __future__ import unicode_literals
from ksx1026 import uchar, normalization
import unittest
import unicodedata
import itertools
import six


class SyllableTest(unittest.TestCase):
    def setUp(self):
        self.syllable = list(
            six.unichr(x) for x in range(int("AC00", 16), int("D7A3", 16) + 1))

        lchar = list(
            six.unichr(x) for x in range(int("1100", 16), int("1112", 16) + 1))
        vchar = list(
            six.unichr(x) for x in range(int("1161", 16), int("1175", 16) + 1))
        tchar = list(
            six.unichr(x) for x in range(int("11A8", 16), int("11C2", 16) + 1))
        self.lvt = itertools.product(lchar, vchar, tchar)

    def test_uchar(self):
        for s in self.syllable:
            self.assertFalse(uchar.isModernChoseong(s), msg=s)
            self.assertFalse(uchar.isChoseongJamo(s), msg=s)
            self.assertFalse(uchar.isModernJungseong(s), msg=s)
            self.assertFalse(uchar.isJungseongJamo(s), msg=s)
            self.assertFalse(uchar.isModernJongseong(s), msg=s)
            self.assertFalse(uchar.isOldJongseong(s), msg=s)
            self.assertFalse(uchar.isJongseongJamo(s), msg=s)
            self.assertFalse(uchar.isHangulJamo(s), msg=s)
            self.assertFalse(uchar.isHalfwidthLetter(s), msg=s)
            self.assertFalse(uchar.isCompatibilityLetter(s), msg=s)
            self.assertFalse(uchar.isParenthesizedLetter(s), msg=s)
            self.assertFalse(uchar.isCircledLetter(s), msg=s)
            self.assertTrue(uchar.isPrecomposedSyllable(s), msg=s)
            self.assertTrue(uchar.isHangulLetter(s), msg=s)

    def test_normalization(self):
        for s in self.syllable:
            lvt = unicodedata.normalize("NFD", s)
            self.assertEqual(normalization.decomposeHangul(s), lvt)
            self.assertEqual(
                normalization.decomposeHangulStr("\uAC01" + s),
                "\u1100\u1161\u11a8" + lvt)
            self.assertEqual(
                normalization.decomposeHangulStr(s + "\uAC01"),
                lvt + "\u1100\u1161\u11a8")
            self.assertEqual(
                normalization.decomposeHangulStr("A" + s),
                "A" + lvt)
            self.assertEqual(
                normalization.decomposeHangulStr(s + "A"),
                lvt + "A")

    def test_lvt(self):
        for l, v, t in self.lvt:
            lvt = "".join((l, v, t))

            s = unicodedata.normalize("NFC", lvt)
            if len(t) == 1:
                t = hex(ord(t))
            self.assertEqual(
                normalization.composeHangul(lvt),
                s,
                msg=hex(ord(l)) + hex(ord(v)) + t)


if __name__ == '__main__':
    unittest.main()
