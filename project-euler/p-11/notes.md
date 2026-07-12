1. Sentinel values (a.k.a. guard values)

Instead of checking "am I near the edge of the grid" with an if, the data itself is padded with -1 past every row's real data, plus three entirely fake rows of -1 at the bottom. So when a diagonal or vertical read steps "off the grid," it doesn't crash or read garbage — it lands on a -1 on purpose, and the code treats that as "invalid, discard." This is the standard trick to look up under sentinel values or guard values in array/grid problems: you pay a little extra memory to eliminate boundary-check branches entirely. It directly answers the diagonal boundary problem you and I discussed — they didn't avoid the bug, they made the bug structurally impossible by construction.
2. Flattening a 2D grid into 1D memory with a stride

There's no grid[row][col] here — there's one pointer (esi) walking through one contiguous block of memory, and "move down a row" means "add 21*4 bytes" (M_WIDTH), while "move right a column" means "add 4 bytes." This is how 2D arrays actually live in memory underneath higher-level languages — read up on row-major order and stride (the number of memory positions you skip to move one step in a given dimension). Once you internalize this, all four directions — horizontal, vertical, and both diagonals — become "pick a stride, then read four values at multiples of it." That's why the four direction functions look almost identical: each just hardcodes a different stride (4, M_WIDTH, M_WIDTH+4, M_WIDTH-4).
3. Sign-flag trick for batch sentinel checking

Rather than comparing each of the four numbers to -1 individually, the code does or ebx, ecx then checks the sign flag (js = jump if sign bit set). This works because -1 in two's complement is all 1-bits, so OR-ing it with anything produces all 1-bits — sign bit guaranteed set — while OR-ing two real grid values (0–99, always non-negative) never sets it. So one OR plus one flag check replaces two separate comparisons. Worth reading about bitwise OR for batch condition-checking and how the sign flag/status flags in a CPU let you test conditions without explicit if instructions. It's a neat instance of letting arithmetic do logic's job.
4. Function pointer table (jump table) for direction dispatch

M_Call is an array of four addresses, and call [M_Call][edi*4] calls whichever function the current count says to call, with no if/else or switch at all. Look up jump tables / function pointer tables — this is the assembly-level ancestor of polymorphism and dispatch tables in higher-level languages.
5. Bitmask instead of modulo

and edi, 11y (binary 11 = 3) is computing edi mod 4 without a division instruction, because masking the low bits works only when the divisor is a power of 2. Worth knowing as a general fact: modulo by a power of two is equivalent to a bitwise AND with (power − 1).
