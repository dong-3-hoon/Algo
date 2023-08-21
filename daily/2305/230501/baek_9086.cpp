#include<iostream>
#include<string>
using namespace std;
int main(){
    int num;
    cin>>num;
    string st;
    for(int i=0;i<num;i++){
        cin>>st;
        cout<<st[0]<<st[st.length()-1]<<endl;
    }
}