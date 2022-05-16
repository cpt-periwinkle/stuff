#include <bits/stdc++.h>
#include <iostream>

using namespace std;
class Queue{
public:
    int size1;
    int f;        //front for deletion
    int r;        //rear for insertion
    int *a;
};
void enqueue(Queue *st,int data){
    if(st->r==st->size1-1){
        cout<<"Queue FULL"<<endl;
    }
    else{
        st->r++;
        st->a[st->r]=data;
    }
}
int dequeue(Queue *st){
    int x=-1;
    if(st->f==st->r){
        cout<<"Queue Empty"<<endl;
    }
    else{
        st->f++;
        x=st->a[st->f];
    }
    return x;
}
int isempty(Queue *st){
    if(st->f==st->r){
        return 1;
    }
    return 0;
}
int arr[8][8]= {{0,0,0,0,0,0,0,0},
                {0,0,1,1,1,0,0,0},
                {0,1,0,1,0,0,0,0},
                {0,1,1,0,1,1,0,0},
                {0,1,0,1,0,1,0,0},
                {0,0,0,1,1,0,1,1},
                {0,0,0,0,0,1,0,0},
                {0,0,0,0,0,1,0,0}};
class graph{
public:
    int *visited;
};
void bfs(graph *t,Queue *q,int i){
    cout<<i<<" ";
    t->visited[i]=1;
    enqueue(q,i);
    while(!isempty(q)){
        int u=dequeue(q);
        for(int j=1;j<=8;j++){
            if(arr[u][j]==1&&t->visited[j]==0){
                cout<<j<<" ";
                t->visited[j]=1;
                enqueue(q,j);
            }
        }
    }

}
void dfs(int u){
    static int visited[8]={0};
    if(visited[u]==0){
        cout<<u<<" ";
        visited[u]=1;
        for(int i=1;i<=8;i++){
            if(arr[u][i]==1 && visited[i]==0){
                dfs(i);
            }
        }
    }
}
int main()
{
    cout<<"*******MENU*******"<<'\n';
    cout<<"1.BFS"<<'\n';
    cout<<"2.DFS"<<'\n';
    cout<<"3.Exit"<<'\n';
    int e=0;
    int c;
    while(e==0){
        cout<<'\n'<<"Enter Choice"<<'\n';
        cin>>c;
        switch(c){
            case 1:{
                graph t;
                Queue s;
                s.f=-1;
                s.r=-1;
                s.size1=8;
                s.a=new int[8];
                t.visited=new int[8];
                for(int i=0;i<8;i++){
                    t.visited[i]=0;
                }
                int c1;
                cout<<"Enter starting Vertex(1-7)"<<'\n';
                cin>>c1;
                bfs(&t,&s,c1);
                break;
            }
            case 2:{
                int c1;
                cout<<"Enter starting Vertex(1-7)"<<'\n';
                cin>>c1;
                dfs(c1);
                break;
            }
            case 3:{
                cout<<"Thank-You"<<'\n';
                e=1;
                break;
            }
        }
    }
    return 0;
}
