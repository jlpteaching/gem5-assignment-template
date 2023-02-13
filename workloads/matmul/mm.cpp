#include <iostream>

#ifdef IJK
#include "ijk_multiply.h"
#endif

#ifdef IKJ
#include "ikj_multiply.h"
#endif

#ifdef GEM5
#include "gem5/m5ops.h"
#endif

int main(int argc, char** argv)
{
    std::cout << "Beginning matrix multiply ..." << std::endl;

#if defined(IJK) || defined(IKJ)

#endif

#if defined(IJ) || defined(IK) || defined(Kj)
#endif

#ifdef GEM5
    m5_work_begin(0,0);
#endif

#if defined(IJK) || defined(IKJ)
    multiply(A, B, C, size);
#endif

#if defined(IJ) || defined(IK) || defined(Kj)
#endif

#ifdef GEM5
    m5_work_end(0,0);
#endif

    std::cout << "Finished matrix multiply." << std::endl;

    return 0;
}
