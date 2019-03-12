""" reprc -> type-string
Conversion from dlis' representation codes to type-strings that can be
interpreted by numpy.dtype. int's and uint's are normalized to 4-byte.

Note: dtype's for reprc with variable lenghts are not yet supported by dlisio
(reprc 19-20, 23-25, 27).
"""
dtype = {
    1      : 'f4',                   #Low precision floating point
    2      : 'f4',                   #IEEE single precision floating point
    3      : '2f4',                  #Validated single precision floating point
    4      : '3f4',                  #Two-way validated single precision floating point
    5      : 'i4',                   #IBM single precision floating point
    6      : 'i4',                   #VAX single precision floating point
    7      : 'f8',                   #IEEE double precision floating point
    8      : '2f8',                  #Validated double precision floating point
    9      : '3f8',                  #Two-way validated double precision floating point
    10     : 'c8',                   #Single precision complex
    11     : 'c16',                  #Double precision complex
    12     : 'i4',                   #Short signed integer
    13     : 'i4',                   #Normal signed integer
    14     : 'i4',                   #Long signed integer
    15     : 'u4',                   #Short unsigned integer
    16     : 'u4',                   #Normal unsigned integer
    17     : 'u4',                   #Long unsigned integer
    18     : 'u4',                   #Variable-length unsigned integer
    19     : 'i1,U',                 #Variable-length identifier
    20     : 'i4,U',                 #Variable-length ASCII character string
    21     : 'M',                    #Date and time
    22     : 'i4',                   #Origin reference
    23     : 'i4,i1,i1,U',           #Object name
    24     : 'i1,U,i4,i1,i1,U',      #Object reference
    25     : 'i1,U,i4,i1,i1,U,i1,U', #Attribute reference
    26     : 'i1',                   #Boolean status
    27     : 'i1,U',                 #Units expression
}
