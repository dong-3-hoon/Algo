#include<iostream>
using namespace std;
int main(){
    int a;
    int b=0, i_m=0, j_m=0;
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            cin>>a;
            if(a>b){
                b=a;
                i_m=i;
                j_m=j;
            }
        }
    }
    cout<<b<<"\n";
    cout<<i_m+1<<" "<<j_m+1;
}