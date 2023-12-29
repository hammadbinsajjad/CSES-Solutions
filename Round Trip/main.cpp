#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<bool> visited;
vector<int> parent;

int cycle_start, cycle_end;

bool dfs(vector<vector<int>>& g, int u, int p) {
    visited[u] = true;

    for (int v:g[u]) {
        if (v == p) continue;
        else {
            if (visited[v]) {
                cycle_start = v;
                cycle_end = u;
                return true;
            }
            parent[v] = u;
            if (dfs(g, v, u)) return true;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, m; cin >> n >> m;

    cycle_start = -1;

    visited.assign(n, false);
    parent.assign(n, -1);
    vector<vector<int>> graph(n);

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graph[--a].push_back(--b);
        graph[b].push_back(a);
    }

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            bool r = dfs(graph, i, -1);
            if (r) break;
        }
    }


    if (cycle_start == -1) {
        cout << "IMPOSSIBLE" << endl;
        return 0;
    }
    else {
        vector<int> path;
        path.push_back(cycle_start);
        for (int cur = cycle_end; cur != cycle_start; cur = parent[cur]) {
            path.push_back(cur);
        }
        path.push_back(cycle_start);
        reverse(path.begin(), path.end());

        cout << path.size() << '\n';
        for (int i:path) {
            cout << i + 1 << " ";
        }
        cout << "\n";
    }


}
