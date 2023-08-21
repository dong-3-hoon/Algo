#include<iostream>
#include<string>
using namespace std;
int main(){
    int a;
    cin>>a;
    int b;
    string k;
    for(int i=0;i<a;i++){
        cin>>b>>k;
        for(int j=0;j<k.length();j++){
            for(int l=0;l<b;l++){
                cout<<k[j];
            }
        }
    cout<<endl;
    }
}