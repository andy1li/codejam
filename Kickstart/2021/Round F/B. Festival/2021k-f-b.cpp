// 2021 Kickstart Round F - B. Festival
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887dba

#include <bits/stdc++.h>
using namespace std;

#define rep(i, j, k) for (int i=j; i<=k; i++)
#define For(stop) rep(i, 0, stop-1)
#define pb push_back
using ll = long long;
using vi = vector<int>;

/*----------------------------------------------------------------------------*/ 
 
array<vi, 300001> ops, eds;
 
ll solve() {
    int D, N, K; cin >> D >> N >> K;

    vi H(N); 
    For(N) {
        int S, E; 
        cin >> H[i] >> S >> E;
        ops[--S].pb(i); eds[E].pb(i);
    }

    ll ans(0), curr(0);
    multiset<int> actives, subs;
    For(D+1) {
        for (int d: ops[i]) {
            actives.insert(H[d]);
            curr += H[d];
            if (actives.size() > K) {
                auto it = begin(actives);
                curr -= *it;
                subs.insert(*it);
                actives.erase(it);
            }
        }
        ops[i].clear();

        for (int d: eds[i]) {
            if (subs.find(H[d]) != end(subs)) {
                subs.erase( subs.find(H[d]) );
            } else {
                actives.erase( actives.find(H[d]) );
                curr -= H[d];
                if (subs.size()) {
                    auto it = --subs.end();
                    curr += *it;
                    actives.insert(*it);
                    subs.erase(it);
                }
            }
        }
        eds[i].clear();

        ans = max(ans, curr);
    }
    return ans;
}

/*----------------------------------------------------------------------------*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T; cin >> T;
    For(T) cout << "Case #" << i+1 << ": " << solve() << endl;
}