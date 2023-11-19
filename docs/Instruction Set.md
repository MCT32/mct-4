# Instruction Set

| **+** | **0** | **1** | **2** | **3** |
| :--: | :--: | :--: | :--: | :--: |
| **0** | NOP | LDI | LDA | STA
| **4** | - | ADD | SUB | OUT
| **8** | JMP | JZ | JC | -
| **12** | - | - | - | HLT

## NOP: No operation
Do nothing.

## LDI: Load immidate into A register
Load value from operand into A register. Can only load 4 bit (0-15) numbers due to operands size, even though register is 8 bit. If bigger numbers are needed, they must be stored in RAM.

## LDA: Load value from RAM into A register
Loads the value in RAM pointed to by the operand into the A register.

## STA: Store value from A register into RAM
Stores the value in the A register into RAM to the address pointed to by the operand.

## ADD: Add value in RAM into A register
Loads the value in RAM pointed to by the operand into the B register, then adds that value into the A register. This (and SUB) is the only use for the B register.

## SUB: Subtract value in RAM from A register
Loads the value in RAM pointed to by the operand into the B register, then subtracts that value into the A register. This (and ADD) is the only use for the B register.

## OUT: Output value in A register into Output register
Copies the value in the A register into the Output register. Useful for outputing values for the user to read.

## JMP: Jump execution to operand
Loads the value in the operand into the program counter, effectively jumping execution to the new address.

## JZ: Jump execution to operand if zero flag is set
Loads the value in the operand into the program counter, effectively jumping execution to the new address, but only if the last ADD or SUB resulted in a zero sum.

## JC: Jump execution to operand if carry flag is set
Loads the value in the operand into the program counter, effectively jumping execution to the new address, but only if the last ADD or SUB resulted in a carry (when adding) or borrow (when subtracting).

## HLT: Halt
Pauses the clock into the user restarts it.
