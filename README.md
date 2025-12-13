##Frank's Equation: Cognitectural Dimenscape

A deterministic geometric-cryptographic framework that generates unique, infinitely complex 3-D structures from a 4-D tesseract.
What is Frank's Equation?

Simple Explanation (Non-Mathematical)

Imagine a 4-dimensional cube perfectly hovering in 3D space (X, Y, Z axes). As time extends infinitely, the 4D cube recursively subdivides into smaller 3D cubes. This process is governed by a secure cryptographic hash, the Mesh Function (\mathbf{s}_n), which dictates the geometry at every step.
The result is the Cognitectural Dimenscape—a geometric structure so complex that:
Provable Uniqueness: No two structures are identical. Each seed generates a provably different geometry (verified by Theorem 4).
Cryptographic Control: The geometry cannot be copied or altered without the original seed, enabling verified digital authorship.
It grows forever towards infinity, defining an infinite geometric family.

##Technical Overview
Frank's Equation \mathbf{F}_{n} is defined by the following triple, representing the n-th iterative state of the Tesseract:

**Fn = (Cn, An, Sn)**

| Component | Definition | Role |
| :---: | :--- | :--- |
| \mathbf{C}_{n} | Set of 3D cubes after n subdivisions | The generated geometric mesh. |
| \mathbf{A}{n} | Number of distinct dihedral angles in C{n} | The complexity metric. |
| \mathbf{s}_{n} | Mesh Function (Hash-Chain Recursion) | A SHA-256 hash value that deterministically controls the subdivision axis and ordering. |

Why "Frank's Equation"?
This work was inspired by Anne Frank's diary, which moved me deeply. The concept emerged at 4 AM on December 4, 2025, combining geometry, cryptography, and the power of infinite complexity.

## Contents

- `Franks_Equation_Naveen_2025.pdf` — Formal mathematical specification
- `frank_equation_CODE.py` — The reference Python implementation of the core recursion and Mesh Function Logic.
- `images/` — 23 hand-drawn proof's of complexity, including the **Evolutionary Recursion Diagram**, demonstrating the Mesh Function's control over the subdivision hierarchy, cognitectural dimscapes 
- 

## How to Replicate and Verify
To verify the deterministic nature of the \mathbf{s}_n Mesh Function, run the Python file:

Frank_equation_CODE.py

The script will output the hash chain (\mathbf{s}_n) and the deterministic control parameters (axis and permutation) for the first five iterations, demonstrating the injectivity of the system.

## Author

**Naveen** (Age 15)  
Created 4 December 2025

## License

MIT License - Free to use, modify, and distribute.

