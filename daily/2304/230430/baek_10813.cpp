#include<iostream>
using namespace std;
int main(){
    int N, M;
    cin>>N>>M;
    int lst[N];
    for(int i=0;i<N;i++){
        lst[i]=i+1;
    }
    int i,j,tmp;
    for(int x=0;x<M;x++){
        cin>>i>>j;
        tmp=lst[i-1];
        lst[i-1]=lst[j-1];
        lst[j-1]=tmp;
    }
    for(int i=0;i<N;i++){
        cout<<lst[i]<<" ";
    }
}