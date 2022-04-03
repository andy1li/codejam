// 202X Round X - X. FOOBAR
// https://

#include <bits/stdc++.h>
using namespace std;

#define rep(i, j, k) for (int i=j; i<=k; ++i)
#define per(i, j, k) for (int i=j; i>=k; --i)
#define For(stop) rep(i, 0, stop-1)
#define all(c) begin(c), end(c)
#define len(c) c.size()
#define each(x, c) for (auto& x: c)
#define in(x, c) c.find(x) != end(c)
#define del(c, x) c.erase( c.find(x) )
#define last(c) --c.end()
#define print(x) cout << x << endl;
#define prints(c) each(x, c) cout << x << ' '; cout << endl
#define inf LLONG_MAX
#define pb push_back
using ll = long long;
using vi = vector<int>;

/*----------------------------------------------------------------------------*/

ll solve() {
    print("12345");
    return 0;
}

/*----------------------------------------------------------------------------*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int T; cin >> T; For(T) 
        cout << "Case #" << i+1 << ": " << solve() << endl;
}