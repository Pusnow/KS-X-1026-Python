"""
Constants for KS X 1026-1
"""

SBase = ord('\uAC00')
LBase = ord('\u1100')
VBase = ord('\u1161')
TBase = ord('\u11A7')
LCount = 19
VCount = 21
TCount = 28
TCountAll = 83
NCount = VCount * TCount  # 588
SCount = LCount * NCount  # 11172


"""
a transformation table from Hangul Compatibility Letters (0x3131 - 0x318E)
to Johab Hangul Letters (0x1100 – 0x11FF)
"""
CPJAMO = [
    ord('\u1100'), ord('\u1101'), ord('\u11AA'), ord('\u1102'), ord('\u11AC'),
    ord('\u11AD'), ord('\u1103'), ord('\u1104'), ord('\u1105'), ord('\u11B0'),
    ord('\u11B1'), ord('\u11B2'), ord('\u11B3'), ord('\u11B4'), ord('\u11B5'),
    ord('\u111A'), ord('\u1106'), ord('\u1107'), ord('\u1108'), ord('\u1121'),
    ord('\u1109'), ord('\u110A'), ord('\u110B'), ord('\u110C'), ord('\u110D'),
    ord('\u110E'), ord('\u110F'), ord('\u1110'), ord('\u1111'), ord('\u1112'),
    ord('\u1161'), ord('\u1162'), ord('\u1163'), ord('\u1164'), ord('\u1165'),
    ord('\u1166'), ord('\u1167'), ord('\u1168'), ord('\u1169'), ord('\u116A'),
    ord('\u116B'), ord('\u116C'), ord('\u116D'), ord('\u116E'), ord('\u116F'),
    ord('\u1170'), ord('\u1171'), ord('\u1172'), ord('\u1173'), ord('\u1174'),
    ord('\u1175'), ord('\u1160'), ord('\u1114'), ord('\u1115'), ord('\u11C7'),
    ord('\u11C8'), ord('\u11CC'), ord('\u11CE'), ord('\u11D3'), ord('\u11D7'),
    ord('\u11D9'), ord('\u111C'), ord('\u11DD'), ord('\u11DF'), ord('\u111D'),
    ord('\u111E'), ord('\u1120'), ord('\u1122'), ord('\u1123'), ord('\u1127'),
    ord('\u1129'), ord('\u112B'), ord('\u112C'), ord('\u112D'), ord('\u112E'),
    ord('\u112F'), ord('\u1132'), ord('\u1136'), ord('\u1140'), ord('\u1147'),
    ord('\u114C'), ord('\u11F1'), ord('\u11F2'), ord('\u1157'), ord('\u1158'),
    ord('\u1159'), ord('\u1184'), ord('\u1185'), ord('\u1188'), ord('\u1191'),
    ord('\u1192'), ord('\u1194'), ord('\u119E'), ord('\u11A1'),
]

"""
a transformation table from Halfwidth Hangul Letters (0xFFA0 - 0xFFDF)
to Johab Hangul Letters (0x1100 – 0x11FF)
"""
HWJAMO = [
    ord('\u1160'), ord('\u1100'), ord('\u1101'), ord('\u11AA'), ord('\u1102'),
    ord('\u11AC'), ord('\u11AD'), ord('\u1103'), ord('\u1104'), ord('\u1105'),
    ord('\u11B0'), ord('\u11B1'), ord('\u11B2'), ord('\u11B3'), ord('\u11B4'),
    ord('\u11B5'), ord('\u111A'), ord('\u1106'), ord('\u1107'), ord('\u1108'),
    ord('\u1121'), ord('\u1109'), ord('\u110A'), ord('\u110B'), ord('\u110C'),
    ord('\u110D'), ord('\u110E'), ord('\u110F'), ord('\u1110'), ord('\u1111'),
    ord('\u1112'), ord('\uFFBF'), ord('\uFFC0'), ord('\uFFC1'), ord('\u1161'),
    ord('\u1162'), ord('\u1163'), ord('\u1164'), ord('\u1165'), ord('\u1166'),
    ord('\uFFC8'), ord('\uFFC9'), ord('\u1167'), ord('\u1168'), ord('\u1169'),
    ord('\u116A'), ord('\u116B'), ord('\u116C'), ord('\uFFD0'), ord('\uFFD1'),
    ord('\u116D'), ord('\u116E'), ord('\u116F'), ord('\u1170'), ord('\u1171'),
    ord('\u1172'), ord('\uFFD8'), ord('\uFFD9'), ord('\u1173'), ord('\u1174'),
    ord('\u1175'), ord('\uFFDD'), ord('\uFFDE'), ord('\uFFDF'),
]

"""
a transformation table from Hangul-embedded Letters (0x3200 - 0x320D, 0x3260 - 0x326D)
to Johab Hangul Letters (0x1100 – 0x11FF)
"""
PCJAMO = [
    ord('\u1100'), ord('\u1102'), ord('\u1103'), ord('\u1105'),
    ord('\u1106'), ord('\u1107'), ord('\u1109'), ord('\u110B'),
    ord('\u110C'), ord('\u110E'), ord('\u110F'), ord('\u1110'),
    ord('\u1111'), ord('\u1112'),
]

"""
a transformation of Parenthesized Hangul Letters and syllable blocks (0x3200 - 0x321C)
to Johab Hangul Letters (0x1100 – 0x11FF) or Wanseong Hangul syllable blocks (0xAC00 - 0xD7A3)
"""
PACHAR = [
    ord('\u1100'), ord('\u1102'), ord('\u1103'), ord('\u1105'), ord('\u1106'),
    ord('\u1107'), ord('\u1109'), ord('\u110B'), ord('\u110C'), ord('\u110E'),
    ord('\u110F'), ord('\u1110'), ord('\u1111'), ord('\u1112'), ord('\uAC00'),
    ord('\uB098'), ord('\uB2E4'), ord('\uB77C'), ord('\uB9C8'), ord('\uBC14'),
    ord('\uC0AC'), ord('\uC544'), ord('\uC790'), ord('\uCC28'), ord('\uCE74'),
    ord('\uD0C0'), ord('\uD30C'), ord('\uD558'), ord('\uC8FC'), ord('\u321D'),
    ord('\u321E'), ord('\u321F'),
]

"""
a transformation of Circled Hangul Letters and Syllable Blocks (0x3260 - 0x327B, 0x327E)
to Johab Hangul Letters (0x1100 – 0x11FF) or Wanseong Hangul syllable blocks (0xAC00 - 0xD7A3)
"""
CLCHAR = [
    ord('\u1100'), ord('\u1102'), ord('\u1103'), ord('\u1105'), ord('\u1106'),
    ord('\u1107'), ord('\u1109'), ord('\u110B'), ord('\u110C'), ord('\u110E'),
    ord('\u110F'), ord('\u1110'), ord('\u1111'), ord('\u1112'), ord('\uAC00'),
    ord('\uB098'), ord('\uB2E4'), ord('\uB77C'), ord('\uB9C8'), ord('\uBC14'),
    ord('\uC0AC'), ord('\uC544'), ord('\uC790'), ord('\uCC28'), ord('\uCE74'),
    ord('\uD0C0'), ord('\uD30C'), ord('\uD558'), ord('\u327C'), ord('\u327D'),
    ord('\uCB60'), ord('\u326F'),

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
