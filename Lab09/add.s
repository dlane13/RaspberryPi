.global _start
_start:
	MOV x1, #5
	MOV x2, #6
	MOV x3, #7
	MOV x8, #93
	ADDS x4, x1, x2
	ADDS x0, x3, x4
	SVC #0
