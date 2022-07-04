#include <iostream>

using namespace std;

int main(){
    int counter[42]={0, };
    int input[10];
    int result = 0;
    for(int i=0; i<10;i++){
        std::cin >> input[i];
        counter[input[i]%42] = 1; 
    }
    for(int i=0;i<sizeof(counter)/sizeof(int);i++){
        if(counter[i] > 0) {
            result += 1;
        }
    }
    std::cout << result;

    return 0;
}