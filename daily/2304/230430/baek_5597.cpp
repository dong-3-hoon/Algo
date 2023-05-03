#include<iostream>
using namespace std;
int main(){
    int a;
    int lst[31];
    for(int i=0;i<31;i++){
        lst[i]=0;
    }
    lst[0]=1;
    for(int i=0;i<28;i++){
        cin>>a;
        lst[a]=1;
    }
    for(int i=0;i<31;i++){
        if(lst[i]==0){
            cout<<i<<endl;
        }
    }
}