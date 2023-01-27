
#include <random>

#ifdef GEM5
#include "gem5/m5ops.h"
#endif

#define ARRAY_SIZE 1 << 20

int main()
{
    int data [ARRAY_SIZE];

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0, 1);

    for (int i = 0; i < ARRAY_SIZE; i++) {
        data[i] = dis(gen);
    }

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

    return 0;
}