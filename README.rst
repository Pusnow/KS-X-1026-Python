KS X 1026 Python
================

Python implementation for KS X 1026-1.

KS X 1026-1
-----------

KS X 1026-1 is a Korean standard for Hangul processing guide for
information interchange. More informations are available
`here <http://www.unicode.org/L2/L2008/08225-n3422.pdf>`__.

Installation
------------

KS X 1026 Python is available via PyPi

::

    pip install ksx1026

or setup.py

::

    python setup.py install

Normalizations
--------------

Hangul Decomposition
~~~~~~~~~~~~~~~~~~~~

Returns a Johab Modern Hangul Syllable Block for the given Wanseong
Modern Hangul Syllable Block

char S: Single character Hangul Syllable. If not, return input.

::

    >>> from ksx1026.normalization import decomposeHangul
    >>> c = "\uAC01"
    >>> d = decomposeHangul(c)
    >>> print(d.encode('raw_unicode_escape'))
    b'\\u1100\\u1161\\u11a8'

Hangul Composition
~~~~~~~~~~~~~~~~~~

Returns a Wanseong Modern Hangul Syllable Block for the given Johab
Modern Hangul Syllable Block. Even when a portion of an Old Hangul
Syllable Block is a Modern Hangul Syllable Block,unlike UAX #15, that
portion is not transformed to a Wanseong Modern Hangul Syllable Block.

string source: unicode string.

::

    >>> from ksx1026.normalization import composeHangul
    >>> source = "\u1100\u1161\u11a8"
    >>> d = composeHangul(source)
    >>> print(d.encode('raw_unicode_escape'))
    b'\\uac01'
    >>> source = "\u1100\u1161\u11c3"
    >>> d = composeHangul(source)
    >>> print(d.encode('raw_unicode_escape'))
    b'\\u1100\\u1161\\u11c3'

Hangul Recomposition
~~~~~~~~~~~~~~~~~~~~

If one uses a UAX #15 algorithm instead of the above composeHangul
function for normalization, an Old Hangul Syllable Block can be
decomposed into a Wanseong Modern Hangul Syllable Block and Johab Hangul
Letter(s). In such cases, after applying, one can use the following
recomposition algorithm to restore a character string in Normalization
Form NFC or NFKC to an L V T format.

string source: unicode string

::

    >>> from ksx1026.normalization import recomposeHangul
    >>> source = "\uac00\u11c3"
    >>> d = recomposeHangul(source)
    >>> print(d.encode('raw_unicode_escape'))
    b'\\u1100\\u1161\\u11c3'

Normalization of Compatibility/Halfwidth Hangul Letters and Hangul-embedded symbols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Normalizing Compatibility/Halfwidth Hangul Letters and Hangul-embedded
symbols (NormalizeJamoKDKC)

string source: unicode string

::

    >>> from ksx1026.normalization import normalizeJamoKDKC
    >>> source = "\u3200"
    >>> d = normalizeJamoKDKC(source)
    >>> print(d.encode('raw_unicode_escape'))
    >>> b'(\\u1100\\u1160)
