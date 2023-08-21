#include<iostream>
#include<queue>
#include<vector>
using namespace std;
vector<int> G[100001];
int bfs(int N, int M, int R){
    int visited[N+1] ={0};
    int t;
    queue<int> q;
    q.push(R);
    visited[R] = 1;
    while (!q.empty()){
        t= q.front();
        q.pop();
        for(int i=0;i<N; i++){
            if(visited[i]==0 && G[t][i] != 0){
                visited[i] = t+1;
                q.push(i);
            }
        }
    }
    for(int i=0;i<N+1;i++){
        cout<<visited[i];
    }
    return 0;
}

int main(){
    int N, M, R;
    int st, en;
    cin>>N>>M>>R;
    for(int i=0;i<N;i++){
        for(int j =0;j<N;j++){
            G[i][j]=0;
        }
    }
    for(int i=0;i<M;i++){
        cin>>st>>en;
        G[st][en] = 1;
        G[en][st] = 1;
    }
    bfs(N, M, R);
}