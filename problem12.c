#include <stdio.h>
#include <stdlib.h>
int triangle(int n);
int divisors(int n);
int main(){
	int divise = 0;
	int num = 1;
	int i = 1;
	while(divise<500){
		num = triangle(i);
		divise = divisors(num);
		printf("The triangle sum %d has %d divisors\n",num,divise);
		i++;
	}
	return 0;
}

int triangle(int n){
	int sum = 0;
	for(int i = 0;i<n;i++){
		sum += i+1;
	}
	return sum;
}

int divisors(int n){
	int div = 0;
	for(int i=1;i<n;i++){
		if(n%i == 0){
			div++;
		}
	}
	return div;
}
