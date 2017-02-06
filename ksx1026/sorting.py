"""
Sort functions for KS X 1026-1
"""
from . import uchar
from . import INDEX1100, INDEXA960, INDEXD7B0, INDEXD7CB
from . import HWJAMO, CPJAMO, PACHAR, CLCHAR
from .normalization import decomposeHangul


def getHangulWeightLVT(L, V, T, _type=0):
    """
    for the Syllable-Initial, Syllable-Peak and Syllable-Final Letters, determine a weight.
    """
    weight = 0
    LW = 0
    VW = 0
    TW = 0

    if uchar.isChoseongJamo(L):
        if uchar.isJungseongJamo(V):
            if T is None or uchar.isJongseongJamo(T):
                if ord(L) < 0x1200:
                    LW = INDEX1100[ord(L) - 0x1100]
                else:
                    LW = INDEXA960[ord(L) - 0xA960]

                if ord(V) < 0x1200:
                    VW = INDEX1100[ord(V) - 0x1100]
                else:
                    VW = INDEXD7B0[ord(V) - 0xD7B0]

                if T is not None:
                    if ord(V) < 0x1200:
                        TW = INDEX1100[ord(T) - 0x1100]
                    else:
                        TW = INDEXD7CB[ord(T) - 0xD7CB]
                if ord(L) == 0x115F and \
                        ord(V) == 0x1160 and \
                        T is not None:
                    weight = (TW << 24) + _type
                else:
                    weight = (LW << 24) + (VW << 16) + (TW << 8) + _type
    return weight


def getHangulWeight(hc):
    """
    determine a weight for a Wanseong Hangul Syllable Block, a Hangul Letter or
    Hangul-embedded Symbol
    """

    _type = 0
    index = ord(hc)
    weight = 0
    L = chr(0x115F)
    V = chr(0x1160)
    T = None

    if uchar.isJongseongJamo(hc):
        _type = 1
        T = hc
    elif uchar.isHalfwidthLetter(hc):
        _type = 2
        index = HWJAMO[index - 0xFFA0]
        if index == ord(hc):
            raise
    elif uchar.isCompatibilityLetter(hc):
        _type = 3
        index = CPJAMO[index - 0x3131]
    elif uchar.isParenthesizedLetter(hc):
        _type = 4
        index = PACHAR[index - 0x3200]
        if index == ord(hc):
            raise
    elif uchar.isCircledLetter(hc):
        _type = 5
        index = CLCHAR[index - 0x3260]
        if index == ord(hc):
            raise

    index = chr(index)
    if uchar.isChoseongJamo(index):
        L = index
    elif uchar.isJungseongJamo(index):
        V = index
    elif uchar.isJongseongJamo(index):
        T = index
    elif uchar.isPrecomposedSyllable(index):
        SIndex = decomposeHangul(index)
        L = SIndex[0]
        V = SIndex[1]
        if len(SIndex) == 3:
            T = SIndex[2]
        else:
            T = None
    else:
        return 0

    weight = getHangulWeightLVT(L, V, T, _type)
    return weight


def sortKey(text, hangul_first=True):
    """
    key function for sorted
    """
    weights = []
    for ch in text:
        if uchar.isHangulLetter(ch):
            weight = getHangulWeight(ch)
            if not hangul_first:
                weight += 1 << 32
        else:
            weight = ord(ch)
            if hangul_first:
                weight += 1 << 32
        weights.append(weight)
    return weights
