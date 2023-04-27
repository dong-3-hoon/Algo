#include<iostream>
using namespace std;
int main(){
    int a;
    cin>>a;
    // 5줄 반복
    for(int i=0;i<a;i++){
        for(int j=1;j<a;j++){
            for(int k=a-1;k>-1;k--){
                cout<<" ";
            }
            cout<<"*";
        }
        cout<<"\n";
    }
}