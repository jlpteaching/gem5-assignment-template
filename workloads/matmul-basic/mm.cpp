#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <omp.h>

#ifdef GEM5
#include "gem5/m5ops.h"
#endif

using namespace std;

// Function to multiply matrices A and B, store result in C
void multiply(double **A, double **B, double **C, int size)
{
    for (int i = 0; i < size; i++) {
        for (int k = 0; k < size; k++) {
            for (int j = 0; j < size; j++) {
                C[i][j] += A[i][k] * B[k][j]; // Accumulate the product
            }
        }
    }
}

// Function to print a matrix
void printMatrix(double **A, int size)
{
    for (int i = 0; i < size; i++) {
        for (int j = 0; i < size; j++) {
            cout << setprecision(3) << setw(8) << A[i][j] << "  ";
        }
        cout << endl;
    }
}

int main(int argc, char *argv[])
{
    // Check for correct number of arguments
    if (argc != 2) {
        cout << "Usage: mm size" << endl;
        return 1;
    }

    // Convert argument to matrix size
    int size = atoi(argv[1]);

    // Validate matrix size
    if (size <= 0) {
        cout << "Invalid size" << endl;
        cout << "Usage: mm size" << endl;
    }

    cout << "Initializing the matrices...";

    // Initialize random number generator
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> dis(0, 1);

    // Allocate memory for matrices
    double *dataA = new double[size*size];
    double *dataB = new double[size*size];
    double *dataC = new double[size*size];

    double **A = new double*[size];
    double **B = new double*[size];
    double **C = new double*[size];

    // Fill matrices with random values
    for (int i = 0; i < size; i++) {
        A[i] = &dataA[size*i];
        B[i] = &dataB[size*i];
        C[i] = &dataC[size*i];
        for (int j = 0; j < size; j++) {
            A[i][j] = dis(gen);
            B[i][j] = dis(gen);
            C[i][j] = 0; // Initialize C matrix to zero
        }
    }

    cout << "Done." << endl;

    // Uncomment to print matrices
    // cout << "Matrix A:" << endl;
    // printMatrix(A, size);
    // cout << "Matrix B:" << endl;
    // printMatrix(B, size);

    cout << "Beginning multiply..." << endl;

    // Start timing
    auto start = std::chrono::high_resolution_clock::now();

#ifdef GEM5
    m5_work_begin(0,0); // Mark the beginning of work for GEM5
#endif

    multiply(A, B, C, size); // Perform matrix multiplication

#ifdef GEM5
    m5_work_end(0,0); // Mark the end of work for GEM5
#endif

    // End timing
    auto end = std::chrono::high_resolution_clock::now();

    cout << "Done." << endl;

    // Calculate and display elapsed time
    cout << "Time " << (double)(end-start).count()/1e6 << " ms" << endl;

    // Uncomment to print result matrix
    // cout << "Matrix C:" << endl;
    // printMatrix(C, size);

    // Deallocate memory
    delete[] A;
    delete[] B;
    delete[] C;
    delete[] dataA;
    delete[] dataB;
    delete[] dataC;

    return 0;
}
