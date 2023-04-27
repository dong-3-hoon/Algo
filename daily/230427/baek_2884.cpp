#include<iostream>
using namespace std;
int main(){
    int a,b;
    cin>>a>>b;
    if(b>=45){
        b=b-45;
    }
    else{
        if(a==0){
            a=23;
            b = 60-(45-b);
        }
        else{
            a--;
            b=60-(45-b);}
    }
    cout<<a<<' '<<b;
}