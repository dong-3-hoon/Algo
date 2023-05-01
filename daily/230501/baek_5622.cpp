#include<iostream>
#include<string>
using namespace std;
int main(){
    int cnt = 0;
    string k;
    cin>>k;
    for(int i=0;i<k.length();i++){
        if(k[i]=='A'||k[i]=='B'||k[i]=='C'){cnt=cnt + 3;}
        else if(k[i]=='D'||k[i]=='E'||k[i]=='F'){cnt = cnt + 4;}
        else if(k[i]=='G'||k[i]=='H'||k[i]=='I'){cnt = cnt + 5;}
        else if(k[i]=='J'||k[i]=='K'||k[i]=='L'){cnt = cnt + 6;}
        else if(k[i]=='M'||k[i]=='N'||k[i]=='O'){cnt = cnt + 7;}
        else if(k[i]=='P'||k[i]=='Q'||k[i]=='R'||k[i]=='S'){cnt = cnt + 8;}
        else if(k[i]=='T'||k[i]=='U'||k[i]=='V'){cnt = cnt + 9;}
        else if(k[i]=='W'||k[i]=='X'||k[i]=='Y'||k[i]=='Z'){cnt = cnt + 10;}
    }
    cout<<cnt;
}