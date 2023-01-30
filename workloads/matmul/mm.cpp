
#include <iostream>

#include "matrix.h"

#ifdef GEM5
#include "gem5/m5ops.h"
#endif


void multiply(double* A, double* B, double* C, int size)
{
    for (int i = 0; i < size; i++) {
        for (int k = 0; k < size; k++) {
            for (int j = 0; j < size; j++) {
                C[i * size + j] += A[i * size + k] * B[k * size + j];
            }
        }
    }
}

int main()
{
    std::cout << "Beginning matrix multiply ..." << std::endl;

#ifdef GEM5
    m5_work_begin(0,0);
#endif

    multiply(A, B, C, SIZE);

#ifdef GEM5
    m5_work_end(0,0);
#endif

    std::cout << "Finished matrix multiply." << std::endl;

    return 0;
}
