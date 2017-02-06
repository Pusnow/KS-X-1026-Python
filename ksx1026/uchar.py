"""
Unicode character determine functions for KS X 1026-1
"""


def isModernChoseong(L):
    """
    Check L is a Modern Hangul Syllable-Initial letter.

    :param char L: Single character string
    """
    if ord(L) >= 0x1100 and ord(L) <= 0x1112:
        return True
    else:
        return False


def isChoseongJamo(L):
    """
    Check L is a Hangul Syllable-Initial letter.

    :param char L: Single character string
    """
    if (ord(L) >= 0x1100 and ord(L) <= 0x115F) or \
            (ord(L) >= 0xA960 and ord(L) <= 0xA97C):
        return True
    else:
        return False


def isModernJungseong(V):
    """
    Check V is a Modern Hangul Syllable-Peak letter.

    :param char V: Single character string
    """
    if ord(V) > 0x1160 and ord(V) <= 0x1175:
        return True
    else:
        return False


def isJungseongJamo(V):
    """
    Check V is a Hangul Syllable-Peak letter.

    :param char V: Single character string
    """
    if (0x1160 <= ord(V) and ord(V) <= 0x11A7) or \
            (0xD7B0 <= ord(V) and ord(V) <= 0xD7C6):
        return True
    else:
        return False


def isModernJongseong(T):
    """
    Check T is a Modern Hangul Syllable-Final letter.

    :param char T: Single character string
    """
    if 0x11A8 <= ord(T) and ord(T) <= 0x11C2:
        return True
    else:
        return False


def isOldJongseong(T):
    """
    Check T is an Old Hangul Syllable-Final letter.

    :param char T: Single character string
    """
    if (0x11C3 <= ord(T) and ord(T) <= 0x11FF) or \
            (0xD7CB <= ord(T) and ord(T) <= 0xD7FB):
        return True
    else:
        return False


def isJongseongJamo(T):
    """
    Check T is a Hangul Syllable-Final letter.

    :param char T: Single character string
    """
    if (0x11A8 <= ord(T) and ord(T) <= 0x11FF) or \
            (0xD7CB <= ord(T) and T <= 0xD7FB):
        return True
    else:
        return False


def isHangulJamo(C):
    """
    Check C is a Johab Hangul letter.

    :param char C: Single character string
    """
    if (0x1100 <= ord(C) and ord(C) <= 0x11FF) or \
            (0xA960 <= ord(C) and ord(C) <= 0xA97C) or \
            (0xD7B0 <= ord(C) and ord(C) <= 0xD7C6) or \
            (0xD7CB <= ord(C) and ord(C) <= 0xD7FB):
        return True
    else:
        return False


def isHalfwidthLetter(C):
    """
    Check C is a Halfwidth Hangul letter.

    :param char C: Single character string
    """
    if 0xFFA0 <= ord(C) and ord(C) <= 0xFFDF:
        return True
    else:
        return False


def isCompatibilityLetter(C):
    """
    Check C is a Hangul Compatibility letter.

    :param char C: Single character string
    """
    if 0x3131 <= ord(C) and ord(C) <= 0x318E:
        return True
    else:
        return False


def isParenthesizedLetter(C):
    """
    Check C is a Parenthesized Hangul letter or a Syllable block.

    :param char C: Single character string
    """
    if 0x3200 <= ord(C) and ord(C) <= 0x321F:
        return True
    else:
        return False


def isCircledLetter(C):
    """
    Check C is a Circled Hangul letter or a Syllable block.

    :param char C: Single character string
    """
    if 0x3260 <= ord(C) and ord(C) <= 0x327F:
        return True
    else:
        return False


def isPrecomposedSyllable(S):
    """
    Check S is a Wanseong Hangul Syllable block.

    :param char S: Single character string
    """
    if 0xAC00 <= ord(S) and ord(S) <= 0xd7A3:
        return True
    else:
        return False


def isHangulLetter(S):
    """
    Check S is a Hanggul-related character.

    :param char S Single character string
    """
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
