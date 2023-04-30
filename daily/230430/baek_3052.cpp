#include<iostream>
using namespace std;
int main(){
    int lst[42];
    int a;
    for(int i=0;i<42;i++){
        lst[i]=0;
    }
    for(int i=0;i<10;i++){
        cin>>a;
        a=a%42;
        lst[a]=1;
    }
    int cnt=0;
    for(int i=0;i<42;i++){
        if(lst[i]==1){
            cnt++;
        }
    }
    cout<<cnt;
}