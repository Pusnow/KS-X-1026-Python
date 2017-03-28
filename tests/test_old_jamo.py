# -*- coding: utf-8 -*-
"""
Tests for old jamo
"""
from __future__ import unicode_literals
from ksx1026 import uchar, normalization
import unittest
import itertools
import six


class OldJamoTest(unittest.TestCase):
    def setUp(self):

        self.lchar = list(
            six.unichr(x) for x in range(int("1100", 16), int("1112", 16) + 1))
        self.vchar = list(
            six.unichr(x) for x in range(int("1161", 16), int("1175", 16) + 1))
        self.tchar = [""] + list(
            six.unichr(x) for x in range(int("11A8", 16), int("11C2", 16) + 1))

        self.old_lchar = list(
            six.unichr(x)
            for x in range(int("1113", 16), int("115E", 16) + 1)) + list(
                six.unichr(x)
                for x in range(int("A960", 16), int("A97C", 16) + 1))

        self.old_vchar = list(
            six.unichr(x)
            for x in range(int("1176", 16), int("11A7", 16) + 1)) + list(
                six.unichr(x)
                for x in range(int("D7B0", 16), int("D7C6", 16) + 1))
        self.old_tchar = list(
            six.unichr(x)
            for x in range(int("11C3", 16), int("11FF", 16) + 1)) + list(
                six.unichr(x)
                for x in range(int("D7CB", 16), int("D7FB", 16) + 1))

    def test_uchar(self):
        for l in self.old_lchar:
            self.assertFalse(uchar.isModernChoseong(l), msg=l)
            self.assertTrue(uchar.isChoseongJamo(l), msg=l)
            self.assertFalse(uchar.isModernJungseong(l), msg=l)
            self.assertFalse(uchar.isJungseongJamo(l), msg=l)
            self.assertFalse(uchar.isModernJongseong(l), msg=l)
            self.assertFalse(uchar.isOldJongseong(l), msg=l)
            self.assertFalse(uchar.isJongseongJamo(l), msg=l)
            self.assertTrue(uchar.isHangulJamo(l), msg=l)
            self.assertFalse(uchar.isHalfwidthLetter(l), msg=l)
            self.assertFalse(uchar.isCompatibilityLetter(l), msg=l)
            self.assertFalse(uchar.isParenthesizedLetter(l), msg=l)
            self.assertFalse(uchar.isCircledLetter(l), msg=l)
            self.assertFalse(uchar.isPrecomposedSyllable(l), msg=l)
            self.assertTrue(uchar.isHangulLetter(l), msg=l)
        for v in self.old_vchar:
            self.assertFalse(uchar.isModernChoseong(v), msg=v)
            self.assertFalse(uchar.isChoseongJamo(v), msg=v)
            self.assertFalse(uchar.isModernJungseong(v), msg=v)
            self.assertTrue(uchar.isJungseongJamo(v), msg=v)
            self.assertFalse(uchar.isModernJongseong(v), msg=v)
            self.assertFalse(uchar.isOldJongseong(v), msg=v)
            self.assertFalse(uchar.isJongseongJamo(v), msg=v)
            self.assertTrue(uchar.isHangulJamo(v), msg=v)
            self.assertFalse(uchar.isHalfwidthLetter(v), msg=v)
            self.assertFalse(uchar.isCompatibilityLetter(v), msg=v)
            self.assertFalse(uchar.isParenthesizedLetter(v), msg=v)
            self.assertFalse(uchar.isCircledLetter(v), msg=v)
            self.assertFalse(uchar.isPrecomposedSyllable(v), msg=v)
            self.assertTrue(uchar.isHangulLetter(v), msg=v)
        for t in self.old_tchar:
            self.assertFalse(uchar.isModernChoseong(t), msg=t)
            self.assertFalse(uchar.isChoseongJamo(t), msg=t)
            self.assertFalse(uchar.isModernJungseong(t), msg=t)
            self.assertFalse(uchar.isJungseongJamo(t), msg=t)
            self.assertFalse(uchar.isModernJongseong(t), msg=t)
            self.assertTrue(uchar.isOldJongseong(t), msg=t)
            self.assertTrue(uchar.isJongseongJamo(t), msg=t)
            self.assertTrue(uchar.isHangulJamo(t), msg=t)
            self.assertFalse(uchar.isHalfwidthLetter(t), msg=t)
            self.assertFalse(uchar.isCompatibilityLetter(t), msg=t)
            self.assertFalse(uchar.isParenthesizedLetter(t), msg=t)
            self.assertFalse(uchar.isCircledLetter(t), msg=t)
            self.assertFalse(uchar.isPrecomposedSyllable(t), msg=t)
            self.assertTrue(uchar.isHangulLetter(t), msg=t)

    def test_normalization(self):
        for l, v, t in itertools.product(self.old_lchar, self.old_vchar,
                                         self.old_tchar):
            lvt = "".join((l, v, t))

            self.assertEqual(normalization.recomposeHangul(lvt), lvt)
            self.assertEqual(normalization.composeHangul(lvt), lvt)

    def test_with_modern_jamo(self):

        for l, v, t in itertools.product(self.old_lchar, self.vchar,
                                         self.tchar):
            lvt = "".join((l, v, t))

            self.assertEqual(normalization.recomposeHangul(lvt), lvt)
            self.assertEqual(normalization.composeHangul(lvt), lvt)

        for l, v, t in itertools.product(self.lchar, self.old_vchar,
                                         self.tchar):
            lvt = "".join((l, v, t))

            self.assertEqual(normalization.recomposeHangul(lvt), lvt)
            self.assertEqual(normalization.composeHangul(lvt), lvt)

        for l, v, t in itertools.product(self.lchar, self.vchar,
                                         self.old_tchar):
            lvt = "".join((l, v, t))

            self.assertEqual(normalization.recomposeHangul(lvt), lvt)
            self.assertEqual(normalization.composeHangul(lvt), lvt)

    def test_with_modern_syllable(self):
        lv = list(
            normalization.composeHangul(x + y)
            for x, y in itertools.product(self.lchar, self.vchar))

        for lv, t in itertools.product(lv, self.old_tchar):

            self.assertEqual(
                normalization.composeHangul(lv + t),
                normalization.decomposeHangul(lv) + t)
            self.assertEqual(
                normalization.recomposeHangul(lv + t),
                normalization.decomposeHangul(lv) + t)


if __name__ == '__main__':
    unittest.main()
