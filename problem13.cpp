#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;


int main(){
	ifstream in;
	string s("fifty.txt");
	in.open(s.c_str());
	long carry(0);
	char temp[50];
	long sum[50];
	int total[75];
	for(int i = 0;i<75;i++)
		total[i] = 0;
	for(int i = 0;i<50;i++)
		sum[i] = 0;
	for(int j = 0;j<100;j++){
		
		for(int i = 0;i<50;i++)
			in>>temp[i];
		for(int i = 0;i<50;i++)
			sum[i] += (int)temp[i]-('0');
	}
	for(int i = 74;i>=0;i--){
		if(i>=25){
			total[i] = (sum[i-25]+carry)%10;
			carry = (sum[i-25]+carry)/10;
		}
		else{
			total[i] = carry%10;
			carry = carry/10;
		}
	}
	bool start(false);
	for(int i = 0;i<75;i++){
		if(total[i] > 0)
			start = true;
		if(start)
			cout<<total[i];
	}
	cout<<endl;
	return 0;
}