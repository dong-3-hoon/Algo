#include<iostream>
using namespace std;
int main(){
    int lst[100][100]={0};
    int line, n,m;
    cin>>line;
    for(int i=0;i<line;i++){
        cin>>n>>m;
        for(int x=n;x<n+10;x++){
            for(int y=m;y<m+10;y++){
                lst[x][y] = 1;
            }
        }
    }
    int cnt=0;
    for(int i=0;i<100;i++){
        for(int j=0;j=100;j++){
            if(lst[i][j]==1){
                cnt++;
            }
        }
    }
    cout<<cnt;
}