#include<iostream>
using namespace std;
int main(){
    int N;
    cin>>N;
    int lst[N];
    for(int i=0;i<N;i++){
        cin>>lst[i];
    }
    int lst_n = 1000000, lst_m=-1000000;
    for(int i=0;i<N;i++){
        if(lst[i]<lst_n){
            lst_n=lst[i];
        }
        if(lst[i]>lst_m){
            lst_m=lst[i];
        }
    }
    cout<<lst_n<<" "<<lst_m;
}