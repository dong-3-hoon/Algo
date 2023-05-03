#include<iostream>

int main(){
    double a, b;
    double c;
    std::cin >> a >>b;
    c = a/b;
    std::cout.precision(10);
    std::cout<<c;
    return 0;
}