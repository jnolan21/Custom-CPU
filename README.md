Logisim Custom CPU and Python Compiler

🚀 About This Project

This repository showcases the design and implementation of a custom CPU created using Logisim-Evolution. The project focuses on building a sequential datapath with essential CPU components, including instruction memory, register file, ALU, data memory, and a program counter (PC). The CPU is capable of executing a basic instruction set with addition, subtraction, load, and store operations. This project demonstrates hands-on experience in digital logic design, instruction set architecture (ISA), and hardware/software integration.

Key Features:
* 4 General Purpose Registers in the register file.
* Supports addition and subtraction arithmetic operations.
* Load and store operations to read from and write to memory with offset support.
* Custom-designed instruction set architecture (ISA) and machine code encoding.
* A simple assembler to convert assembly code into machine code for execution on the CPU.
* Fully functioning CPU simulation in Logisim-Evolution.


🔧 Technologies & Tools Used

* Hardware Simulation: Logisim-Evolution
* Languages: [C/Java/Python] (for assembler development)
* Tools: Git, Visual Studio Code (or your preferred IDE)


💡 What I Learned

Throughout this project, I gained hands-on experience in:

* Digital Logic Design: Designing and simulating a CPU, including building key components like the ALU, registers, and memory.
* Instruction Set Architecture (ISA): Developing a custom instruction set, mapping assembly instructions to binary machine code, and understanding CPU instruction decoding.
* Assembler Development: Writing an assembler to translate assembly programs into machine-readable machine code for execution.
* Software-Hardware Integration: Understanding how software interacts with hardware through the execution of assembly code and memory operations.


⚡ CPU Features

* 4 General Purpose Registers: The CPU has four general-purpose registers (R0, R1, R2, R3) for performing operations and storing intermediate results.
* Arithmetic Operations: Supports addition and subtraction operations, where two registers are read and the result is written back to a third register.
* Memory Operations:
  * Load instruction: Reads data from memory and stores it in a register.
  * Store instruction: Writes data from a register to memory, both with offset support.
* Instruction Set Architecture (ISA): Custom-designed ISA with a simple binary encoding, enabling basic arithmetic and memory access operations.
* Sequential Execution: The CPU operates in a single-clock cycle, ensuring efficient execution of instructions.
* Assembler Program: A custom-written assembler that converts assembly code into machine-readable hexadecimal instructions for loading into the CPU.
