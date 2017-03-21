"""
Tests for Enclosed CJK Letters and Months
"""
from __future__ import unicode_literals
from ksx1026 import uchar, normalization
import unittest
import unicodedata
import six


class EnclosedTest(unittest.TestCase):
    def setUp(self):
        self.parenthesized = list(
            six.unichr(x) for x in range(int("3200", 16), int("321E", 16) + 1))
        self.circled = list(
            six.unichr(x) for x in range(int("3260", 16), int("327E", 16) + 1))

    def test_parenthesized(self):
        for p in self.parenthesized:
            self.assertFalse(uchar.isModernChoseong(p), msg=p)
            self.assertFalse(uchar.isChoseongJamo(p), msg=p)
            self.assertFalse(uchar.isModernJungseong(p), msg=p)
            self.assertFalse(uchar.isJungseongJamo(p), msg=p)
            self.assertFalse(uchar.isModernJongseong(p), msg=p)
            self.assertFalse(uchar.isOldJongseong(p), msg=p)
            self.assertFalse(uchar.isJongseongJamo(p), msg=p)
            self.assertFalse(uchar.isHangulJamo(p), msg=p)
            self.assertFalse(uchar.isHalfwidthLetter(p), msg=p)
            self.assertFalse(uchar.isCompatibilityLetter(p), msg=p)
            self.assertTrue(uchar.isParenthesizedLetter(p), msg=p)
            self.assertFalse(uchar.isCircledLetter(p), msg=p)
            self.assertFalse(uchar.isPrecomposedSyllable(p), msg=p)
            self.assertTrue(uchar.isHangulLetter(p), msg=p)

            pp1 = unicodedata.normalize("NFKC", p)
            pp2 = normalization.normalizeJamoKDKC(p)
            if len(pp2) > 1 and uchar.isModernChoseong(pp2[1]):
                self.assertEqual(pp1[:2] + "\u1160" + pp1[-1], pp2)

    def test_circled(self):
        for c in self.circled:
            self.assertFalse(uchar.isModernChoseong(c), msg=c)
            self.assertFalse(uchar.isChoseongJamo(c), msg=c)
            self.assertFalse(uchar.isModernJungseong(c), msg=c)
            self.assertFalse(uchar.isJungseongJamo(c), msg=c)
            self.assertFalse(uchar.isModernJongseong(c), msg=c)
            self.assertFalse(uchar.isOldJongseong(c), msg=c)
            self.assertFalse(uchar.isJongseongJamo(c), msg=c)
            self.assertFalse(uchar.isHangulJamo(c), msg=c)
            self.assertFalse(uchar.isHalfwidthLetter(c), msg=c)
            self.assertFalse(uchar.isCompatibilityLetter(c), msg=c)
            self.assertFalse(uchar.isParenthesizedLetter(c), msg=c)
            self.assertTrue(uchar.isCircledLetter(c), msg=c)
            self.assertFalse(uchar.isPrecomposedSyllable(c), msg=c)
            self.assertTrue(uchar.isHangulLetter(c), msg=c)
            cc1 = unicodedata.normalize("NFKC", c)
            cc2 = normalization.normalizeJamoKDKC(c)
            if uchar.isModernChoseong(cc2[0]):
                self.assertEqual(cc1 + "\u1160", cc2)


if __name__ == '__main__':
    unittest.main()
