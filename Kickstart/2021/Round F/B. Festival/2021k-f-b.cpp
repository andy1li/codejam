// 2021 Kickstart Round F - B. Festival
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887dba

#include <bits/stdc++.h>
using namespace std;

#define rep(i, j, k) for (int i=j; i<=k; i++)
#define For(stop) rep(i, 0, stop-1)
#define len(c) c.size()
#define each(x, c) for (auto& x: c)
#define in(x, c) c.find(x) != end(c)
#define del(c, x) c.erase( c.find(x) )
#define last(c) --c.end()
#define pb push_back
using ll = long long;
using vi = vector<int>;

/*----------------------------------------------------------------------------*/ 
 
array<vi, 300001> ss, es;

ll solve() {
    int D, N, K; cin >> D >> N >> K;

    For(N) {
        int h, s, e; cin >> h >> s >> e;
        ss[--s].pb(h); es[e].pb(h);
    }

    ll ans(0), curr(0);
    multiset<int> actives, subs;
    For(D+1) {
        each(h, ss[i]) {
            actives.insert(h); curr += h;
            if (len(actives) > K) {
                auto it = begin(actives); actives.erase(it);
                subs.insert(*it); curr -= *it;
            }
        }
        ss[i].clear();

        each(h, es[i]) {
            if (in(h, subs)) {
                del(subs, h);
            } else {
                del(actives, h); curr -= h;
                if (len(subs)) {
                    auto it = last(subs); subs.erase(it);
                    actives.insert(*it); curr += *it;       
                }
            }
        }
        es[i].clear();

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