#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define vi vector<int>
#define vll vector<long long>
#define map unordered_map
#define fast_io ios::sync_with_stdio(0); cin.tie(0);
#define rep(s, e, st) for (int i = s; i < e; i += st)

void solve() {
    ll n, x;
    cin >> n >> x;

    pair<ll, ll> p[n];
    rep(0, n, 1) {
        int temp;
        cin >> temp;
        p[i].first = temp;
        p[i].second = i;
    }

    ll l = 0, r = n - 1;
    sort(p, p + n);

    // for (auto e:p) {
    //     cout << e.first << " " << e.second << endl;
    // }

    while (l < r) {
        int s = p[l].first + p[r].first;
        if (s < x) {
            l += 1;
        }
        else if (s > x) {
            r += 1;
        }
        else {
            // cout << p[l].first << " " << p[r].first << endl;
            cout << p[l].second + 1 << " " << p[r].second + 1 << endl;
            return;
        }
    }

    cout << "IMPOSSIBLE" << endl;

}

int main() {
    fast_io
    int t = 1;
    while (t--) {
        solve();
    }
}