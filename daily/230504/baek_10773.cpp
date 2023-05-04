#include<iostream>
#include<stack>
using namespace std;
int main(){
    int line, a;
    stack<int> stk;
    cin>>line;
    for(int i=0;i<line;i++){
        cin>>a;
        if(a==0){
            stk.pop();
        }
        else{
            stk.push(a);
        }
    }
    int s=0;
    while(!stk.empty()){
        s= s+stk.top();
        stk.pop();
    }
    cout<<s;
}