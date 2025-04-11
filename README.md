# Sparse-Matrix


Sparse Matrix Implementation
==========================

Overview
--------

This project implements a sparse matrix data structure and provides functions for basic matrix operations such as addition, subtraction, and multiplication.

Features
--------

*   **Sparse Matrix Representation**: The matrix is represented using a dictionary to store non-zero elements, which reduces memory usage and improves performance.
*   **Matrix Operations**: The implementation provides functions for matrix addition, subtraction, and multiplication, which are optimized for performance.
*   **Input File Parsing**: The implementation includes a function to parse input files and read matrix data, which supports a variety of file formats.
*   **Output File Generation**: The implementation includes a function to generate output files and write matrix data, which supports a variety of file formats.

Usage
-----

### Running the Program

1.  Clone the repository to your local machine using `git clone`.
2.  Navigate to the project directory using `cd`.
3.  Run the `matrix.py` file using Python (e.g., `python matrix.py`).
4.  Follow the prompts to select the matrix operation and input files.

### Input File Format

The input file should be in the following format:


rows=<number of rows>
cols=<number of columns>
(row, col, value)
(row, col, value)
...


For example:


rows=8433
cols=3180
(0, 381, -694)
(0, 128, -838)
(0, 639, 857)
(0, 165, -933)
(0, 1350, -89)


### Output File Format

The output file will be in the same format as the input file.


Requirements
------------

*   **Python 3.x**: The implementation requires Python 3.x to run.
*   **No External Libraries**: The implementation does not require any external libraries.

Note
----

*   **Error Handling**: The implementation assumes that the input files are in the correct format and does not perform any error checking. You may want to add error checking to handle invalid input files.
*   **Performance**: The implementation is designed to be efficient in terms of memory usage and computational complexity. However, the performance may vary depending on the size of the input files and the matrix operations.

Input Files
------------

*   The input files should be placed in the `/dsa/sparse_matrix/sample_inputs/` directory.

Output Files
------------

*   The output files will be generated in the same directory as the input files.
