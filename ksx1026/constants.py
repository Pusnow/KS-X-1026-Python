"""
====================================
 Constants for KS X 1026-1
====================================
.. moduleauthor:: Wonsup Yoon <pusnow@me.com>


All constants for KS X 1026-1.

Reference
============

 * http://www.unicode.org/L2/L2008/08225-n3422.pdf

 """
SBase = 0xAC00
LBase = 0x1100
VBase = 0x1161
TBase = 0x11A7
LCount = 19
VCount = 21
TCount = 28
TCountAll = 83
NCount = VCount * TCount  # 588
SCount = LCount * NCount  # 11172


# a transformation table from Hangul Compatibility Letters(0x3131 - 0x318E)
# to Johab Hangul Letters(0x1100 – 0x11FF)

CPJAMO = [
    0x1100, 0x1101, 0x11AA, 0x1102, 0x11AC,
    0x11AD, 0x1103, 0x1104, 0x1105, 0x11B0,
    0x11B1, 0x11B2, 0x11B3, 0x11B4, 0x11B5,
    0x111A, 0x1106, 0x1107, 0x1108, 0x1121,
    0x1109, 0x110A, 0x110B, 0x110C, 0x110D,
    0x110E, 0x110F, 0x1110, 0x1111, 0x1112,
    0x1161, 0x1162, 0x1163, 0x1164, 0x1165,
    0x1166, 0x1167, 0x1168, 0x1169, 0x116A,
    0x116B, 0x116C, 0x116D, 0x116E, 0x116F,
    0x1170, 0x1171, 0x1172, 0x1173, 0x1174,
    0x1175, 0x1160, 0x1114, 0x1115, 0x11C7,
    0x11C8, 0x11CC, 0x11CE, 0x11D3, 0x11D7,
    0x11D9, 0x111C, 0x11DD, 0x11DF, 0x111D,
    0x111E, 0x1120, 0x1122, 0x1123, 0x1127,
    0x1129, 0x112B, 0x112C, 0x112D, 0x112E,
    0x112F, 0x1132, 0x1136, 0x1140, 0x1147,
    0x114C, 0x11F1, 0x11F2, 0x1157, 0x1158,
    0x1159, 0x1184, 0x1185, 0x1188, 0x1191,
    0x1192, 0x1194, 0x119E, 0x11A1,
]


# a transformation table from Halfwidth Hangul Letters(0xFFA0 - 0xFFDF)
# to Johab Hangul Letters(0x1100 – 0x11FF)

HWJAMO = [
    0x1160, 0x1100, 0x1101, 0x11AA, 0x1102,
    0x11AC, 0x11AD, 0x1103, 0x1104, 0x1105,
    0x11B0, 0x11B1, 0x11B2, 0x11B3, 0x11B4,
    0x11B5, 0x111A, 0x1106, 0x1107, 0x1108,
    0x1121, 0x1109, 0x110A, 0x110B, 0x110C,
    0x110D, 0x110E, 0x110F, 0x1110, 0x1111,
    0x1112, 0xFFBF, 0xFFC0, 0xFFC1, 0x1161,
    0x1162, 0x1163, 0x1164, 0x1165, 0x1166,
    0xFFC8, 0xFFC9, 0x1167, 0x1168, 0x1169,
    0x116A, 0x116B, 0x116C, 0xFFD0, 0xFFD1,
    0x116D, 0x116E, 0x116F, 0x1170, 0x1171,
    0x1172, 0xFFD8, 0xFFD9, 0x1173, 0x1174,
    0x1175, 0xFFDD, 0xFFDE, 0xFFDF,
]


# a transformation table from Hangul - embedded Letters(0x3200 - 0x320D, 0x3260 - 0x326D)
# to Johab Hangul Letters(0x1100 – 0x11FF)

PCJAMO = [
    0x1100, 0x1102, 0x1103, 0x1105,
    0x1106, 0x1107, 0x1109, 0x110B,
    0x110C, 0x110E, 0x110F, 0x1110,
    0x1111, 0x1112,
]


# a transformation of Parenthesized Hangul Letters and syllable blocks(0x3200 - 0x321C)
# to Johab Hangul Letters(0x1100 – 0x11FF) or Wanseong Hangul syllable
# blocks(0xAC00 - 0xD7A3)

PACHAR = [
    0x1100, 0x1102, 0x1103, 0x1105, 0x1106,
    0x1107, 0x1109, 0x110B, 0x110C, 0x110E,
    0x110F, 0x1110, 0x1111, 0x1112, 0xAC00,
    0xB098, 0xB2E4, 0xB77C, 0xB9C8, 0xBC14,
    0xC0AC, 0xC544, 0xC790, 0xCC28, 0xCE74,
    0xD0C0, 0xD30C, 0xD558, 0xC8FC, 0x321D,
    0x321E, 0x321F,
]


# a transformation of Circled Hangul Letters and Syllable Blocks(0x3260 - 0x327B, 0x327E)
# to Johab Hangul Letters(0x1100 – 0x11FF) or Wanseong Hangul syllable
# blocks(0xAC00 - 0xD7A3)

CLCHAR = [
    0x1100, 0x1102, 0x1103, 0x1105, 0x1106,
    0x1107, 0x1109, 0x110B, 0x110C, 0x110E,
    0x110F, 0x1110, 0x1111, 0x1112, 0xAC00,
    0xB098, 0xB2E4, 0xB77C, 0xB9C8, 0xBC14,
    0xC0AC, 0xC544, 0xC790, 0xCC28, 0xCE74,
    0xD0C0, 0xD30C, 0xD558, 0x327C, 0x327D,
    0xCB60, 0x326F,

]


# The order values for Johab Hangul Letters 0x1100 - 0x11FF
INDEX1100 = [
    1, 2, 12, 24, 26, 36, 70, 86, 93, 109, 118, 138, 161, 165, 171, 176,
    177, 179, 185, 13, 14, 15, 17, 25, 41, 45, 66, 69, 77, 85, 87, 88,
    89, 94, 95, 96, 97, 98, 99, 101, 102, 104, 105, 107, 108, 110, 111, 112,
    113, 114, 115, 116, 122, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134,
    135, 139, 140, 142, 143, 144, 145, 146, 147, 148, 149, 150, 152, 164, 167, 168,
    169, 170, 172, 173, 174, 175, 180, 184, 191, 192, 4, 18, 20, 23, 28, 194,
    0, 1, 5, 6, 10, 11, 15, 16, 20, 21, 22, 23, 33, 34, 43, 46,
    48, 52, 54, 64, 71, 73, 2, 3, 7, 8, 12, 13, 14, 18, 19, 26,
    27, 29, 30, 32, 37, 38, 40, 41, 42, 44, 45, 47, 50, 51, 55, 57,
    58, 59, 60, 62, 63, 69, 70, 72, 74, 75, 80, 83, 85, 87, 88, 90,
    92, 93, 94, 4, 9, 17, 24, 25, 1, 2, 7, 12, 20, 23, 24, 36,
    37, 47, 51, 58, 64, 65, 66, 70, 86, 94, 109, 118, 138, 161, 171, 176,
    177, 179, 185, 5, 8, 13, 15, 18, 19, 22, 25, 28, 39, 41, 42, 44,
    45, 48, 49, 54, 56, 57, 59, 60, 63, 67, 71, 75, 77, 79, 80, 81,
    83, 84, 85, 90, 105, 106, 107, 110, 112, 113, 115, 135, 153, 154, 158, 159,
    152, 156, 157, 180, 184, 186, 187, 188, 189, 192, 3, 6, 9, 10, 11, 14,
]


# The order values for Johab Hangul Syllable-Initial Letters 0xA960 - 0xA97C
INDEXA960 = [
    29, 30, 31, 33, 37, 38, 42, 43, 47, 51, 53, 57, 58, 62, 63, 71,
    74, 79, 100, 103, 106, 121, 141, 151, 166, 178, 183, 190, 193,
]

# The order values for Johab Hangul Syllable-Peak Letters 0xD7B0 - 0xD7C6
INDEXD7B0 = [
    28, 31, 35, 36, 39, 49, 53, 56, 61, 65, 66, 67, 68, 76, 77, 78,
    79, 81, 82, 84, 86, 89, 91,
]

# The order values for Johab Hangul Syllable-Final Letters 0xD7CB - 0xD7FB
INDEXD7CB = [
    16, 21, 26, 27, 30,
    31, 32, 33, 34, 35, 38, 40, 46, 50, 52, 55, 61, 68, 69, 72, 73,
    76, 78, 82, 89, 91, 92, 93, 96, 101, 102, 114, 117, 119, 120, 123, 125,
    126, 128, 130, 136, 137, 155, 160, 162, 163, 165, 181, 182,
]