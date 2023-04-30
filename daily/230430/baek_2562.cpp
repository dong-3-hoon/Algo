#include<iostream>
using namespace std;
int main(){
    int lst[9];
    for(int i=0;i<9;i++){
        cin>>lst[i];
    }
    int lst_m=0, lst_ind=0;

    for(int i=0;i<9;i++){
        if(lst[i]>lst_m){
            lst_m=lst[i];
            lst_ind=i;
        }
    }
    cout<<lst_m<<endl;
    cout<<lst_ind+1;
}