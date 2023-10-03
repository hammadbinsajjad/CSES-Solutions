#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define vi vector<int>
#define vll vector<long long>
#define fast_io ios::sync_with_stdio(0); cin.tie(0);
#define rep(i, s, e, st) for (i = s; i < e; i += st)

void solve() {
    ll n, q; cin >> n >> q;

    vll a(n);
    ll i;
    vector<vll> m(n, vll((int)log2(n) + 1, 0));
    rep(i, 0, n, 1) {
        cin >> a[i];
        m[i][0] = a[i];
    }

    // Preprocess
    ll j;
    rep(j, 1, log2(n) + 1, 1) {
        for(i = 0; (i + pow(2, j) - 1) < n; i++) {
            m[i][j] = min(m[i][j - 1], m[i + (int)pow(2,j - 1)][j - 1]);
        }
    }

    vi bin_log(n + 1);
    bin_log[1] = 0;
    rep(i, 2, n + 1, 1) {
        bin_log[i] = bin_log[i/2] + 1;
    }
    ll _;
    rep(_, 0, q, 1) {
        ll l, r;
        cin >> l >> r;
        l -= 1;
        r -= 1;

        ll len = r - l + 1;

        ll p2 = bin_log[len];

        cout << min(m[l][p2], m[r-pow(2, p2) + 1][p2]) << endl;
    }
}

int main() {
    fast_io
    int t = 1;
    while (t--) {
        solve();
    }
}