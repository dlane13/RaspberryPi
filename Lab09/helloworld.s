.global _start
_start:
    MOV x8, #64     // syscall number
    MOV x0, #1      // stdout
    MOV x2, #27     // string is 12 characters long
    LDR x1, =string // string located at 'string:'
    SVC #0

_exit:
    MOV x8, #93     // exit syscall
    SVC #0

.data
string:
    .ascii "Hello World, this is Darby\n"
