#include<iostream>
using namespace std;
int main(){
    int N, v, cnt;
    cin>>N;
    int arr[N];
    for(int i=0;i<N;i++){
        cin>>arr[i];
    }
    cin>>v;
    cnt=0;
    for(int i=0;i<N;i++){
        if(arr[i]==v){
            cnt=cnt+1;
        }
    }
    cout<<cnt;
}