#include<iostream>
#include<string>
using namespace std;
int main(){
    string k;
    cin>>k;
    int lst[26];
    for (int i=0;i<26;i++){
        lst[i] = -1;
    }
    for(int i=0;i<k.length();i++){
        if(lst[(int) k[i]-97]==-1){
            lst[(int) k[i]-97]=i;
        }
        //-97
    }
    for(int i=0;i<26;i++){
        cout<<lst[i]<<" ";
    }
}