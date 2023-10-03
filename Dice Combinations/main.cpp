#include <iostream>
#include <vector>

using namespace std;

using ll = long long;

int main() {
    int n; cin >> n;

    vector<ll> dp(n + 1, 0);
    dp[1] = 1;
    dp[2] = 2;

    for (int i = 3; i <= n; i++) {
        for (int j = 1; j <= 6; j++) {
            if (i - j > 0) {
                dp[i] = (dp[i] + dp[i - j]) % (ll)(1e9 + 7);
            }
        }
        if (i <= 6)
            dp[i] += 1;
    }

    cout << dp[n];
    cout << endl;
}
