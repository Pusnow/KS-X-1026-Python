"""
========================================================================
 Hangul normalization functions defined in KS X 1026-1
========================================================================
.. moduleauthor:: Wonsup Yoon <pusnow@me.com>


Reference
============

 * http://www.unicode.org/L2/L2008/08225-n3422.pdf

 """
from __future__ import unicode_literals
from .constants import SBase, LBase, VBase, TBase
from .constants import LCount, VCount, TCount, NCount, SCount
from .constants import CPJAMO, HWJAMO, PCJAMO
from . import uchar
import six


def decomposeHangul(S):
    """
    returns a Johab Modern Hangul Syllable Block for the given Wanseong Modern Hangul Syllable Block

    :param char S: Single character Hangul Syllable. If not, return input.
    """
    SIndex = ord(S) - SBase
    if SIndex < 0 or SIndex >= SCount:
        return S
    result = ""
    L = LBase + SIndex // NCount
    V = VBase + (SIndex % NCount) // TCount
    T = TBase + SIndex % TCount
    result += six.unichr(L)
    result += six.unichr(V)
    if T != TBase:
        result += six.unichr(T)
    return result


def decomposeHangulStr(source):
    """
    returns a Johab Modern Hangul Syllable String for the given Wanseong Modern Hangul Syllable String

    :param string source: Single character Hangul Syllable. If not, return input.
    """
    result = []

    for S in source:
        result.append(decomposeHangul(S))

    return "".join(result)


def composeHangul(source):
    """
    returns a Wanseong Modern Hangul Syllable Block for the given Johab Modern Hangul Syllable
    Block. Even when a portion of an Old Hangul Syllable Block is a Modern Hangul Syllable Block,
    unlike UAX #15, that portion is not transformed to a Wanseong Modern Hangul Syllable Block.

    :param string source: unicode string.
    """
    length = len(source)
    if length == 0:
        return ""

    result = []
    last = source[0]
    result += last

    for i in range(1, length):
        ch = source[i]
        LIndex = ord(last) - LBase
        if 0 <= LIndex and LIndex < LCount:
            VIndex = ord(ch) - VBase
            if 0 <= VIndex and VIndex < VCount:
                last = six.unichr(SBase + (LIndex * VCount + VIndex) * TCount)
                len_result = len(result)
                result[len_result - 1] = last
                continue
        SIndex = ord(last) - SBase
        if 0 <= SIndex and SIndex < SCount and (SIndex % TCount) == 0:
            TIndex = ord(ch) - TBase
            if 0 < TIndex and TIndex < TCount:
                last = six.unichr(ord(last) + TIndex)
                len_result = len(result)
                result[len_result - 1] = last
                continue

            if uchar.isOldJongseong(ch):
                L = LBase + SIndex // NCount
                V = VBase + (SIndex % NCount) // TCount
                len_result = len(result)
                result[len_result - 1] = six.unichr(L)
                result += six.unichr(V)
                result += ch
                continue
        last = ch
        result += ch

    return "".join(result)


def recomposeHangul(source):
    """
    If one uses a UAX #15 algorithm instead of the above composeHangul function for normalization,
    an Old Hangul Syllable Block can be decomposed into a Wanseong Modern Hangul Syllable Block and
    Johab Hangul Letter(s). In such cases, after applying, one can use the following recomposition
    algorithm to restore a character string in Normalization Form NFC or NFKC to an L V T format.

    :param string source: unicode string
    """
    length = len(source)

    if length == 0:
        return ""

    result = []
    last = source[0]
    result += last
    for i in range(1, length):
        ch = source[i]

        # check to see if two consecutive characters are a Wanseong Modern Hangul
        # Syallable Block and a Syllable-Final Letter.
        SIndex = ord(last) - SBase
        if 0 <= SIndex and SIndex < SCount and (SIndex % TCount) == 0:
            if uchar.isOldJongseong(ch):
                L = LBase + SIndex // NCount
                V = VBase + (SIndex % NCount) // TCount
                result[len(result) - 1] = six.unichr(L)
                result += six.unichr(V)
                result += ch
                continue
        last = ch
        result += ch
    return "".join(result)


def normalizeJamoKDKC(source):
    """
    Normalizing Compatibility/Halfwidth Hangul Letters and Hangul-embedded symbols
    (NormalizeJamoKDKC)

    :param string source: unicode string
    """
    PHBase = 0x3200
    PHEnd = 0x320D
    CHBase = 0x3260
    CHEnd = 0x326D

    length = len(source)
    if length == 0:
        return ""

    result = []

    for i in range(0, length):
        ch = source[i]
        pf = 0

        if uchar.isCompatibilityLetter(ch):
            ch = six.unichr(CPJAMO[ord(ch) - 0x3131])
        elif PHBase <= ord(ch) and ord(ch) <= PHEnd:
            result += '\u0028'
            ch = six.unichr(PCJAMO[ord(ch) - PHBase])
            pf = '\u0029'
        elif CHBase <= ord(ch) and ord(ch) <= CHEnd:
            ch = six.unichr(PCJAMO[ord(ch) - CHBase])
        elif uchar.isHalfwidthLetter(ch):
            ch = six.unichr(HWJAMO[ord(ch) - 0xFFA0])
        else:
            result += ch
            continue

        if uchar.isChoseongJamo(ch):
            result += ch
            result += '\u1160'
        elif uchar.isJungseongJamo(ch):
            result += '\u115F'
            result += ch
        elif uchar.isJongseongJamo(ch):
            result += '\u115F'
            result += '\u1160'
            result += ch

        if pf != 0:
            result.append(pf)

    return "".join(result)
