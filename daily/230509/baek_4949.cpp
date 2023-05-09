#include<iostream>
#include<string>
#include<stack>
using namespace std;
int main(){
    while(1){
        string lst;
        string ans = "yes";
        int end=0;
        getline(cin, lst);
        stack<char> stk;
        for(int i=0; i<lst.length();i++){
            if(lst.length()==1){
                end=1;
                break;
            }
            // ( 나 [ 삽입 시 push
            if(lst[i]=='(' || lst[i]=='['){
                stk.push(lst[i]);
            }
            else if(lst[i]==')'){
                if(stk.size()==0){
                    ans="no";
                    break;
                }
                else{
                    if(stk.top()=='('){
                        stk.pop();
                    }
                    else{
                        ans ="no";
                        break;
                    }
                }
            }
            else if(lst[i]==']'){
                if(stk.size()==0){
                    ans="no";
                    break;
                }
                else{
                    if(stk.top()=='['){
                        stk.pop();
                    }
                    else{
                        ans ="no";
                        break;
                    }
                }
            }
            else if(lst[i]=='.'){
                if(stk.size()!=0){
                    ans="no";
                }
                break;
            }
        }
        if(end==0){
            cout<<ans<<"\n";
        }
        else{
            break;
        }
    }
}

