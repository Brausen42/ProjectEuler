#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;


int main(){
	long count;
	long n;
	long max[2];
	max[0] = 1;
	max[1] = 1;
	for(long i = 2;i<1000000;i++){
		count = 0;
		n = i;
		while(n != 1){
			if(n%2 == 0)
				n = n/2;
			else
				n = (3*n)+1;
			count++;
		}
		if(count>max[1]){
			max[0] = i;
			max[1] = count;
		}
	}
	cout<<max[0]<<"\t"<<max[1]<<endl;
	return 0;
}