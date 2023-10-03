#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define vi vector<int>
#define vll vector<long long>
#define map unordered_map
#define fast_io ios::sync_with_stdio(0); cin.tie(0);
#define rep(i, s, e, st) for (i = s; i < e; i += st)


void dfs(ll node, const vector<vll>& g, vector<bool>& vis) {
    int n = g.size();
    queue<ll> s;

    s.push(node);

    while(!s.empty()) {
        ll cur = s.front();
        s.pop();

        if (vis[cur]) continue;

        vis[cur] = true;
        
        ll i;
        rep(i, 0, g[cur].size(), 1) {
            s.push(g[cur][i]);
        }
    }

}

void solve() {
    ll n, m;
    cin >> n >> m;

    vector<vll> graph(n + 1);

    ll i;
    rep(i, 0, m, 1) {
        ll a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    vll sn;
    vector<bool> vis(n + 1, false);
    rep(i, 1, n + 1, 1) {
        if (!vis[i]) {
            sn.push_back(i);
            dfs(i, graph, vis);
        }
    }
    cout << sn.size() - 1 << endl;
    rep(i, 1, sn.size(), 1) {
        cout << sn[i - 1] << " " <<  sn[i] << endl;
    }
}

int main() {
    fast_io
    int t = 1; 
    while (t--) {
        solve();
    }
}