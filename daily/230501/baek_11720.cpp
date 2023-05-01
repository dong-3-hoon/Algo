#include<iostream>
#include<string>
using namespace std;
int main(){
    int a;
    string b;
    cin>>a;
    cin>>b;
    int tot=0;
    for(int i=0;i<a;i++){
        tot = tot+int(b[i]-48);
    }
    cout<<tot;
}