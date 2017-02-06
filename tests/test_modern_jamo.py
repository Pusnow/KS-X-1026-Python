"""
Tests for modern jamo
"""

from ksx1026 import uchar, normalization
import unittest
import unicodedata


class JamoTest(unittest.TestCase):

    def setUp(self):
        self.lchar = list(chr(x)
                          for x in range(int("1100", 16), int("1112", 16) + 1))
        self.vchar = list(chr(x)
                          for x in range(int("1161", 16), int("1175", 16) + 1))
        self.tchar = list(chr(x)
                          for x in range(int("11A8", 16), int("11C2", 16) + 1))

        self.cpcchar = list(chr(x) for x in range(
            int("3131", 16), int("314E", 16) + 1))
        self.cpvchar = list(chr(x) for x in range(
            int("314F", 16), int("3163", 16) + 1))

    def test_choseong(self):
        for l in self.lchar:
            self.assertTrue(uchar.isModernChoseong(l), msg=l)
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

    def test_jungseong(self):
        for v in self.vchar:
            self.assertFalse(uchar.isModernChoseong(v), msg=v)
            self.assertFalse(uchar.isChoseongJamo(v), msg=v)
            self.assertTrue(uchar.isModernJungseong(v), msg=v)
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

    def test_jongseong(self):
        for t in self.tchar:
            self.assertFalse(uchar.isModernChoseong(t), msg=t)
            self.assertFalse(uchar.isChoseongJamo(t), msg=t)
            self.assertFalse(uchar.isModernJungseong(t), msg=t)
            self.assertFalse(uchar.isJungseongJamo(t), msg=t)
            self.assertTrue(uchar.isModernJongseong(t), msg=t)
            self.assertFalse(uchar.isOldJongseong(t), msg=t)
            self.assertTrue(uchar.isJongseongJamo(t), msg=t)
            self.assertTrue(uchar.isHangulJamo(t), msg=t)
            self.assertFalse(uchar.isHalfwidthLetter(t), msg=t)
            self.assertFalse(uchar.isCompatibilityLetter(t), msg=t)
            self.assertFalse(uchar.isParenthesizedLetter(t), msg=t)
            self.assertFalse(uchar.isCircledLetter(t), msg=t)
            self.assertFalse(uchar.isPrecomposedSyllable(t), msg=t)
            self.assertTrue(uchar.isHangulLetter(t), msg=t)

    def test_cpc(self):
        for cpc in self.cpcchar:
            l = unicodedata.normalize("NFKD", cpc)
            self.assertFalse(uchar.isModernChoseong(cpc), msg=cpc)
            self.assertFalse(uchar.isChoseongJamo(cpc), msg=cpc)
            self.assertFalse(uchar.isModernJungseong(cpc), msg=cpc)
            self.assertFalse(uchar.isJungseongJamo(cpc), msg=cpc)
            self.assertFalse(uchar.isModernJongseong(cpc), msg=cpc)
            self.assertFalse(uchar.isOldJongseong(cpc), msg=cpc)
            self.assertFalse(uchar.isJongseongJamo(cpc), msg=cpc)
            self.assertFalse(uchar.isHangulJamo(cpc), msg=cpc)
            self.assertFalse(uchar.isHalfwidthLetter(cpc), msg=cpc)
            self.assertTrue(uchar.isCompatibilityLetter(cpc), msg=cpc)
            self.assertFalse(uchar.isParenthesizedLetter(cpc), msg=cpc)
            self.assertFalse(uchar.isCircledLetter(cpc), msg=cpc)
            self.assertFalse(uchar.isPrecomposedSyllable(cpc), msg=cpc)
            self.assertTrue(uchar.isHangulLetter(cpc), msg=cpc)

            if uchar.isChoseongJamo(l):
                self.assertEqual(normalization.normalizeJamoKDKC(
                    cpc), l + chr(int("1160", 16)))
            else:
                self.assertEqual(normalization.normalizeJamoKDKC(
                    cpc), chr(int("115F", 16)) + chr(int("1160", 16)) + l)

    def test_cpv(self):
        for cpv in self.cpvchar:
            v = unicodedata.normalize("NFKD", cpv)
            self.assertFalse(uchar.isModernChoseong(cpv), msg=cpv)
            self.assertFalse(uchar.isChoseongJamo(cpv), msg=cpv)
            self.assertFalse(uchar.isModernJungseong(cpv), msg=cpv)
            self.assertFalse(uchar.isJungseongJamo(cpv), msg=cpv)
            self.assertFalse(uchar.isModernJongseong(cpv), msg=cpv)
            self.assertFalse(uchar.isOldJongseong(cpv), msg=cpv)
            self.assertFalse(uchar.isJongseongJamo(cpv), msg=cpv)
            self.assertFalse(uchar.isHangulJamo(cpv), msg=cpv)
            self.assertFalse(uchar.isHalfwidthLetter(cpv), msg=cpv)
            self.assertTrue(uchar.isCompatibilityLetter(cpv), msg=cpv)
            self.assertFalse(uchar.isParenthesizedLetter(cpv), msg=cpv)
            self.assertFalse(uchar.isCircledLetter(cpv), msg=cpv)
            self.assertFalse(uchar.isPrecomposedSyllable(cpv), msg=cpv)
            self.assertTrue(uchar.isHangulLetter(cpv), msg=cpv)
            self.assertEqual(normalization.normalizeJamoKDKC(
                cpv), chr(int("115F", 16)) + v)


if __name__ == '__main__':
    unittest.main()
