#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define vi vector<int>
#define vll vector<long long>
#define map unordered_map
#define fast_io ios::sync_with_stdio(0); cin.tie(0);
#define rep(s, e, st) for (int i = s; i < e; i += st)

void solve() {
    ll n, m, k; cin >> n >> m >> k;
    ll a[n], b[n];

    rep(0, n, 1) {
        cin >> a[i];
    }
    rep(0, m, 1) {
        cin >> b[i];
    }

    sort(a, a + n);
    sort(b, b + n);

    ll u = 0;
    ll d = 0;
    ll c = 0;

    while (u < n && d < m) {
        cout << a[u] << " " << b[d] << endl;
        ll s = b[d];
        if (s >= a[u] - k && s <= a[u] + k) {
            c += 1;
            u += 1;
            d += 1;
        }
        else if (s < a[u]) {
            d += 1;
        }
        else if (s > a[u]) {
            u += 1;
        }
    }
    cout << c << endl;
}

int main() {
    fast_io
    int t; t = 1;
    while (t--) {
        solve();
    }
}