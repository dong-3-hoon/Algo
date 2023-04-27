#include<iostream>
#include<algorithm>
using namespace std;
int main(){
    int lst[3];
    int a;
    for(int i=0;i<3;i++){
        cin>>a;
        lst[i]=a;
    }
    sort(lst, lst+3);
    if(lst[2]==lst[0]){
        a=10000+lst[0]*1000;
    }
    else if(lst[0]==lst[1]){
        a=1000+lst[0]*100;
    }
    else if(lst[1]==lst[2]){
        a=1000+lst[2]*100;
    }
    else{
        a=lst[2]*100;
    }
    cout<<a;
}