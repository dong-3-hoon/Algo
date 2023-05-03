#include<iostream>
using namespace std;
int main(){
    int a, b, c, d;
    cin>>a>>b;
    int lst1[a][b]{0};
    int lst2[a][b]{0};
    for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            cin>>c;
            lst1[i][j]=c;
        }
    }
    for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            cin>>c;
            lst2[i][j]=c;
        }
    }
    for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            cout<<lst1[i][j]+lst2[i][j]<<" ";
        }
        cout<<endl;
    }
}