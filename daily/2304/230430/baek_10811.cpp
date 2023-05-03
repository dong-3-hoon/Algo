#include<iostream>
#include<string>
#include <algorithm>
using namespace std;
int main(){
    int N,M;
    cin>>N>>M;
    int lst[N+1];
    for(int i=0;i<N+1;i++){
        lst[i]=i;
    }
    for(int i=0;i<M;i++){
        int a,b;
        cin>>a>>b;
        reverse(lst+a, lst+b);
    }
    for(int i=1;i<N+1;i++){
        cout<<lst[i]<<" ";
    }
}