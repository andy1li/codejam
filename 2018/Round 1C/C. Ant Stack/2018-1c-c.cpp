// Round 1C 2018 - C. Ant Stack 
// https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard/000000000003e0a8

// Solution adpated from https://codejam.withgoogle.com/2018/challenges/0000000000007765/attempts/for/SkyDec

#include <stdio.h>
#include <stdlib.h>
#include <climits>
#include <iostream>
using namespace std;

#define rep(i, j, k) for (int i=j; i<=k; ++i)
#define per(i, j, k) for (int i=j; i>=k; --i)
#define inf LLONG_MAX
typedef long long LL;
int num_cases, case_i = 1;

/* ########################################################################## */

const int magic = 139;
int n, weight;
LL dp[magic+1];

void solve() {
    dp[0] = 0; rep(i, 1, magic) dp[i] = inf;

    cin >> n;
    while (n--) {
        cin >> weight;
        per(i, magic, 1) {
            if (dp[i-1] <= 6LL * weight)
                dp[i] = min(dp[i], dp[i-1]+weight);
        }
    }

    int res = 0;
    rep(i, 1, magic) {
        if (dp[i] < inf) res = i;
    }
    printf("Case #%d: %d\n", ++case_i, res);
}

/* ########################################################################## */

int main() {
    if (getenv("__LOCAL__")) freopen("sample.in", "r", stdin);
    cin >> num_cases;
    while (num_cases--) solve();
    return 0;
}