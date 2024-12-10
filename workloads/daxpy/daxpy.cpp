#include <cstdio>
#include <random>

#ifdef GEM5
#include "gem5/m5ops.h"
#endif

int main()
{
  const int N = 131072;
  double X[N], Y[N], alpha = 0.5;
  std::random_device rd; std::mt19937 gen(rd());
  std::uniform_real_distribution<> dis(1, 2);
  for (int i = 0; i < N; ++i)
  {
    X[i] = dis(gen);
    Y[i] = dis(gen);
  }

#ifdef GEM5
m5_work_begin(0,0);
#endif

  // Start of daxpy loop
  for (int i = 0; i < N; ++i)
  {
    Y[i] = alpha * X[i] + Y[i];
  }
  // End of daxpy loop

#ifdef GEM5
    m5_work_end(0,0);
#endif

  double sum = 0;
  for (int i = 0; i < N; ++i)
  {
    sum += Y[i];
  }
  printf("%lf\n", sum);
  return 0;
}
