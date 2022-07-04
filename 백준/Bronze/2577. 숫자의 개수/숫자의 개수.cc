#include <iostream>

using namespace std;

int main(){
    int result[10] ={0, };
    int a, b, c;
    
    std::cin >> a;
    std::cin >> b;
    std::cin >> c;

    int total = a * b * c;
    int tmp = 0;
    while(total > 0) {
         tmp = total % 10;
         total /= 10;
         result[tmp] += 1;
    }
    for(int i=0; i<10; i++){
        std::cout << result[i] << "\n";
    }
    return 0;
}