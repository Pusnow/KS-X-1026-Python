
from ksx1026 import SBase, LBase, VBase, TBase
from ksx1026 import LCount, VCount, TCount, TCountAll, NCount, SCount
from ksx1026 import CPJAMO, HWJAMO, PCJAMO
from ksx1026 import uchar


def decomposeHangul(S):
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
    length = len(source)

    if length == 0:
        return ""

    result = []
    last = source[0]
    result += last
    for i in range(1, length):
        ch = source[i]
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
    PHBase = ord('\u3200')
    PHEnd = ord('\u320D')
    CHBase = ord('\u3260')
    CHEnd = ord('\u326D')

    length = len(source)
    if length == 0:
        return ""

    result = []

    for i in range(0, length):
        ch = source[i]
        pf = 0

        if uchar.isCompatibilityLetter(ch):
            ch = CPJAMO[ch - ord('\u3131')]
        elif PHBase <= ord(ch) and ord(ch) <= PHEnd:
            result += chr(ord('\u0028'))
            ch = chr(PCJAMO[ord(ch) - PHBase])
            pf = chr(ord('\u0029'))
        elif CHBase <= ord(ch) and ord(ch) <= CHEnd:
            ch = PCJAMO[ord(ch) - CHBase]
        elif uchar.isHalfwidthLetter(ch):
            ch = HWJAMO[ord(ch) - ord('\uFFA0')]
        else:
            result += ch
            continue

        if LBase <= ord(ch) and ord(ch) < (LBase + LCount):
            result += ch
            result += chr(ord('\u1160'))
        elif VBase <= ord(ch) and ord(ch) < (VBase + VCount):
            result += chr(ord('\u115F'))
            result += ch
        elif TBase <= ord(ch) and ord(ch) < (TBase + TCount):
            result += chr(ord('\u115F'))
            result += chr(ord('\u1160'))
            result += ch

        if pf != 0:
            result.append(pf)

    return "".join(result)
