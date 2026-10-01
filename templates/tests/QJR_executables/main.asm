
OUT "Hello, World!!!"

MOV AX, BX
OUT AX
OUT BX

MOV AX, 2
MOV BX, 6

MOV CX, 1
OUT CX
INC CX
OUT CX

STORE 1023, CX
LOAD DX, 1023

OUT AX
OUT BX

OUT "Let's mix them!!!"

XCHG AX, BX
OUT AX
OUT BX

OUT "Mixed :)"
RET

// Adding something
ADD AX, BX
ADD DX, 192
OUT AX
OUT DX

// Substracting something
SUB AX, DX
OUT AX
OUT DX

// Multipying something
MUL DX
MUL CX
OUT DX
OUT CX

// Division

DIV AX
DIV BX

OUT AX
OUT BX

// Something later...

INC CX
INC CX
INC CX

DEC AX
DEC AX

OUT AX
OUT BX
OUT CX
OUT DX

// Halting

HLT
