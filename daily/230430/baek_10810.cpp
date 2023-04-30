#include<iostream>
using namespace std;
int main(){
    int N, M;
    cin>>N>>M;
    int lst[N+1];
    for(int i=0;i<N+1;i++){
        lst[i]=0;
    }
    for(int K=0;K<M;K++){
        int i,j,k;
        cin>>i>>j>>k;
        for(i+1;i<j+1;i++){
            lst[i]=k;
        }
    }
    for(int i=1;i<N+1;i++){
        cout<<lst[i]<<" ";
    }
}