#include<iostream>
using namespace std;
int main(){
    int N;
    cin>>N;
    float lst[N];
    int lst_m=0;
    int a;
    for(int i=0;i<N;i++){
        cin>>a;
        lst[i]=a;
        if(lst[i]>lst_m){
            lst_m=lst[i];
        }
    }
    for(int i=0;i<N;i++){
        lst[i]=lst[i]/lst_m*100;
    }
    float su=0;
    for(int i=0;i<N;i++){
        su = su+lst[i];
    }
    cout<<su/N;
}