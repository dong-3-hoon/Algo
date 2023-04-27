#include<iostream>
#include<string>
using namespace std;
int main(){
    int a;
    string b;
    cin>>a;
    cin>>b;
    for(int i=b.length()-1;i>-1;i--){
        cout<<(a*(b[i]-'0'))<<endl;
    };
    cout<<(a*stoi(b))<<endl;
    return 0;
}