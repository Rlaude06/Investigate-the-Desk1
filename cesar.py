
def decode(encoded, cle):
    encoded = encoded.upper()
    return "".join(chr(ord(i)-cle+26*((ord(i)-cle<65)-(ord(i)-cle>90))) if i!=' ' else ' ' for i in encoded).lower()

#version réduite de :
"""for i in encoded.upper():
    if i!=' ':
        decoded+=chr(ord(i)-cle+26*((ord(i)-cle<65)-(ord(i)-cle>90)))
    else:
        decoded+=' '
        """