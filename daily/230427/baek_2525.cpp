#include<iostream>
using namespace std;
int main(){
    int a,b,c;
    int d;
    cin>>a>>b;
    cin>>c;
    if(b+c>=60){
        a=a+(b+c)/60;
        b=(b+c)%60;
        }
    else{b=b+c;}
    if(a>=24){a=24-a;}
    cout<<abs(a)<<' '<<b;
    return 0;
}