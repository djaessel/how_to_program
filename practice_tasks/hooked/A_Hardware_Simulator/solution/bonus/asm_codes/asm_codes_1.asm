# Main Program
main: MOV AX, 0x0012
ADD AX, 0x0002
ADD BX, AX
MUL BX, AX
MOV DX, 0xFFFF
PUSHA
JUMP main
# This is only for debugging
# and currently deactivated.
debug: MOV TEST, 0x0012
MOV TEST, 0x0002
MOV TEST, 0xFFFF
JUMP main
