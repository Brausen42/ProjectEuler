#include <stdio.h>
#include <stdlib.h>

long long largestPrimeFactor(long long n);

int main(int argc, char const *argv[]) {

  long long num = 600851475143;

  printf("%lld\n", largestPrimeFactor(num));

  return 0;
}

long long largestPrimeFactor(long long n){
  if(n < 1){
    // function only supports positive numbers
    return -1;
  }
  long long divisor = 2;
  long long n_copy = n;
  while(n_copy != 1){
    if(n_copy % divisor == 0){
      n_copy = n_copy / divisor;
    } else {
      divisor++;
    }
  }
  return divisor;
}
