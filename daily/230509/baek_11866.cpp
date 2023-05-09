#include<iostream>
#include<queue>
using namespace std;
int main(){
    int len, num;
    queue<int> q;
    cin>>len>>num;

    int lst[len];
    int stk=0;
    int cnt=0;
    for(int i=1;i<len+1;i++){
        q.push(i);
    }
    while(1){
        if(q.size()==0){
            break;
        }
        if(cnt==num){
            lst[stk]=q.front();
            q.pop();
            stk++;
            cnt=0;
        }
        else{
            q.push(q.front());
            q.pop();
            }
        cnt++;
    }
    cout<<"<";
    for(int i=0;i<len;i++){
        if(len==1){
            cout<<len;
        }
        else{
            if(lst[i]==1){
                if(i==len-1){
                    cout<<len;
                }
                else{
                    cout<<len<<", ";
                }
            }
            else{
                if(i==len-1){
                    cout<<lst[i]-1;
                }
                else{
                    cout<<lst[i]-1<<", ";
                }
            }
        }
    }
    cout<<">";
}