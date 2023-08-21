#include<iostream>
#include<string>
using namespace std;
int main(){
    string st;
    getline(cin, st);
    int cnt = 1;
    for(int i=0;i<st.length();i++){
        if(st.length()==1&&st[0]==' '){
            cnt = 0;
            break;
        }
        if(st[i]==' '){
            if(i!=0&&i!=st.length()-1){
                cnt++;
            }
        }
    }
    cout<<cnt;
}