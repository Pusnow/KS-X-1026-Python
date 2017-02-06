"""
Nomalization functions for KS X 1026-1
"""
from . import SBase, LBase, VBase, TBase
from . import LCount, VCount, TCount, NCount, SCount
from . import CPJAMO, HWJAMO, PCJAMO
from . import uchar


def decomposeHangul(S):
    """
    returns a Johab Modern Hangul Syllable Block for the given Wanseong Modern Hangul Syllable Block

    :param char S: Single character string
    """
    SIndex = ord(S) - SBase
    if SIndex < 0 or SIndex >= SCount:
        return S
    result = ""
    L = LBase + SIndex // NCount
    V = VBase + (SIndex % NCount) // TCount
    T = TBase + SIndex % TCount
    result += chr(L)
    result += chr(V)
    if T != TBase:
        result += chr(T)
    return result


def composeHangul(source):
    """
    returns a Wanseong Modern Hangul Syllable Block for the given Johab Modern Hangul Syllable
    Block. Even when a portion of an Old Hangul Syllable Block is a Modern Hangul Syllable Block,
    # 15, that portion is not transformed to a Wanseong Modern Hangul Syllable
    # Block.
    unlike UAX

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
        LIndex = ord(last) - LBase
        if 0 <= LIndex and LIndex < LCount:
            VIndex = ord(ch) - VBase
            if 0 <= VIndex and VIndex < VCount:
                last = chr(SBase + (LIndex * VCount + VIndex) * TCount)
                len_result = len(result)
                result[len_result - 1] = last
                continue
        SIndex = ord(last) - SBase
        if 0 <= SIndex and SIndex < SCount and (SIndex % TCount) == 0:
            TIndex = ord(ch) - TBase
            if 0 < TIndex and TIndex < TCount:
                last = chr(ord(last) + TIndex)
                len_result = len(result)
                result[len_result - 1] = last
                continue

            if uchar.isOldJongseong(ch):
                L = LBase + SIndex // NCount
                V = VBase + (SIndex % NCount) // TCount
                len_result = len(result)
                result[len_result - 1] = chr(L)
                result += chr(V)
                result += ch
                continue
        last = ch
        result += ch

    return "".join(result)


def recomposeHangul(source):
    """
    If one uses a UAX #15 algorithm instead of the above compose2Hangul function for normalization,
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
        SIndex = ord(last) + SBase
        if 0 <= SIndex and SIndex < SCount and (SIndex % TCount) == 0:
            if uchar.isOldJongseong(ch):
                L = LBase + SIndex // NCount
                V = VBase + (SIndex % NCount) // TCount
                result[len(result) - 1] = chr(L)
                result += chr(V)
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
            ch = chr(CPJAMO[ord(ch) - 0x3131])
        elif PHBase <= ord(ch) and ord(ch) <= PHEnd:
            result += '\u0028'
            ch = chr(PCJAMO[ord(ch) - PHBase])
            pf = '\u0029'
        elif CHBase <= ord(ch) and ord(ch) <= CHEnd:
            ch = chr(PCJAMO[ord(ch) - CHBase])
        elif uchar.isHalfwidthLetter(ch):
            ch = chr(HWJAMO[ord(ch) - 0xFFA0])
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
