#include <iostream>
#include <vector>
using namespace std;

using ll = long long;
#define rep(i, s, e, st) for (i = s; i < e; i += st)
#define vll vector<long long>

int main()
{
    ll n, q;
    cin >> n >> q;

    vector<vll> a(n, vll(n));
    ll i, j;
    rep(i, 0, n, 1)
    {
        rep(j, 0, n, 1)
        {
            char temp;
            cin >> temp;
            if (temp == '*')
            {
                a[i][j] = 1;
            }
        }
    }

    vector<vll> pref(n + 1, vll(n + 1, 0));

    rep(i, 1, n + 1, 1)
    {
        rep(j, 1, n + 1, 1)
        {
            pref[i][j] = a[i - 1][j - 1];
            pref[i][j] += (pref[i - 1][j] + pref[i][j - 1]) - pref[i - 1][j - 1];
        }
    }

    ll qrs;
    rep(qrs, 0, q, 1)
    {
        ll y1, x1, y2, x2;
        cin >> x1 >> y1 >> x2 >> y2;

        ll res = pref[x2][y2];
        res -= pref[x1 - 1][y2];
        res -= pref[x2][y1 - 1];
        res += pref[x1 - 1][y1 - 1];
        cout << res << endl;
    }
}
