#include<iostream>
#include<queue>
using namespace std;
int main(){
    int num;
    queue<int> q;
    cin>>num;
    for(int i=1;i<num+1;i++){
        q.push(i);
    }
    while(1){
        if(q.size()==1){
            cout<<q.front();
            break;
        }
        q.pop();
        q.push(q.front());
        q.pop();
    }
}