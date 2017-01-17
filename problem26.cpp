#include <iostream>
#include <vector>
#include <string>
#include <map>


int main(){
	int longest = 0;
	int num_with_longest = 0;
	for(int i = 1; i < 1000 ; i++){
		std::string decimals = "";
		int value(0),remain(-1),current(1);
		while(value == 0){
			value = current / i;
			remain = current % i;
			current = remain * 10;
		}
		std::map<int,int> remain_to_index;
		int remain_index = 0;
		while(remain_to_index.find(remain) == remain_to_index.end()){
			decimals += std::to_string(value);
			remain_to_index[remain] = remain_index++;
			value = current / i;
			remain = current % i;
			current = remain * 10;
		}
		int location = remain_to_index[remain];
		int repeat_length = decimals.substr(location,decimals.length() - location).length();
		if( repeat_length > longest){
			longest = repeat_length;
			num_with_longest = i;
		}
	}
	std::cout << "Number with longest repeating sequence is: " << num_with_longest << std::endl; 
	return 0;
}
