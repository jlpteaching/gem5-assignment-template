
#include <iostream>

#include "array.h"

#ifdef GEM5
#include "gem5/m5ops.h"
#endif

int main()
{
    std::cout << "Beginning bubble sort ... " << std::endl;

#ifdef GEM5
    m5_work_begin(0,0);
#endif

    for (int i = 0; i < ARRAY_SIZE - 1; i++) {
        for (int j = i + 1; j < ARRAY_SIZE; j++) {
            if (data[i] > data[j]) {
                int temp = data[i];
                data[i] = data[j];
                data[j] = temp;
            }
        }
    }

#ifdef GEM5
    m5_work_end(0,0);
#endif

    std::cout << "Finished bubble sort." << std::endl;

    return 0;
}
