
"""Common Functions"""


def isModernChoseong(L):
    """  A Modern Hangul Syllable-Initial Letter?"""
    if ord(L) >= ord('\u1100') and ord(L) < ord('\u1112'):
        return True
    else:
        return False


def isChoseongJamo(L):
    """Hangul Syllable-Initial Letter?"""
    if (ord(L) >= ord('\u1100') and ord(L) <= ord('\u115F')) or \
            (ord(L) >= ord('\uA960') and ord(L) <= ord('\uA97C')):
        return True
    else:
        return False


def isModernJungseong(V):
    """A Modern Hangul Syllable-Peak Letter?"""
    if ord(V) > ord('\u1160') and ord(V) <= ord('\u1175'):
        return True
    else:
        return False


def isJungseongJamo(V):
    """A Hangul Syllable-Peak Letter?"""
    if (ord('\u1160') <= ord(V) and ord(V) <= ord('\u11A7')) or \
            (ord('\uD7B0') <= ord(V) and ord(V) <= ord('\uD7C6')):
        return True
    else:
        return False


def isModernJongseong(T):
    """A Modern Hangul Syllable-Final Letter?"""
    if ord('\u11A8') <= ord(T) and ord(T) <= ord('\u11C2'):
        return True
    else:
        return False


def isOldJongseong(T):
    """A Old Hangul Syllable-Final Letter?"""
    if (ord('\u11C3') <= ord(T) and ord(T) <= ord('\u11FF')) or \
            (ord('\uD7CB') <= ord(T) and ord(T) <= ord('\uD7FB')):
        return True
    else:
        return False


def isJongseongJamo(T):
    """A Hangul Syllable-Final Letter?"""
    if (ord('\u11A8') <= ord(T) and ord(T) <= ord('\u11FF')) or \
            (ord('\uD7CB') <= ord(T) and T <= ord('\uD7FB')):
        return True
    else:
        return False


def isHangulJamo(C):
    """A Johab Hangul Letter?"""
    if (ord('\u1100') <= ord(C) and ord(C) <= ord('\u11FF')) or \
            (ord('\uA960') <= ord(C) and ord(C) <= ord('\uA97C')) or \
            (ord('\uD7B0') <= ord(C) and ord(C) <= ord('\uD7C6')) or \
            (ord('\uD7CB') <= ord(C) and ord(C) <= ord('\uD7FB')):
        return True
    else:
        return False


def isHalfwidthLetter(C):
    """A Halfwidth Hangul Letter?"""
    if ord('\uFFA0') <= ord(C) and ord(C) <= ord('\uFFDF'):
        return True
    else:
        return False


def isCompatibilityLetter(C):
    """A Hangul Compatibility Letter?"""
    if ord('\u3131') <= ord(C) and ord(C) <= ord('\u318E'):
        return True
    else:
        return False


def isParenthesizedLetter(C):
    """A Parenthesized Hangul Letter or a Syllable Block?"""
    if ord('\u3200') <= ord(C) and ord(C) <= ord('\u321F'):
        return True
    else:
        return False


def isCircledLetter(C):
    """A Circled Hangul Letter or a Syllable Block?"""
    if ord('\u3260') <= ord(C) and ord(C) <= ord('\u327F'):
        return True
    else:
        return False


def isPrecomposedSyllable(S):
    """A Wanseong Hangul Syllable Block?"""
    if ord('\uAC00') <= ord(S) and ord(S) <= ord('\ud7A3'):
        return True
    else:
        return False


def isHangulLetter(S):
    """A Hanggul-related character?"""
    if isPrecomposedSyllable(S):
        return True
    if isHangulJamo(S):
        return True
    if isCompatibilityLetter(S):
        return True
    if isParenthesizedLetter(S):
        return True
    if isCircledLetter(S):
        return True
    if isHalfwidthLetter(S):
        return True
    return False
