# Registers

## A register
8-bit general-purpose read/write register. Used to transfer information to and from RAM, send information to the Out register, and perform arithmatic.

## B register
8-bit write only register used only for arithmatic. Loads value from RAM when ADD or SUB instruction is used.

## Out register
8-bit write only register used to output a value to the user. Can only be written from the A register. Displays its contents in both decimal and hexadecimal notation.

## Memory Address Register (MAR)
4-bit register used to point to an address in RAM. Before a value in RAM is accessed or changed, the address must be written to the MAR.

## Program Counter (PC)
4-bit register used to store the current address of execution. Incremented every instruction. Written to during jump instructions to redirect code flow.

## Instruction Register (IR)
8-bit register used to store the current instruction being executed. The 4 most significant bits (instruction id) is used by the PLA to set required control bits. The least significant bits (operand) are sent to the bus to be used in various ways.