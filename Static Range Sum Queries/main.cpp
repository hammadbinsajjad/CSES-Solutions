#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define vi vector<int>
#define vll vector<long long>
#define map unordered_map
#define fast_io ios::sync_with_stdio(0); cin.tie(0);
#define rep(i, s, e, st) for (i = s; i < e; i += st)

void solve() {
    ll n, q;
    cin >> n >> q;

    vll a(n);

    ll i;
    rep(i, 0, n, 1) {
        cin >> a[i];
    }

    deque<ll> pref(n, 0);

    rep(i, 0, n, 1) {
        if (i == 0) {
            pref[i] = a[i];
        }
        else {
            pref[i] = pref[i - 1] + a[i];
        }
    }

    pref.push_front(0);

    ll qr;
    rep(qr, 0, q, 1) {
        ll a, b;
        cin >> a >> b;
        cout << pref[b] - pref[a - 1] << endl;
    }

}

int main() {
    fast_io
    int t = 1; 
    // cin >> t;
    while (t--) {
        solve();
    }
}