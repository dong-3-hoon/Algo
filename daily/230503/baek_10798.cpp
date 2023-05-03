#include<iostream>
#include<string>
using namespace std;
int main(){
    string lst[5][15];
    string stk;
    int cnt=0;
    while(cnt<5){
        cin>>stk;
        for(int i=0;i<stk.length();i++){
            lst[cnt][i]=stk[i];
        }
        cnt++;
    }
    for(int i=0;i<15;i++){
        for(int j=0;j<5;j++){
            if(lst[j][i] != "\0")
                cout<<lst[j][i];
        }
    }
}