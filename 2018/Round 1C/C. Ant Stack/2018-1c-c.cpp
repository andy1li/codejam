// Round 1C 2018 - C. Ant Stack 
// https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard/000000000003e0a8

// Solution adpated from https://codejam.withgoogle.com/2018/challenges/0000000000007765/attempts/for/SkyDec

#include <stdio.h>
#include <iostream>
#include <climits>
using namespace std;

#define rep(i, j, k) for (int i=j; i<=k; i++)
#define per(i, j, k) for (int i=j; i>=k; i--)
#define inf LLONG_MAX
typedef long long LL;
int case_i = 0;
int t, magic=139;
LL dp[139+1];

void solve(){
    rep(i, 1, magic) dp[i] = inf;
    dp[0] = 0;

    int n; cin >> n;
    while (n--) {
        int weight; cin >> weight;
        per(i, magic, 1) {
            if (dp[i-1] <= 6LL * weight)
                dp[i] = min(dp[i], dp[i-1]+weight);
        }
    }

    int res = 0;
    rep(i, 1, magic)
        if (dp[i] < inf) res = i;
    printf("Case #%d: %d\n", ++case_i, res);
}

int main(){
    freopen("sample.in", "r", stdin);
    cin >> t;
    while (t--) solve();
    return 0;
}
