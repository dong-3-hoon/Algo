#include<iostream>
#include<string>
#include<queue>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int line;
    string a;
    int num;
    queue<int> q;
    cin>>line;
    for(int i=0;i<line;i++){
        cin>>a;
        if(a=="push"){
            cin>>num;
            q.push(num);
        }
        else if(a=="pop"){
            if(q.size()==0){
                cout<<-1<<"\n";
            }
            else{
                cout<<q.front()<<"\n";
                q.pop();
            }
        }
        else if(a=="size"){
            cout<<q.size()<<"\n";
        }
        else if(a=="empty"){
            if(q.size()==0){
                cout<<1<<"\n";
            }
            else{
                cout<<0<<"\n";
            }
        }
        else if(a=="front"){
            if(q.size()==0){
                cout<<-1<<"\n";
            }
            else{
                cout<<q.front()<<"\n";
            }
        }
        else if(a=="back"){
            if(q.size()==0){
                cout<<-1<<"\n";
            }
            else{
                cout<<q.back()<<"\n";
            }
        }
    }
}