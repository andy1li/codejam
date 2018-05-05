// https://codejam.withgoogle.com/2018/challenges/0000000000007765/attempts/for/SkyDec

#include<stdio.h>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<cmath>
#include<iostream>
#include<assert.h>
#include<queue>
#include<string>
#define rep(i,j,k) for(int i=(int)j;i<=(int)k;i++)
#define per(i,j,k) for(int i=(int)j;i>=(int)k;i--)
#define pii pair<int,int>
#define fi first
#define se second
#define pb push_back
using namespace std;
typedef long long LL;
const int N=110000;
const LL inf=1000000000000ll;
int n,m=140;
LL f[145];
int cas;
void Main(){
    scanf("%d",&n);
    rep(i,0,m)f[i]=inf;f[0]=0;
    while(n--){
        int x;scanf("%d",&x);
        per(i,m,0){
            if(f[i]<=6ll*x)f[i+1]=min(f[i+1],f[i]+x);
        }
    }
    int ans=0;
    rep(i,0,m)if(f[i]<inf)ans=i;
    printf("Case #%d: %d\n",++cas,ans);
}
int main(){
    int t;scanf("%d",&t);
    while(t--)Main();
    return 0;
}
