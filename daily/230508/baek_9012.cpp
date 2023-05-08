#include<iostream>
#include<stack>
#include<string>
using namespace std;

int main(){
    int line;
    cin>>line;
    for(int i=0;i<line;i++){
        // 문자열 선언
        string lst;
        // 스택 선언
        stack<char> stk;
        string ans ="YES";
        cin>>lst;
        for(int j=0;j<lst.length();j++){

            // ( 가 입력
            if(lst[j]=='('){
                stk.push('(');
            }
            // ) 가 입력
            else{
                // 스택이 비어있는 경우
                if(stk.size()==0){
                    ans = "NO";
                    break;
                }
                // 스택이 비어있지 않다면
                else{
                    stk.pop();
                }
            }
        }
        if(stk.size()!=0){
            ans="NO";
        }
        cout<<ans<<"\n";
    }
}