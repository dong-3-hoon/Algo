#include<iostream>
#include<stack>
#include<string>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int line;
    cin>>line;
    string order;
    stack<int> stk;
    int num;
    for(int i=0;i<line;i++){
        cin>>order;
        if(order=="push"){
            cin>>num;
            stk.push(num);
        }
        else if(order=="top"){
            if(stk.empty()){
                cout<<-1<<"\n";
            }
            else{
                cout<<stk.top()<<"\n";
            }
        }
        else if(order=="size"){
            cout<<stk.size()<<"\n";
        }
        else if(order=="empty"){
            if(stk.empty()){
                cout<<1<<"\n";
            }
            else{
                cout<<0<<"\n";
            }
        }
        else if(order=="pop"){
            if(stk.empty()){
                cout<<-1<<"\n";
            }
            else{
                cout<<stk.top()<<"\n";
                stk.pop();
            }
        }
    }
}